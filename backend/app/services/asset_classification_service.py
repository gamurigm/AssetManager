from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Any

from .fmp_service import fmp_service


SECTOR_TO_ETF: dict[str, str] = {
    "Information Technology": "XLK",
    "Health Care": "XLV",
    "Financials": "XLF",
    "Consumer Discretionary": "XLY",
    "Consumer Staples": "XLP",
    "Energy": "XLE",
    "Industrials": "XLI",
    "Materials": "XLB",
    "Utilities": "XLU",
    "Real Estate": "XLRE",
    "Communication Services": "XLC",
}

ETF_TO_SECTOR: dict[str, str] = {etf: sector for sector, etf in SECTOR_TO_ETF.items()}

SECTOR_ALIASES: dict[str, str] = {
    "Technology": "Information Technology",
    "Information Technology": "Information Technology",
    "Healthcare": "Health Care",
    "Health Care": "Health Care",
    "Financial": "Financials",
    "Financials": "Financials",
    "Financial Services": "Financials",
    "Consumer Cyclical": "Consumer Discretionary",
    "Consumer Disc.": "Consumer Discretionary",
    "Consumer Discretionary": "Consumer Discretionary",
    "Consumer Defensive": "Consumer Staples",
    "Consumer Staples": "Consumer Staples",
    "Basic Materials": "Materials",
    "Materials": "Materials",
    "Industrials": "Industrials",
    "Industrial Goods": "Industrials",
    "Communication Services": "Communication Services",
    "Communication Svc": "Communication Services",
    "Telecommunication Services": "Communication Services",
    "Utilities": "Utilities",
    "Energy": "Energy",
    "Real Estate": "Real Estate",
}

LEGACY_SYMBOL_TO_SECTOR_ETF: dict[str, str] = {
    "AAPL": "XLK", "MSFT": "XLK", "NVDA": "XLK", "AMD": "XLK", "INTC": "XLK",
    "QCOM": "XLK", "TXN": "XLK", "AVGO": "XLK", "CRM": "XLK", "ORCL": "XLK",
    "ACN": "XLK", "IBM": "XLK", "MU": "XLK", "AMAT": "XLK", "LRCX": "XLK",
    "PANW": "XLK", "FTNT": "XLK", "MRVL": "XLK", "NOW": "XLK", "ADBE": "XLK",
    "GOOGL": "XLC", "GOOG": "XLC", "META": "XLC", "NFLX": "XLC", "DIS": "XLC",
    "CMCSA": "XLC", "VZ": "XLC", "T": "XLC", "TMUS": "XLC", "EA": "XLC",
    "WBD": "XLC", "PARA": "XLC",
    "AMZN": "XLY", "TSLA": "XLY", "NKE": "XLY", "HD": "XLY", "MCD": "XLY",
    "SBUX": "XLY", "LOW": "XLY", "TGT": "XLY", "BKNG": "XLY", "ABNB": "XLY",
    "GM": "XLY", "F": "XLY", "RIVN": "XLY", "TJX": "XLY", "EBAY": "XLY",
    "JPM": "XLF", "BAC": "XLF", "WFC": "XLF", "GS": "XLF", "MS": "XLF",
    "C": "XLF", "USB": "XLF", "AXP": "XLF", "BLK": "XLF", "SCHW": "XLF",
    "V": "XLF", "MA": "XLF", "PYPL": "XLF", "COF": "XLF", "BX": "XLF",
    "JNJ": "XLV", "PFE": "XLV", "UNH": "XLV", "MRK": "XLV", "ABBV": "XLV",
    "TMO": "XLV", "ABT": "XLV", "DHR": "XLV", "BMY": "XLV", "AMGN": "XLV",
    "GILD": "XLV", "CVS": "XLV", "ISRG": "XLV", "MDT": "XLV", "SYK": "XLV",
    "REGN": "XLV", "VRTX": "XLV", "ZBH": "XLV",
    "XOM": "XLE", "CVX": "XLE", "COP": "XLE", "SLB": "XLE", "OXY": "XLE",
    "EOG": "XLE", "MPC": "XLE", "PSX": "XLE", "VLO": "XLE", "HES": "XLE",
    "CAT": "XLI", "BA": "XLI", "GE": "XLI", "MMM": "XLI", "UPS": "XLI",
    "FDX": "XLI", "HON": "XLI", "LMT": "XLI", "RTX": "XLI", "NOC": "XLI",
    "DE": "XLI", "EMR": "XLI", "ETN": "XLI", "PH": "XLI", "CARR": "XLI",
    "PG": "XLP", "KO": "XLP", "PEP": "XLP", "WMT": "XLP", "COST": "XLP",
    "MDLZ": "XLP", "PM": "XLP", "MO": "XLP", "CL": "XLP", "KMB": "XLP",
    "EL": "XLP", "GIS": "XLP",
    "NEE": "XLU", "DUK": "XLU", "SO": "XLU", "D": "XLU", "AEP": "XLU",
    "EXC": "XLU", "SRE": "XLU", "XEL": "XLU", "ED": "XLU",
    "AMT": "XLRE", "PLD": "XLRE", "EQIX": "XLRE", "SPG": "XLRE", "PSA": "XLRE",
    "O": "XLRE", "WELL": "XLRE", "DLR": "XLRE", "CCI": "XLRE",
    "LIN": "XLB", "APD": "XLB", "FCX": "XLB", "NEM": "XLB", "DD": "XLB",
    "PPG": "XLB", "ECL": "XLB", "VMC": "XLB",
}

DEFAULT_HIERARCHY_BY_SECTOR: dict[str, tuple[str, str, str]] = {
    "Information Technology": ("Software & Services", "Technology", "Unclassified Technology"),
    "Health Care": ("Health Care Equipment & Services", "Health Care Services", "Unclassified Health Care"),
    "Financials": ("Financial Services", "Financial Services", "Unclassified Financial Services"),
    "Consumer Discretionary": ("Retailing", "Consumer Discretionary", "Unclassified Consumer Discretionary"),
    "Consumer Staples": ("Food, Beverage & Tobacco", "Consumer Staples", "Unclassified Consumer Staples"),
    "Energy": ("Energy", "Oil, Gas & Consumable Fuels", "Unclassified Energy"),
    "Industrials": ("Capital Goods", "Industrials", "Unclassified Industrials"),
    "Materials": ("Materials", "Materials", "Unclassified Materials"),
    "Utilities": ("Utilities", "Utilities", "Unclassified Utilities"),
    "Real Estate": ("Real Estate Management & Development", "Real Estate", "Unclassified Real Estate"),
    "Communication Services": ("Media & Entertainment", "Communication Services", "Unclassified Communication Services"),
}

SPECIAL_CLASSIFICATIONS: dict[str, dict[str, str]] = {
    "AAPL": {
        "sector": "Information Technology",
        "industry_group": "Technology Hardware & Equipment",
        "industry": "Technology Hardware, Storage & Peripherals",
        "sub_industry": "Consumer Electronics",
    },
    "MSFT": {
        "sector": "Information Technology",
        "industry_group": "Software & Services",
        "industry": "Software",
        "sub_industry": "Systems & Productivity Software",
    },
    "NVDA": {
        "sector": "Information Technology",
        "industry_group": "Semiconductors & Semiconductor Equipment",
        "industry": "Semiconductors",
        "sub_industry": "GPU Designers",
    },
    "AMD": {
        "sector": "Information Technology",
        "industry_group": "Semiconductors & Semiconductor Equipment",
        "industry": "Semiconductors",
        "sub_industry": "GPU Designers",
    },
    "INTC": {
        "sector": "Information Technology",
        "industry_group": "Semiconductors & Semiconductor Equipment",
        "industry": "Semiconductors",
        "sub_industry": "Integrated Device Manufacturers",
    },
    "ORCL": {
        "sector": "Information Technology",
        "industry_group": "Software & Services",
        "industry": "Software",
        "sub_industry": "Database & Enterprise Software",
    },
    "CRM": {
        "sector": "Information Technology",
        "industry_group": "Software & Services",
        "industry": "Software",
        "sub_industry": "Enterprise SaaS",
    },
    "ADBE": {
        "sector": "Information Technology",
        "industry_group": "Software & Services",
        "industry": "Software",
        "sub_industry": "Creative & Document Software",
    },
    "GOOGL": {
        "sector": "Communication Services",
        "industry_group": "Media & Entertainment",
        "industry": "Interactive Media & Services",
        "sub_industry": "Search & Digital Advertising",
    },
    "GOOG": {
        "sector": "Communication Services",
        "industry_group": "Media & Entertainment",
        "industry": "Interactive Media & Services",
        "sub_industry": "Search & Digital Advertising",
    },
    "META": {
        "sector": "Communication Services",
        "industry_group": "Media & Entertainment",
        "industry": "Interactive Media & Services",
        "sub_industry": "Social Networks & Digital Advertising",
    },
    "NFLX": {
        "sector": "Communication Services",
        "industry_group": "Media & Entertainment",
        "industry": "Entertainment",
        "sub_industry": "Streaming Platforms",
    },
    "DIS": {
        "sector": "Communication Services",
        "industry_group": "Media & Entertainment",
        "industry": "Entertainment",
        "sub_industry": "Diversified Media & Streaming",
    },
    "AMZN": {
        "sector": "Consumer Discretionary",
        "industry_group": "Retailing",
        "industry": "Broadline Retail",
        "sub_industry": "E-Commerce Platforms",
    },
    "TSLA": {
        "sector": "Consumer Discretionary",
        "industry_group": "Automobiles & Components",
        "industry": "Automobiles",
        "sub_industry": "Electric Vehicles",
    },
    "HD": {
        "sector": "Consumer Discretionary",
        "industry_group": "Retailing",
        "industry": "Specialty Retail",
        "sub_industry": "Home Improvement Retail",
    },
    "MCD": {
        "sector": "Consumer Discretionary",
        "industry_group": "Consumer Services",
        "industry": "Hotels, Restaurants & Leisure",
        "sub_industry": "Quick Service Restaurants",
    },
    "JPM": {
        "sector": "Financials",
        "industry_group": "Banks",
        "industry": "Banks",
        "sub_industry": "Money Center Banks",
    },
    "BAC": {
        "sector": "Financials",
        "industry_group": "Banks",
        "industry": "Banks",
        "sub_industry": "Money Center Banks",
    },
    "GS": {
        "sector": "Financials",
        "industry_group": "Capital Markets",
        "industry": "Capital Markets",
        "sub_industry": "Investment Banking & Brokerage",
    },
    "MS": {
        "sector": "Financials",
        "industry_group": "Capital Markets",
        "industry": "Capital Markets",
        "sub_industry": "Investment Banking & Brokerage",
    },
    "BLK": {
        "sector": "Financials",
        "industry_group": "Capital Markets",
        "industry": "Capital Markets",
        "sub_industry": "Asset Management & Custody Banks",
    },
    "V": {
        "sector": "Financials",
        "industry_group": "Financial Services",
        "industry": "Transaction & Payment Processing Services",
        "sub_industry": "Card Networks",
    },
    "MA": {
        "sector": "Financials",
        "industry_group": "Financial Services",
        "industry": "Transaction & Payment Processing Services",
        "sub_industry": "Card Networks",
    },
    "PYPL": {
        "sector": "Financials",
        "industry_group": "Financial Services",
        "industry": "Transaction & Payment Processing Services",
        "sub_industry": "Digital Wallets & Payments",
    },
    "JNJ": {
        "sector": "Health Care",
        "industry_group": "Pharmaceuticals, Biotechnology & Life Sciences",
        "industry": "Pharmaceuticals",
        "sub_industry": "Diversified Pharmaceuticals",
    },
    "PFE": {
        "sector": "Health Care",
        "industry_group": "Pharmaceuticals, Biotechnology & Life Sciences",
        "industry": "Pharmaceuticals",
        "sub_industry": "Drug Manufacturers",
    },
    "UNH": {
        "sector": "Health Care",
        "industry_group": "Health Care Equipment & Services",
        "industry": "Health Care Providers & Services",
        "sub_industry": "Managed Care",
    },
    "PG": {
        "sector": "Consumer Staples",
        "industry_group": "Household & Personal Products",
        "industry": "Household Products",
        "sub_industry": "Home Care Products",
    },
    "KO": {
        "sector": "Consumer Staples",
        "industry_group": "Food, Beverage & Tobacco",
        "industry": "Beverages",
        "sub_industry": "Soft Drinks & Non-alcoholic Beverages",
    },
    "WMT": {
        "sector": "Consumer Staples",
        "industry_group": "Consumer Staples Distribution & Retail",
        "industry": "Consumer Staples Merchandise Retail",
        "sub_industry": "Food & Mass Merchandise Retail",
    },
    "XOM": {
        "sector": "Energy",
        "industry_group": "Energy",
        "industry": "Oil, Gas & Consumable Fuels",
        "sub_industry": "Integrated Oil & Gas",
    },
    "CVX": {
        "sector": "Energy",
        "industry_group": "Energy",
        "industry": "Oil, Gas & Consumable Fuels",
        "sub_industry": "Integrated Oil & Gas",
    },
    "BA": {
        "sector": "Industrials",
        "industry_group": "Capital Goods",
        "industry": "Aerospace & Defense",
        "sub_industry": "Commercial Aerospace & Defense",
    },
    "HON": {
        "sector": "Industrials",
        "industry_group": "Capital Goods",
        "industry": "Industrial Conglomerates",
        "sub_industry": "Diversified Industrials",
    },
    "CAT": {
        "sector": "Industrials",
        "industry_group": "Capital Goods",
        "industry": "Machinery",
        "sub_industry": "Construction & Farm Machinery",
    },
    "LIN": {
        "sector": "Materials",
        "industry_group": "Materials",
        "industry": "Chemicals",
        "sub_industry": "Industrial Gases",
    },
    "NEE": {
        "sector": "Utilities",
        "industry_group": "Utilities",
        "industry": "Electric Utilities",
        "sub_industry": "Regulated & Renewable Utilities",
    },
    "AMT": {
        "sector": "Real Estate",
        "industry_group": "Equity Real Estate Investment Trusts (REITs)",
        "industry": "Specialized REITs",
        "sub_industry": "Telecom Tower REITs",
    },
    "PLD": {
        "sector": "Real Estate",
        "industry_group": "Equity Real Estate Investment Trusts (REITs)",
        "industry": "Industrial REITs",
        "sub_industry": "Logistics REITs",
    },
    "EQIX": {
        "sector": "Real Estate",
        "industry_group": "Equity Real Estate Investment Trusts (REITs)",
        "industry": "Specialized REITs",
        "sub_industry": "Data Center REITs",
    },
}

_CLASSIFICATION_CACHE: dict[tuple[str, str], "AssetClassification"] = {}
_PROFILE_CACHE: dict[str, dict[str, str]] = {}


@dataclass(frozen=True)
class AssetClassification:
    ticker: str
    asset_type: str
    sector: str
    sector_etf: str
    industry_group: str
    industry: str
    sub_industry: str
    company_name: str = ""
    source: str = "fallback"

    def to_payload(self) -> dict[str, Any]:
        return {
            "ticker": self.ticker,
            "asset_type": self.asset_type,
            "sector": self.sector,
            "sector_etf": self.sector_etf,
            "industry_group": self.industry_group,
            "industry": self.industry,
            "sub_industry": self.sub_industry,
            "company_name": self.company_name,
            "source": self.source,
        }


def _classification_from_payload(payload: dict[str, Any]) -> AssetClassification:
    return AssetClassification(
        ticker=payload["ticker"],
        asset_type=payload.get("asset_type", "equity"),
        sector=payload.get("sector", "Unclassified"),
        sector_etf=payload.get("sector_etf", "SPY"),
        industry_group=payload.get("industry_group", "Unclassified"),
        industry=payload.get("industry", "Unclassified"),
        sub_industry=payload.get("sub_industry", "Unclassified"),
        company_name=payload.get("company_name", ""),
        source=payload.get("source", "database"),
    )


def _load_db_classification(symbol: str, benchmark: str) -> dict[str, Any] | None:
    from ..core.container import duckdb_repo

    return duckdb_repo.get_asset_classification(symbol, benchmark=benchmark)


def _persist_db_classifications(classifications: list[dict[str, Any]], benchmark: str) -> None:
    from ..core.container import duckdb_repo

    duckdb_repo.upsert_asset_classifications(classifications, benchmark=benchmark)


def sector_name_for_etf(etf: str, benchmark: str = "SPY") -> str:
    normalized = etf.upper().strip()
    if normalized == benchmark.upper():
        return "Market (S&P 500)" if normalized == "SPY" else normalized
    return ETF_TO_SECTOR.get(normalized, normalized)


def _sector_etf_for_sector(sector: str, benchmark: str) -> str:
    return SECTOR_TO_ETF.get(sector, benchmark.upper())


def _normalize_sector(raw_sector: str) -> str:
    normalized = " ".join(str(raw_sector or "").replace("&", " and ").split()).strip()
    return SECTOR_ALIASES.get(normalized, normalized)


def _normalize_label(raw_value: str) -> str:
    value = " ".join(str(raw_value or "").replace("/", " / ").split()).strip()
    if not value:
        return ""

    words: list[str] = []
    for word in value.split(" "):
        upper = word.upper()
        if upper in {"IT", "GPU", "REIT", "REITS", "FX", "CRM", "AI", "SaaS".upper()}:
            words.append(upper if upper != "SAAS" else "SaaS")
            continue
        if word in {"&", "/"}:
            words.append(word)
            continue
        words.append(word.capitalize() if word.islower() else word)
    return " ".join(words)


def _detect_asset_type(symbol: str) -> str:
    normalized = symbol.upper().strip()
    compact = normalized.replace("/", "")
    if normalized in ETF_TO_SECTOR or normalized in {"SPY", "QQQ", "IWM", "RSP", "TLT", "GLD", "SLV", "USO", "UNG", "TAN", "RSPT"}:
        return "etf"
    if normalized.startswith("^"):
        return "index"
    if normalized.endswith("-USD"):
        return "crypto"
    if normalized.endswith("=X"):
        return "forex"
    if "/" in normalized and len(compact) == 6 and compact.isalpha():
        return "forex"
    return "equity"


def _build_non_equity_classification(symbol: str, benchmark: str) -> AssetClassification:
    asset_type = _detect_asset_type(symbol)
    if asset_type == "etf":
        sector = sector_name_for_etf(symbol, benchmark) if symbol in ETF_TO_SECTOR else "Broad Market ETF"
        sector_etf = symbol if symbol in ETF_TO_SECTOR else benchmark.upper()
        industry_group = "Sector Funds" if symbol in ETF_TO_SECTOR else "Index Funds"
        sub_industry = f"{sector} ETF" if symbol in ETF_TO_SECTOR else "Broad Market ETF"
        return AssetClassification(
            ticker=symbol,
            asset_type=asset_type,
            sector=sector,
            sector_etf=sector_etf,
            industry_group=industry_group,
            industry="Exchange Traded Fund",
            sub_industry=sub_industry,
            source="instrument-rule",
        )

    if asset_type == "forex":
        return AssetClassification(
            ticker=symbol,
            asset_type=asset_type,
            sector="Foreign Exchange",
            sector_etf=benchmark.upper(),
            industry_group="Currencies",
            industry="FX Spot",
            sub_industry="Major FX Pair",
            source="instrument-rule",
        )

    if asset_type == "crypto":
        return AssetClassification(
            ticker=symbol,
            asset_type=asset_type,
            sector="Digital Assets",
            sector_etf=benchmark.upper(),
            industry_group="Cryptoassets",
            industry="Blockchain Networks",
            sub_industry="Token",
            source="instrument-rule",
        )

    return AssetClassification(
        ticker=symbol,
        asset_type=asset_type,
        sector="Market Indexes",
        sector_etf=benchmark.upper(),
        industry_group="Indexes",
        industry="Equity Index",
        sub_industry="Benchmark Index",
        source="instrument-rule",
    )


def _classification_from_override(symbol: str, benchmark: str) -> AssetClassification | None:
    override = SPECIAL_CLASSIFICATIONS.get(symbol)
    if not override:
        return None
    sector = override["sector"]
    return AssetClassification(
        ticker=symbol,
        asset_type="equity",
        sector=sector,
        sector_etf=_sector_etf_for_sector(sector, benchmark),
        industry_group=override["industry_group"],
        industry=override["industry"],
        sub_industry=override["sub_industry"],
        source="override",
    )


async def _fetch_profile(symbol: str) -> dict[str, str]:
    if symbol in _PROFILE_CACHE:
        return _PROFILE_CACHE[symbol]

    profile_payload: dict[str, str] = {}

    try:
        profile = await fmp_service.get_profile(symbol)
        sector = str(profile.get("sector") or "").strip()
        industry = str(profile.get("industry") or "").strip()
        company_name = str(profile.get("companyName") or profile.get("name") or "").strip()
        if sector or industry or company_name:
            profile_payload = {
                "sector": sector,
                "industry": industry,
                "company_name": company_name,
                "source": "fmp",
            }
    except Exception:
        profile_payload = {}

    if not profile_payload:
        def _load_yahoo_profile() -> dict[str, str]:
            import yfinance as yf

            info = yf.Ticker(symbol).info or {}
            return {
                "sector": str(info.get("sectorDisp") or info.get("sector") or "").strip(),
                "industry": str(info.get("industryDisp") or info.get("industry") or "").strip(),
                "company_name": str(info.get("shortName") or info.get("longName") or "").strip(),
                "source": "yfinance",
            }

        try:
            yahoo_profile = await asyncio.wait_for(asyncio.to_thread(_load_yahoo_profile), timeout=5.0)
            if yahoo_profile.get("sector") or yahoo_profile.get("industry") or yahoo_profile.get("company_name"):
                profile_payload = yahoo_profile
        except Exception:
            profile_payload = {}

    _PROFILE_CACHE[symbol] = profile_payload
    return profile_payload


def _infer_it_sub_industry(symbol: str, industry_text: str) -> tuple[str, str, str]:
    if "semiconductor" in industry_text or "chip" in industry_text:
        if symbol in {"NVDA", "AMD"}:
            sub_industry = "GPU Designers"
        elif symbol == "INTC":
            sub_industry = "Integrated Device Manufacturers"
        elif symbol in {"AVGO", "QCOM", "MRVL"}:
            sub_industry = "Fabless Semiconductors"
        else:
            sub_industry = "Semiconductor Manufacturing"
        return ("Semiconductors & Semiconductor Equipment", "Semiconductors", sub_industry)

    if any(keyword in industry_text for keyword in ("it services", "information technology services", "consulting", "outsourcing")):
        return ("Software & Services", "IT Services", "IT Consulting & Services")

    if any(keyword in industry_text for keyword in ("communication equipment", "networking", "network")):
        return ("Technology Hardware & Equipment", "Communications Equipment", "Networking & Communications Equipment")

    if any(keyword in industry_text for keyword in ("hardware", "computer", "consumer electronics", "peripheral", "storage")):
        return ("Technology Hardware & Equipment", "Technology Hardware, Storage & Peripherals", "Hardware & Devices")

    if any(keyword in industry_text for keyword in ("software", "application", "saas", "systems")):
        if symbol == "MSFT":
            sub_industry = "Systems & Productivity Software"
        elif symbol == "CRM":
            sub_industry = "Enterprise SaaS"
        elif symbol == "ADBE":
            sub_industry = "Creative & Document Software"
        else:
            sub_industry = "Software Applications"
        return ("Software & Services", "Software", sub_industry)

    return DEFAULT_HIERARCHY_BY_SECTOR["Information Technology"]


def _infer_health_care_sub_industry(symbol: str, industry_text: str) -> tuple[str, str, str]:
    if "biotech" in industry_text:
        return ("Pharmaceuticals, Biotechnology & Life Sciences", "Biotechnology", "Biotechnology")

    if any(keyword in industry_text for keyword in ("pharmaceutical", "drug manufacturer", "drug", "pharma")) or symbol in {"JNJ", "PFE", "MRK", "ABBV", "BMY"}:
        sub_industry = "Diversified Pharmaceuticals" if symbol in {"JNJ", "MRK", "ABBV"} else "Drug Manufacturers"
        return ("Pharmaceuticals, Biotechnology & Life Sciences", "Pharmaceuticals", sub_industry)

    if any(keyword in industry_text for keyword in ("medical device", "medical instruments", "diagnostic", "equipment", "devices")) or symbol in {"ISRG", "MDT", "SYK", "TMO", "DHR", "ABT"}:
        return ("Health Care Equipment & Services", "Health Care Equipment", "Medical Devices & Diagnostics")

    if any(keyword in industry_text for keyword in ("health care plan", "managed care", "hospital", "providers", "services")) or symbol in {"UNH", "CVS"}:
        sub_industry = "Managed Care" if symbol == "UNH" else "Health Care Services"
        return ("Health Care Equipment & Services", "Health Care Providers & Services", sub_industry)

    return DEFAULT_HIERARCHY_BY_SECTOR["Health Care"]


def _infer_financial_sub_industry(symbol: str, industry_text: str) -> tuple[str, str, str]:
    if any(keyword in industry_text for keyword in ("insurance", "insurer")):
        return ("Insurance", "Insurance", "Multi-line Insurance")

    if any(keyword in industry_text for keyword in ("bank", "banks", "regional bank")) or symbol in {"JPM", "BAC", "WFC", "C", "USB"}:
        sub_industry = "Regional & Diversified Banks" if symbol in {"USB", "WFC"} else "Money Center Banks"
        return ("Banks", "Banks", sub_industry)

    if any(keyword in industry_text for keyword in ("asset management", "capital markets", "brokerage", "investment")) or symbol in {"GS", "MS", "BLK", "SCHW", "BX"}:
        if symbol == "BLK":
            sub_industry = "Asset Management & Custody Banks"
        else:
            sub_industry = "Investment Banking & Brokerage"
        return ("Capital Markets", "Capital Markets", sub_industry)

    if any(keyword in industry_text for keyword in ("credit services", "payment", "transaction", "fintech")) or symbol in {"V", "MA", "PYPL", "AXP", "COF"}:
        if symbol == "PYPL":
            sub_industry = "Digital Wallets & Payments"
        else:
            sub_industry = "Card Networks"
        return ("Financial Services", "Transaction & Payment Processing Services", sub_industry)

    return DEFAULT_HIERARCHY_BY_SECTOR["Financials"]


def _infer_consumer_discretionary_sub_industry(symbol: str, industry_text: str) -> tuple[str, str, str]:
    if any(keyword in industry_text for keyword in ("auto", "automobile", "vehicle")) or symbol in {"TSLA", "GM", "F", "RIVN"}:
        sub_industry = "Electric Vehicles" if symbol in {"TSLA", "RIVN"} else "Automotive Manufacturers"
        return ("Automobiles & Components", "Automobiles", sub_industry)

    if any(keyword in industry_text for keyword in ("restaurant", "hotel", "travel", "leisure", "lodging")) or symbol in {"MCD", "SBUX", "BKNG", "ABNB"}:
        if symbol == "MCD":
            sub_industry = "Quick Service Restaurants"
        elif symbol in {"BKNG", "ABNB"}:
            sub_industry = "Online Travel & Lodging Platforms"
        else:
            sub_industry = "Restaurants"
        return ("Consumer Services", "Hotels, Restaurants & Leisure", sub_industry)

    if any(keyword in industry_text for keyword in ("retail", "e-commerce", "internet retail", "home improvement")) or symbol in {"AMZN", "HD", "LOW", "TJX", "EBAY", "TGT"}:
        if symbol == "AMZN":
            sub_industry = "E-Commerce Platforms"
        elif symbol in {"HD", "LOW"}:
            sub_industry = "Home Improvement Retail"
        else:
            sub_industry = "Specialty & Broadline Retail"
        return ("Retailing", "Broadline Retail", sub_industry)

    return DEFAULT_HIERARCHY_BY_SECTOR["Consumer Discretionary"]


def _infer_consumer_staples_sub_industry(symbol: str, industry_text: str) -> tuple[str, str, str]:
    if any(keyword in industry_text for keyword in ("beverage", "drink", "soft")) or symbol in {"KO", "PEP"}:
        return ("Food, Beverage & Tobacco", "Beverages", "Soft Drinks & Non-alcoholic Beverages")

    if any(keyword in industry_text for keyword in ("tobacco", "smoke")) or symbol in {"PM", "MO"}:
        return ("Food, Beverage & Tobacco", "Tobacco", "Tobacco Products")

    if any(keyword in industry_text for keyword in ("household", "personal", "cosmetic", "home care")) or symbol in {"PG", "CL", "KMB", "EL"}:
        return ("Household & Personal Products", "Household Products", "Home & Personal Care Products")

    if any(keyword in industry_text for keyword in ("retail", "discount", "warehouse")) or symbol in {"WMT", "COST"}:
        return ("Consumer Staples Distribution & Retail", "Consumer Staples Merchandise Retail", "Food & Mass Merchandise Retail")

    return DEFAULT_HIERARCHY_BY_SECTOR["Consumer Staples"]


def _infer_energy_sub_industry(symbol: str, industry_text: str) -> tuple[str, str, str]:
    if any(keyword in industry_text for keyword in ("integrated", "major")) or symbol in {"XOM", "CVX"}:
        return ("Energy", "Oil, Gas & Consumable Fuels", "Integrated Oil & Gas")

    if any(keyword in industry_text for keyword in ("equipment", "services")) or symbol == "SLB":
        return ("Energy", "Energy Equipment & Services", "Oil & Gas Equipment & Services")

    if any(keyword in industry_text for keyword in ("refining", "marketing", "downstream")) or symbol in {"MPC", "PSX", "VLO"}:
        return ("Energy", "Oil, Gas & Consumable Fuels", "Refining & Marketing")

    return ("Energy", "Oil, Gas & Consumable Fuels", "Exploration & Production")


def _infer_industrials_sub_industry(symbol: str, industry_text: str) -> tuple[str, str, str]:
    if any(keyword in industry_text for keyword in ("aerospace", "defense")) or symbol in {"BA", "LMT", "RTX", "NOC"}:
        sub_industry = "Commercial Aerospace & Defense" if symbol == "BA" else "Defense Primes"
        return ("Capital Goods", "Aerospace & Defense", sub_industry)

    if any(keyword in industry_text for keyword in ("logistics", "air freight", "delivery", "transport")) or symbol in {"UPS", "FDX"}:
        return ("Transportation", "Air Freight & Logistics", "Logistics & Parcel Delivery")

    if any(keyword in industry_text for keyword in ("machinery", "industrial", "electrical", "building")) or symbol in {"CAT", "DE", "ETN", "PH", "CARR", "GE", "HON", "EMR"}:
        if symbol in {"CAT", "DE"}:
            sub_industry = "Construction & Farm Machinery"
        elif symbol == "HON":
            sub_industry = "Diversified Industrials"
        else:
            sub_industry = "Industrial Equipment"
        return ("Capital Goods", "Machinery", sub_industry)

    return DEFAULT_HIERARCHY_BY_SECTOR["Industrials"]


def _infer_materials_sub_industry(symbol: str, industry_text: str) -> tuple[str, str, str]:
    if any(keyword in industry_text for keyword in ("chemical", "chemicals")) or symbol in {"LIN", "APD", "DD", "ECL", "PPG"}:
        sub_industry = "Industrial Gases" if symbol in {"LIN", "APD"} else "Specialty Chemicals"
        return ("Materials", "Chemicals", sub_industry)

    if any(keyword in industry_text for keyword in ("gold", "metal", "mining", "copper")) or symbol in {"FCX", "NEM"}:
        return ("Materials", "Metals & Mining", "Metals & Mining")

    if any(keyword in industry_text for keyword in ("construction", "building")) or symbol == "VMC":
        return ("Materials", "Construction Materials", "Building Materials")

    return DEFAULT_HIERARCHY_BY_SECTOR["Materials"]


def _infer_utilities_sub_industry(symbol: str, industry_text: str) -> tuple[str, str, str]:
    if any(keyword in industry_text for keyword in ("renewable", "clean")) or symbol == "NEE":
        return ("Utilities", "Electric Utilities", "Regulated & Renewable Utilities")

    if any(keyword in industry_text for keyword in ("gas", "water")):
        return ("Utilities", "Multi-Utilities", "Gas & Water Utilities")

    return ("Utilities", "Electric Utilities", "Regulated Utilities")


def _infer_real_estate_sub_industry(symbol: str, industry_text: str) -> tuple[str, str, str]:
    if symbol in {"AMT", "CCI"}:
        return ("Equity Real Estate Investment Trusts (REITs)", "Specialized REITs", "Telecom Tower REITs")

    if symbol in {"EQIX", "DLR"}:
        return ("Equity Real Estate Investment Trusts (REITs)", "Specialized REITs", "Data Center REITs")

    if symbol == "PLD":
        return ("Equity Real Estate Investment Trusts (REITs)", "Industrial REITs", "Logistics REITs")

    if symbol == "SPG":
        return ("Equity Real Estate Investment Trusts (REITs)", "Retail REITs", "Mall REITs")

    if symbol == "PSA":
        return ("Equity Real Estate Investment Trusts (REITs)", "Specialized REITs", "Self-Storage REITs")

    if symbol == "WELL":
        return ("Equity Real Estate Investment Trusts (REITs)", "Health Care REITs", "Health Care REITs")

    return ("Real Estate Management & Development", "Real Estate", "Commercial & Residential Properties")


def _infer_communication_sub_industry(symbol: str, industry_text: str) -> tuple[str, str, str]:
    if any(keyword in industry_text for keyword in ("telecom", "wireless", "telecommunications")) or symbol in {"VZ", "T", "TMUS"}:
        return ("Telecommunication Services", "Diversified Telecommunication Services", "Wireless & Integrated Telecom")

    if any(keyword in industry_text for keyword in ("interactive media", "social media", "internet content", "advertising")) or symbol in {"GOOGL", "GOOG", "META"}:
        if symbol in {"GOOGL", "GOOG"}:
            sub_industry = "Search & Digital Advertising"
        else:
            sub_industry = "Social Networks & Digital Advertising"
        return ("Media & Entertainment", "Interactive Media & Services", sub_industry)

    if any(keyword in industry_text for keyword in ("entertainment", "streaming", "broadcast", "cable", "media")) or symbol in {"NFLX", "DIS", "CMCSA", "WBD", "PARA"}:
        if symbol == "NFLX":
            sub_industry = "Streaming Platforms"
        elif symbol == "DIS":
            sub_industry = "Diversified Media & Streaming"
        else:
            sub_industry = "Broadcasting & Media"
        return ("Media & Entertainment", "Entertainment", sub_industry)

    return DEFAULT_HIERARCHY_BY_SECTOR["Communication Services"]


def _infer_equity_hierarchy(symbol: str, sector: str, raw_industry: str) -> tuple[str, str, str]:
    industry_text = str(raw_industry or "").strip().lower()
    if sector == "Information Technology":
        return _infer_it_sub_industry(symbol, industry_text)
    if sector == "Health Care":
        return _infer_health_care_sub_industry(symbol, industry_text)
    if sector == "Financials":
        return _infer_financial_sub_industry(symbol, industry_text)
    if sector == "Consumer Discretionary":
        return _infer_consumer_discretionary_sub_industry(symbol, industry_text)
    if sector == "Consumer Staples":
        return _infer_consumer_staples_sub_industry(symbol, industry_text)
    if sector == "Energy":
        return _infer_energy_sub_industry(symbol, industry_text)
    if sector == "Industrials":
        return _infer_industrials_sub_industry(symbol, industry_text)
    if sector == "Materials":
        return _infer_materials_sub_industry(symbol, industry_text)
    if sector == "Utilities":
        return _infer_utilities_sub_industry(symbol, industry_text)
    if sector == "Real Estate":
        return _infer_real_estate_sub_industry(symbol, industry_text)
    if sector == "Communication Services":
        return _infer_communication_sub_industry(symbol, industry_text)
    return DEFAULT_HIERARCHY_BY_SECTOR.get(sector, ("Unclassified", _normalize_label(raw_industry) or "Unclassified", "Unclassified"))


def _fallback_sector_from_legacy(symbol: str) -> str:
    legacy_etf = LEGACY_SYMBOL_TO_SECTOR_ETF.get(symbol)
    return ETF_TO_SECTOR.get(legacy_etf, "")


async def get_asset_classification(symbol: str, benchmark: str = "SPY") -> dict[str, Any]:
    normalized_symbol = symbol.upper().strip()
    cache_key = (normalized_symbol, benchmark.upper())
    cached = _CLASSIFICATION_CACHE.get(cache_key)
    if cached:
        return cached.to_payload()

    cached_db = _load_db_classification(normalized_symbol, benchmark.upper())
    if cached_db:
        classification = _classification_from_payload(cached_db)
        _CLASSIFICATION_CACHE[cache_key] = classification
        return classification.to_payload()

    benchmark_symbol = benchmark.upper()
    asset_type = _detect_asset_type(normalized_symbol)
    if asset_type != "equity":
        classification = _build_non_equity_classification(normalized_symbol, benchmark_symbol)
        _CLASSIFICATION_CACHE[cache_key] = classification
        payload = classification.to_payload()
        _persist_db_classifications([payload], benchmark_symbol)
        return payload

    override = _classification_from_override(normalized_symbol, benchmark_symbol)
    if override:
        _CLASSIFICATION_CACHE[cache_key] = override
        payload = override.to_payload()
        _persist_db_classifications([payload], benchmark_symbol)
        return payload

    profile = await _fetch_profile(normalized_symbol)
    sector = _normalize_sector(profile.get("sector", "")) or _fallback_sector_from_legacy(normalized_symbol)
    if not sector:
        sector = "Unclassified"

    industry_group, industry, sub_industry = _infer_equity_hierarchy(normalized_symbol, sector, profile.get("industry", ""))
    if sector == "Unclassified":
        industry_group = "Unclassified"
        industry = _normalize_label(profile.get("industry", "")) or "Unclassified"
        sub_industry = "Unclassified"

    classification = AssetClassification(
        ticker=normalized_symbol,
        asset_type=asset_type,
        sector=sector,
        sector_etf=_sector_etf_for_sector(sector, benchmark_symbol),
        industry_group=_normalize_label(industry_group) or "Unclassified",
        industry=_normalize_label(industry) or "Unclassified",
        sub_industry=_normalize_label(sub_industry) or "Unclassified",
        company_name=profile.get("company_name", ""),
        source=profile.get("source", "legacy-map" if sector != "Unclassified" else "fallback"),
    )
    _CLASSIFICATION_CACHE[cache_key] = classification
    payload = classification.to_payload()
    _persist_db_classifications([payload], benchmark_symbol)
    return payload


async def classify_assets(symbols: list[str], benchmark: str = "SPY") -> dict[str, dict[str, Any]]:
    unique_symbols: list[str] = []
    seen: set[str] = set()
    for symbol in symbols:
        normalized = symbol.upper().strip()
        if normalized and normalized not in seen:
            seen.add(normalized)
            unique_symbols.append(normalized)

    classifications = await asyncio.gather(*(get_asset_classification(symbol, benchmark=benchmark) for symbol in unique_symbols))
    _persist_db_classifications(classifications, benchmark.upper())
    return {classification["ticker"]: classification for classification in classifications}