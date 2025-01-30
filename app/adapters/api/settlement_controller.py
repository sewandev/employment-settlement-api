"""
settlement_controller.py:
Responsabilidad: Manejar solicitudes HTTP y devolver respuestas.
Relación con Hexágono: Adaptador que traduce peticiones HTTP a llamadas al core.
"""
# adapters/api/settlement_controller.py
from fastapi import APIRouter
from app.schemas import SettlementInput, SettlementOutput
from app.core.services.settlement_service import SettlementService  # Conexión con el core

router = APIRouter(tags=["Finiquitos"])
service = SettlementService()  # Inyección de dependencia

@router.post("/calculate", response_model=SettlementOutput)
def calculate_settlement(data: SettlementInput):
    # Usa el servicio del core
    result = service.calculate_settlement(
        base_salary=data.base_salary,
        start_date=data.start_date,  # Ya convertido a date por el schema
        end_date=data.end_date,
        termination_reason=data.termination_reason
    )
    return result