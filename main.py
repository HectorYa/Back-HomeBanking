"""HOMEBANKING — Backend FastAPI · Banca Internet Banco Andino.

Portal del CLIENTE. Proyecto separado del core bancario; se conecta a la base
PostgreSQL YA EXISTENTE bd_core_financiero (no crea tablas).

Desarrollo:  uvicorn main:app --reload --port 8002
Produccion:  gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT
"""
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.cfg_config import settings
from app.routes import route_auth, route_creditos, route_cuentas, route_operaciones, route_public, route_reclamos

app = FastAPI(
    title="Banca Internet Banco Andino — Homebanking API",
    description="Portal del cliente de Banca Internet Banco Andino. Solo consultas y "
    "operaciones del cliente del portal (dcliente / usuarios_homebanking).",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(route_auth.router)
app.include_router(route_cuentas.router)
app.include_router(route_operaciones.router)
app.include_router(route_creditos.router)
app.include_router(route_public.router)
app.include_router(route_reclamos.router)


@app.get("/", tags=["root"])
def raiz():
    return {
        "servicio": "Banca Internet Banco Andino — Homebanking API",
        "version": "1.0.0",
        "estado": "ok",
        "docs": "/docs",
        "puerto": int(os.environ.get("PORT", settings.PORT)),
    }
