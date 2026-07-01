"""Schemas para el módulo de reclamos / seguimiento."""
from datetime import date

from pydantic import BaseModel, Field


class ReclamoRequest(BaseModel):
    asunto: str = Field(..., min_length=5, max_length=200, description="Asunto del reclamo")
    descripcion: str = Field(..., min_length=10, max_length=2000, description="Detalle del reclamo")
    tipo: str = Field(default="RECLAMO", description="RECLAMO | QUEJA | CONSULTA")


class ReclamoOut(BaseModel):
    id: int
    asunto: str
    descripcion: str
    tipo: str
    estado: str
    fecha_creacion: date
    fecha_resolucion: date | None = None
    respuesta: str | None = None


class ReclamoListResponse(BaseModel):
    reclamos: list[ReclamoOut]
    total: int
