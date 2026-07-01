"""Controlador de endpoints públicos (simulador, tarifarios, transparencia)."""
from app.utils.financieras import ted, tem, fpc
from app.utils.productos import listar_productos, obtener_producto

# TMIC de referencia por tipo (Tasa Máxima de Interés Convencional — valores ilustrativos)
TMIC_REF = {
    "ME": 65.0, "PE": 45.0, "CO": 55.0, "HI": 18.0, "GE": 25.0,
}


def simular(monto: float, plazo: int, tea: float) -> dict:
    td = ted(tea)
    tm = tem(tea)
    factor = fpc(tea, plazo)
    cuota = monto * factor if factor > 0 else monto / plazo

    saldo = monto
    total_intereses = 0.0
    cronograma = []
    for n in range(1, plazo + 1):
        interes = saldo * tm
        capital = cuota - interes
        saldo = max(0.0, saldo - capital)
        total_intereses += interes
        cronograma.append({
            "nrocuota": n,
            "cuota": round(cuota, 2),
            "capital": round(capital, 2),
            "interes": round(interes, 2),
            "saldo": round(saldo, 2),
        })

    return {
        "monto": round(monto, 2),
        "plazo_meses": plazo,
        "tea": tea,
        "ted": round(td * 100, 6),
        "tem": round(tm * 100, 4),
        "tcea": round(tea + 1.5, 2),  # TCEA = TEA + comisiones estimadas (~1.5%)
        "cuota_referencial": round(cuota, 2),
        "total_intereses": round(total_intereses, 2),
        "total_pagar": round(monto + total_intereses, 2),
        "cronograma": cronograma,
    }


def listar_tarifarios() -> dict:
    productos = []
    for p in listar_productos():
        cod = p["codigo"]
        tea_ref = {"ME": 40.0, "PE": 25.0, "CO": 33.0, "HI": 11.5, "GE": 15.0}
        tea_min = {"ME": 28.0, "PE": 18.0, "CO": 22.0, "HI": 9.0, "GE": 12.0}
        tea_max = {"ME": 55.0, "PE": 32.0, "CO": 45.0, "HI": 14.0, "GE": 18.0}
        productos.append({
            "codigo": cod,
            "nombre": p["nombre"],
            "subtitulo": p["subtitulo"],
            "descripcion": p["descripcion"],
            "tea_min": tea_min.get(cod, 15.0),
            "tea_mid": tea_ref.get(cod, 20.0),
            "tea_max": tea_max.get(cod, 30.0),
            "tmic_referencial": TMIC_REF.get(cod, 30.0),
        })

    return {
        "productos": productos,
        "vigencia": "Julio 2026",
        "notas": "Tasas referenciales sujetas a evaluación crediticia. "
                 "TMIC = Tasa Máxima de Interés Convencional (BCRP).",
    }
