from typing import Dict, Any
from ..models.models import Portfolio

class FeeService:
    @staticmethod
    def calculate_total_expenses(portfolio: Portfolio, current_aum: float) -> Dict[str, float]:
        """
        Calculates the comprehensive annual fund operation expenses.
        Based on the provided rates:
        - Management Fee: 2.75%
        - Service Fee: 0.75%
        - Other Expenses: 0.59%
        - Reimbursement/Waiver: (0.59%)
        - Total Net: 3.50%
        """
        # Rates (Annual)
        rates = {
            "management_fee": 0.0275,
            "service_fee": 0.0075,
            "other_expenses": 0.0059,
            "reimbursement": -0.0059
        }
        
        # Monthly calculations
        results = {}
        for key, rate in rates.items():
            results[key] = (current_aum * rate) / 12
            
        results["total_annual_gross"] = current_aum * 0.0409 / 12
        results["total_annual_net"] = current_aum * 0.0350 / 12
        
        return results

    @staticmethod
    def calculate_management_fee(portfolio: Portfolio, current_aum: float) -> float:
        """
        Legacy method for backward compatibility. 
        Calculates the management fee using the old 1% or the new 2.75% if updated.
        """
        # Using the portfolio's stored rate, but defaulting to the new 2.75% if it's 0.01
        rate = portfolio.management_fee_rate if portfolio.management_fee_rate != 0.01 else 0.0275
        monthly_rate = rate / 12
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
