"""Router de reclamos. Exige get_cliente."""
from fastapi import APIRouter, Depends

from app.controllers import ctrl_reclamos
from app.core.cfg_auth import get_cliente
from app.schemas.sch_reclamos import ReclamoOut, ReclamoRequest, ReclamoListResponse

router = APIRouter(prefix="/reclamos", tags=["reclamos"], dependencies=[Depends(get_cliente)])


@router.get("/", response_model=ReclamoListResponse)
def listar_reclamos(cliente: dict = Depends(get_cliente)):
    reclamos = ctrl_reclamos.listar_reclamos(cliente["pkcliente"])
    return {"reclamos": reclamos, "total": len(reclamos)}


@router.post("/", response_model=ReclamoOut)
def crear_reclamo(body: ReclamoRequest, cliente: dict = Depends(get_cliente)):
    return ctrl_reclamos.crear_reclamo(
        cliente["pkcliente"], body.asunto, body.descripcion, body.tipo
    )
