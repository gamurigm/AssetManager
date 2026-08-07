# OpenBB Economy Endpoints Research

Current integration in MMAM Intelligence Core via `macro_economy.py` and `openbb_config.py`.

## Core Endpoints (Integrated)

| Command | Provider | Description |
|:---|:---|:---|
| **economy.gdp.nominal** | `oecd` | Nominal GDP by country (Default: United States) |
| **economy.cpi** | `fred` | Consumer Price Index (HICP for OECD, CPIAUCSL for FRED) |
| **economy.fred_series** | `fred` | Generic FRED data loader (used for `FEDFUNDS` and `UNRATE`) |
| **economy.calendar** | `fmp` | Economic events (upcoming releases) |

## Additional Router Groups

### 1. Survey Data (`economy.survey`)
- **economy.survey.bls_series**: Labor statistics from Bureau of Labor Statistics. Useful for non-farm payrolls, job openings (JOLTS).
- **economy.survey.economic_sentiment**: UMICH consumer sentiment index.

### 2. Shipping & Trade (`economy.shipping`)
- **economy.shipping.chokepoint_info**: Real-time traffic for Suez/Panama canals.
- **economy.shipping.port_info**: Terminal congestion and wait times.

### 3. Fixed Income Correlations
- **fixedincome.government.treasury_rates**: Not in economy router but closely related. Yield curve data for 3M to 30Y tenors.

## CLI Aliases
The terminal supports shorthand notation:
- `gdp` → `economy.gdp.nominal`
- `cpi` → `economy.cpi`
- `calendar` → `economy.calendar`
- `treasury` → `fixedincome.government.treasury_rates`
