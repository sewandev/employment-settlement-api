# core/services/settlement_service.py
from datetime import date
from app.core.ports.settlement_port import SettlementPort

class SettlementService(SettlementPort):
    def calculate_settlement(
        self,
        base_salary: float,
        start_date: date,
        end_date: date,
        termination_reason: str
    ) -> dict:
        
        days_worked = (end_date - start_date).days
        liquidation = (base_salary / 30) * days_worked

        # Cálculos básicos (simplificados)
        return {
            "liquidation": round(liquidation, 2),
            "vacation_pay": 0.0,  # ¡Implementaremos esto luego!
            "seniority_bonus": 0.0,
            "total_settlement": round(liquidation, 2)
        }