"""Schemas para endpoints públicos (simulador, tarifarios, transparencia)."""
from pydantic import BaseModel, Field


class SimularRequest(BaseModel):
    monto: float = Field(..., gt=0, description="Monto del crédito")
    plazo: int = Field(..., ge=1, le=120, description="Plazo en meses")
    tea: float = Field(..., gt=0, description="TEA en porcentaje (ej: 33.0)")


class CuotaSimulada(BaseModel):
    nrocuota: int
    cuota: float
    capital: float
    interes: float
    saldo: float


class SimularResponse(BaseModel):
    monto: float
    plazo_meses: int
    tea: float
    ted: float
    tem: float
    tcea: float
    cuota_referencial: float
    total_intereses: float
    total_pagar: float
    cronograma: list[CuotaSimulada]


class TarifarioItem(BaseModel):
    codigo: str
    nombre: str
    subtitulo: str
    descripcion: str
    tea_min: float
    tea_mid: float
    tea_max: float
    tmic_referencial: float


class TarifarioResponse(BaseModel):
    productos: list[TarifarioItem]
    vigencia: str
    notas: str
