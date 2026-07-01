"""Rutas públicas (sin autenticación): simulador, tarifarios."""
from fastapi import APIRouter, HTTPException, status

from app.controllers import ctrl_public
from app.schemas.sch_public import SimularRequest, SimularResponse, TarifarioResponse

router = APIRouter(prefix="/public", tags=["public"])


@router.post("/simular", response_model=SimularResponse)
def simular(body: SimularRequest):
    if body.plazo > 120:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Plazo máximo 120 meses")
    if body.tea <= 0 or body.tea > 100:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="TEA fuera de rango")
    return ctrl_public.simular(body.monto, body.plazo, body.tea)


@router.get("/tarifarios", response_model=TarifarioResponse)
def tarifarios():
    return ctrl_public.listar_tarifarios()
