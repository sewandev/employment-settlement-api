from abc import ABC, abstractmethod
from datetime import date
from typing import Dict

class SettlementService(ABC):
    @abstractmethod
    def calculate_settlement(self, salary: float, start_date: date, end_date: date, termination_reason: str) -> Dict[str, float]:
        """
        Define la operación para calcular una liquidación laboral.

        Parámetros:
        - salary: Salario del empleado.
        - start_date: Fecha de inicio del empleo.
        - end_date: Fecha de finalización del empleo.
        - termination_reason: Razón de la terminación del contrato.

        Retorna:
        - Un diccionario con los componentes de la liquidación (liquidation, vacation_pay, seniority_bonus, total_settlement).
        """
        pass