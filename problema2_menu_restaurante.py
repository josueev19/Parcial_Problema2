# ── MATRIZ DE DATOS ──────────────────────────────────────────────────
# Formato: [Nombre del Producto, Categoría, Precio Base]

menu = [
    ["Bandeja Paisa",       "Plato Principal", 32000],
    ["Sancocho Trifásico",  "Plato Principal", 28000],
    ["Ajiaco Bogotano",     "Plato Principal", 18000],
    ["Limonada de Coco",    "Bebida",           9000],
    ["Jugo Natural",        "Bebida",           7500],
    ["Ceviche de Camarón",  "Entrada",         22000],
    ["Patacones con Hogao", "Entrada",         12000],
    ["Tres Leches",         "Postre",          11000],
]

# ── PARÁMETROS DE LA PROMOCIÓN ───────────────────────────────────────

categoria_objetivo = "Plato Principal"
umbral_precio      = 20000
descuento          = 0.15

# ── MÓDULO: función que calcula el precio final ──────────────────────

def calcular_precio_final(precio_base, categoria, cat_objetivo, umbral):
    if categoria == cat_objetivo and precio_base > umbral:
        return precio_base * (1 - descuento)
    return precio_base

# ── PROGRAMA PRINCIPAL ────────────────────────────────────────────────

print(f"{'Producto':<22} {'Categoría':<18} {'Precio Base':>12} {'Precio Final':>12}")
print("-" * 68)

for fila in menu:
    nombre    = fila[0]
    categoria = fila[1]
    base      = fila[2]
    final     = calcular_precio_final(base, categoria, categoria_objetivo, umbral_precio)

    nota = " <- 15% desc." if final < base else ""
    print(f"{nombre:<22} {categoria:<18} ${base:>10,} ${final:>10,.0f}{nota}")
