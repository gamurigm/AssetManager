# Kill any process listening on port 8282 (Backend)
$port = 8282
$tcp = Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue

if ($tcp) {
    echo "Found process on port $port. Terminating..."
    Stop-Process -Id $tcp.OwningProcess -Force
    echo "Backend process terminated."
} else {
    echo "No process found on port $port."
}
