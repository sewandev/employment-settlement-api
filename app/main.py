from fastapi import FastAPI, Depends
from app.adapters.api.settlement_controller import router as settlement_router
from app.core.services.settlement_calculator import SettlementCalculator

app = FastAPI(title="Employment Settlement API", version="1.0.0")

# Inyectar el servicio de cálculo de liquidación
def get_settlement_service():
    return SettlementCalculator()

app.include_router(settlement_router, prefix="/api", dependencies=[Depends(get_settlement_service)])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Employment Settlement API"}