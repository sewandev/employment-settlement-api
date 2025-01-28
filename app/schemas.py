from datetime import date
from pydantic import BaseModel

class SettlementInput(BaseModel):
    salary: float
    start_date: date
    end_date: date
    termination_reason: str

class SettlementOutput(BaseModel):
    liquidation: float
    vacation_pay: float
    seniority_bonus: float
    total_settlement: float