"""
Utilidades financieras — mismo API que BackendCore/app/utils/financieras.py.
Standalone, sin dependencia de la BD.
"""


def ted(tea: float) -> float:
    if tea <= -100:
        return 0.0
    return (1 + tea / 100) ** (1 / 360) - 1


def tem(tea: float) -> float:
    if tea <= -100:
        return 0.0
    return (1 + tea / 100) ** (1 / 12) - 1


def fpc(tea: float, plazo: int) -> float:
    tm = tem(tea)
    if tm <= 0 or plazo <= 0:
        return 1.0 / plazo if plazo > 0 else 0.0
    return tm * (1 + tm) ** plazo / ((1 + tm) ** plazo - 1)


def tcea(tea: float, comisiones: list[float] | None = None,
         gastos: list[float] | None = None, monto: float = 1.0) -> float:
    cargo_extra = (sum(comisiones or []) + sum(gastos or [])) / monto if monto > 0 else 0
    return tea + cargo_extra * 100
