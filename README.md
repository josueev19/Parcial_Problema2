# Menú Restaurante — problema2_menu_restaurante.py

**Descripción**
- Script en Python que muestra un menú de restaurante y aplica una promoción automática del 15% a los platos de una categoría objetivo cuyo precio base supera un umbral.

**Archivo**
- Código principal: [problema2_menu_restaurante.py](problema2_menu_restaurante.py)

**Requisitos**
- Python 3.x

**Uso**
- Ejecutar desde la terminal:

```
python problema2_menu_restaurante.py
```

**Cómo funciona**
- El menú está definido en la variable `menu` como una lista de listas: `[Nombre, Categoría, Precio Base]`.
- Parámetros de la promoción (modificables al inicio del archivo):
  - `categoria_objetivo` — categoría que recibe el descuento (ej.: "Plato Principal").
  - `umbral_precio` — precio mínimo para aplicar el descuento.
  - `descuento` — fracción aplicada (0.15 corresponde a 15%).
- La función `calcular_precio_final(precio_base, categoria, cat_objetivo, umbral)` devuelve el precio final con descuento si aplica, o el precio base si no.

**Salida de ejemplo**
- El script imprime una tabla con columnas: Producto, Categoría, Precio Base y Precio Final. Los ítems con descuento muestran la nota "<- 15% desc.".

**Personalización rápida**
- Para cambiar la promoción, edite las variables `categoria_objetivo`, `umbral_precio` y `descuento` en [problema2_menu_restaurante.py](problema2_menu_restaurante.py).
- Para añadir o quitar productos, modifique la lista `menu`.

**¿Quieres que lo convierta en un módulo reutilizable o añada pruebas?**
- Dime si quieres que genere una versión con funciones exportables, tests unitarios o un `requirements.txt`.
