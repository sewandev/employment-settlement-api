from fastapi import APIRouter
from datetime import date
from app.core.services.settlement_calculator import SettlementCalculator
from app.schemas import SettlementInput, SettlementOutput

router = APIRouter()

@router.post("/calculate-settlement", response_model=SettlementOutput)
def calculate_settlement(data: SettlementInput):
    calculator = SettlementCalculator()
    result = calculator.calculate_settlement(
        salary=data.salary,
        start_date=data.start_date,
        end_date=data.end_date,
        termination_reason=data.termination_reason,
    )
    return result