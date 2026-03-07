param(
    [int]$Port = 9092,
    [switch]$SkipBuild,
    [ValidateSet("Normal", "Minimized", "Maximized", "Hidden")]
    [string]$WindowStyle = "Minimized",
    [int]$HealthTimeoutSeconds = 15
)

$ErrorActionPreference = "Stop"

$rootPath = $PSScriptRoot
$coreEnginePath = Join-Path $rootPath "core_engine"
$buildPath = Join-Path $coreEnginePath "build"
$serviceUrl = "http://127.0.0.1:$Port"

function Test-PortfolioCppHealth {
    param([string]$Url)

    try {
        $response = Invoke-RestMethod -Uri "$Url/health" -TimeoutSec 2
        return $response.service -eq "portfolio_cpp_service"
    }
    catch {
        return $false
    }
}

function Find-PortfolioCppExecutable {
    $candidates = @(
        (Join-Path $buildPath "portfolio_cpp_service.exe"),
        (Join-Path $buildPath "Release\portfolio_cpp_service.exe"),
        (Join-Path $buildPath "Debug\portfolio_cpp_service.exe"),
        (Join-Path $buildPath "RelWithDebInfo\portfolio_cpp_service.exe"),
        (Join-Path $buildPath "MinSizeRel\portfolio_cpp_service.exe")
    )

    foreach ($candidate in $candidates) {
        if (Test-Path $candidate) {
            return $candidate
        }
    }

    return $null
}

function Ensure-PortfolioCppExecutable {
    $existingExecutable = Find-PortfolioCppExecutable
    if ($existingExecutable) {
        return $existingExecutable
    }

    if ($SkipBuild) {
        throw "portfolio_cpp_service.exe was not found under $buildPath"
    }

    Write-Host "[portfolio_cpp_service] Configuring CMake build..." -ForegroundColor Cyan
    & cmake -S $coreEnginePath -B $buildPath
    if ($LASTEXITCODE -ne 0) {
        throw "CMake configure failed for portfolio_cpp_service"
    }

    Write-Host "[portfolio_cpp_service] Building standalone service target..." -ForegroundColor Cyan
    & cmake --build $buildPath --target portfolio_cpp_service --config Release
    if ($LASTEXITCODE -ne 0) {
        throw "CMake build failed for portfolio_cpp_service"
    }

    $builtExecutable = Find-PortfolioCppExecutable
    if (-not $builtExecutable) {
        throw "Build completed but portfolio_cpp_service.exe was not found"
    }

    return $builtExecutable
}

$env:PORTFOLIO_CPP_SERVICE_URL = $serviceUrl

if (Test-PortfolioCppHealth -Url $serviceUrl) {
    Write-Host "[portfolio_cpp_service] Already healthy at $serviceUrl" -ForegroundColor Green
    Write-Host "[portfolio_cpp_service] PORTFOLIO_CPP_SERVICE_URL=$serviceUrl" -ForegroundColor DarkCyan
    return
}

$portListeners = @(Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess -Unique)
if ($portListeners.Count -gt 0) {
    throw "Port $Port is already in use by PID(s): $($portListeners -join ', ')"
}

$serviceExecutable = Ensure-PortfolioCppExecutable
$workingDirectory = Split-Path $serviceExecutable -Parent

Write-Host "[portfolio_cpp_service] Starting standalone service on $serviceUrl" -ForegroundColor Green
$process = Start-Process -FilePath $serviceExecutable -ArgumentList @("$Port") -WorkingDirectory $workingDirectory -WindowStyle $WindowStyle -PassThru

for ($attempt = 0; $attempt -lt $HealthTimeoutSeconds; $attempt++) {
    Start-Sleep -Seconds 1

    if ($process.HasExited) {
        throw "portfolio_cpp_service exited early with code $($process.ExitCode)"
    }

    if (Test-PortfolioCppHealth -Url $serviceUrl) {
        Write-Host "[portfolio_cpp_service] Healthy at $serviceUrl (PID $($process.Id))" -ForegroundColor Green
        Write-Host "[portfolio_cpp_service] PORTFOLIO_CPP_SERVICE_URL=$serviceUrl" -ForegroundColor DarkCyan
        return
    }
}

throw "portfolio_cpp_service did not answer on $serviceUrl within $HealthTimeoutSeconds seconds"