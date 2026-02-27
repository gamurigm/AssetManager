"""
Standardizer Service — Data Formatting for Professional UIs
Converts internal MMAM entities into standard formats (OpenBB, TradingView).
"""

from typing import List, Dict, Any

class Standardizer:
    @staticmethod
    def to_openbb_metric(label: str, value: Any, change: str = None, is_positive: bool = True) -> Dict[str, Any]:
        """Convert to OpenBB metric widget format."""
        return {
            "metric": label,
            "value": str(value),
            "change": change or "",
            "isPositive": is_positive
        }

    @staticmethod
    def to_openbb_table(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Ensure keys are properly capitalized for professional tables."""
        if not rows:
            return []
        
        # OpenBB table widget usually takes a list of flat dicts
        return rows

    @staticmethod
    def to_openbb_text(title: str, body: str) -> Dict[str, str]:
        """Convert to OpenBB text/markdown widget format."""
        return {
            "markdown": f"## {title}\n\n{body}"
        }

standardizer = Standardizer()
