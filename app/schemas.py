"""
schemas.py:
Responsabilidad: Definir cómo se estructuran los datos de entrada/salida.
Relación con Hexágono: Parte del adaptador HTTP (valida formato externo).
"""

# app/schemas.py
from datetime import date
from pydantic import BaseModel, Field, field_validator
from enum import Enum

# Enumeración para las razones de terminación (mejor que strings)
class TerminationReason(str, Enum):
    resignation = "renuncia"
    dismissal = "despido"

# Modelo de entrada (Input)
class SettlementInput(BaseModel):
    base_salary: float = Field(
        gt=0,
        default=500_000,
        examples=[500_000, 1_200_000, 2_500_000],
        min_length=6,
        title="Sueldo",
        description="Salario base mensual del empleado",
        json_schema_extra={"error_message": "El salario debe ser un número positivo"}
    )
    start_date: date = Field(
        examples=["2020-01-01"],
        description="Fecha de inicio del contrato"
    )
    end_date: date = Field(
        examples=["2023-12-31"],
        description="Fecha de terminación del contrato"
    )
    termination_reason: TerminationReason = Field(
        examples=["despido"],
        description="Razón de terminación del contrato"
    )

    # Validador personalizado para fechas
    @field_validator("end_date")
    def validate_dates(cls, end_date, values):
        if "start_date" in values.data and end_date <= values.data["start_date"]:
            raise ValueError("La fecha de término debe ser posterior a la de inicio")
        return end_date

# Modelo de salida (Output)
class SettlementOutput(BaseModel):
    liquidation: float = Field(
        examples=[5000.0],
        description="Liquidación por días trabajados"
    )
    vacation_pay: float = Field(
        examples=[1200.0],
        description="Pago de vacaciones pendientes"
    )
    seniority_bonus: float = Field(
        examples=[3000.0],
        description="Bono por antigüedad"
    )
    total_settlement: float = Field(
        examples=[9200.0],
        description="Total del finiquito"
    )