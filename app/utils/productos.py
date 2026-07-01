"""
Catálogo de productos con nombre comercial — mismo API que BackendCore.
"""

PRODUCTOS = {
    "ME": {
        "codigo": "ME",
        "nombre": "Prospera",
        "subtitulo": "Crédito Microempresa",
        "descripcion": "Financiamiento ágil para emprendedores y pequeños negocios.",
    },
    "PE": {
        "codigo": "PE",
        "nombre": "Construyendo Sueños",
        "subtitulo": "Crédito Pequeña Empresa",
        "descripcion": "Impulsa el crecimiento de tu empresa con tasas preferenciales.",
    },
    "CO": {
        "codigo": "CO",
        "nombre": "Momentum",
        "subtitulo": "Crédito de Consumo",
        "descripcion": "El efectivo que necesitas con cuotas a tu medida.",
    },
    "HI": {
        "codigo": "HI",
        "nombre": "Hogar Seguro",
        "subtitulo": "Crédito Hipotecario",
        "descripcion": "Tu casa propia con la mejor tasa del mercado.",
    },
    "GE": {
        "codigo": "GE",
        "nombre": "Flexnegocio",
        "subtitulo": "Crédito Genérico",
        "descripcion": "Solución financiera flexible para tu negocio.",
    },
}


def obtener_producto(codigo: str) -> dict | None:
    return PRODUCTOS.get(codigo.upper().strip())


def listar_productos() -> list[dict]:
    return list(PRODUCTOS.values())
