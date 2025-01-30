"""
main.py:
Responsabilidad: Inicializar FastAPI y conectar los routers.
Relación con Hexágono: Es el adaptador de entrada que inicia la aplicación.

app/
├── main.py
├── schemas.py
│
├── adapters/
│   └── api/
│       └── settlement_controller.py
│
└── core/
    ├── services/
    │   └── settlement_service.py   # Nuevo archivo
    └── ports/
        └── settlement_port.py      # Nueva interfaz
"""


# app/main.py (Versión Simplificada)
from fastapi import FastAPI

# 1. Crea la aplicación FastAPI (Adaptador de Entrada)
app = FastAPI(
    title="Employment Settlement API",
    version="1.0",
    description="API para cálculo de finiquitos laborales"
)

# 2. Importa el router del controlador (Adaptador HTTP)
from app.adapters.api.settlement_controller import router as settlement_router

# 3. Conecta el router al núcleo (Hexágono)
app.include_router(settlement_router, prefix="/api")