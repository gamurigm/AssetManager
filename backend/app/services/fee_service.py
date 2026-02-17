from typing import Dict, Any
from ..models.models import Portfolio

class FeeService:
    @staticmethod
    def calculate_management_fee(portfolio: Portfolio, current_aum: float) -> float:
        """
        Calculates the management fee based on the annual rate and current AUM.
        Usually calculated daily or monthly and charged periodically.
        For simplicity, returns the periodic amount assuming a monthly calculation.
        """
        monthly_rate = portfolio.management_fee_rate / 12
        return current_aum * monthly_rate

    @staticmethod
    def calculate_performance_fee(portfolio: Portfolio, current_aum: float) -> Dict[str, Any]:
        """
        Calculates performance fee using High-Water Mark (HWM) logic.
        Fee is only charged if current_aum > high_water_mark.
        """
        if current_aum > portfolio.high_water_mark:
            profit_above_hwm = current_aum - portfolio.high_water_mark
            fee_amount = profit_above_hwm * portfolio.performance_fee_rate
            return {
                "fee_charged": True,
                "fee_amount": fee_amount,
                "profit_recognized": profit_above_hwm,
                "new_hwm_candidate": current_aum - fee_amount
            }
        
        return {
            "fee_charged": False,
            "fee_amount": 0.0,
            "profit_recognized": 0.0,
            "new_hwm_candidate": portfolio.high_water_mark
        }

    @staticmethod
    def update_high_water_mark(portfolio: Portfolio, current_aum: float, session: Any):
        """
        Updates the HWM if the current AUM reaches a new peak.
        This usually happens at the end of a performance period.
        """
        if current_aum > portfolio.high_water_mark:
            portfolio.high_water_mark = current_aum
            session.add(portfolio)
            session.commit()
