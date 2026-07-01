"""Controlador de reclamos — datos en memoria simulado (sin tabla en BD)."""
from datetime import date

# Almacén en memoria (simulado)
_reclamos: list[dict] = []
_next_id = 1


def listar_reclamos(pkcliente: int) -> list[dict]:
    return [r for r in _reclamos if r["pkcliente"] == pkcliente]


def crear_reclamo(pkcliente: int, asunto: str, descripcion: str, tipo: str) -> dict:
    global _next_id
    reclamo = {
        "id": _next_id,
        "pkcliente": pkcliente,
        "asunto": asunto,
        "descripcion": descripcion,
        "tipo": tipo.upper(),
        "estado": "Pendiente",
        "fecha_creacion": date.today().isoformat(),
        "fecha_resolucion": None,
        "respuesta": None,
    }
    _next_id += 1
    _reclamos.append(reclamo)
    return reclamo
