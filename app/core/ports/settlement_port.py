# core/ports/settlement_port.py
from abc import ABC, abstractmethod
from datetime import date

class SettlementPort(ABC):
    @abstractmethod
    def calculate_settlement(
        self,
        base_salary: float,
        start_date: date,
        end_date: date,
        termination_reason: str
    ) -> dict:
        pass