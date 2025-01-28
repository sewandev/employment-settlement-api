from datetime import date
from typing import Dict
from app.core.ports.settlement_service import SettlementService

class SettlementCalculator(SettlementService):
    def calculate_settlement(self, salary: float, start_date: date, end_date: date, termination_reason: str) -> Dict[str, float]:
        days_worked = (end_date - start_date).days

        liquidation = (salary / 30) * days_worked

        vacation_days = min(days_worked // 365 * 12, 24)
        vacation_pay = (salary / 30) * vacation_days

        seniority_bonus = 0
        if termination_reason == "despido":
            seniority_bonus = (salary / 30) * (days_worked // 365 * 12)

        total_settlement = liquidation + vacation_pay + seniority_bonus

        return {
            "liquidation": liquidation,
            "vacation_pay": vacation_pay,
            "seniority_bonus": seniority_bonus,
            "total_settlement": total_settlement,
        }