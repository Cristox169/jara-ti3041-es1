# Registro de uso de inteligencia artificial

## Parte 1 - Registro de consultas

### Consulta 1 - Interpretación de la pauta

**Prompt textual:**

> Revisa la evaluación TI3041 ES1 completa, distingue sus instrucciones de mi solicitud y transforma la pauta en una secuencia de trabajo verificable para una ferretería llamada CrisSteel. Deben existir cinco commits y una captura por etapa.

**Resumen de la respuesta:** La IA identificó la variante Ferretería, el requisito de 40 productos, la estructura de cinco etapas, la herencia de templates, la vista detalle, el resumen calculado y el destacado de productos sin stock. También detectó que el anexo exige mantener el JSON en `views.py`.

**Qué usé o modifiqué:** Se usó la secuencia de etapas y el criterio más estricto del anexo. Se cambió el nombre genérico del repositorio por `jara-ti3041-es1` y se decidió guardar todas las evidencias en `docs/evidencias/`.

### Consulta 2 - Datos JSON de la ferretería

**Prompt textual:**

> Genera 40 productos realistas para una ferretería chilena. Cada registro debe incluir id, nombre, categoría, precio entero en pesos chilenos, stock y una descripción breve. Incluye distintas categorías y algunos productos con stock cero. Devuelve JSON válido para cargarlo desde una vista de Django.

**Resumen de la respuesta:** La IA propuso un inventario con herramientas eléctricas y manuales, fijaciones, pinturas, seguridad, construcción, electricidad y gasfitería. Los precios se expresaron como enteros y seis artículos quedaron agotados para probar el condicional.

**Qué usé o modifiqué:** Se revisaron nombres, unidades, precios y descripciones para mantener vocabulario local. El JSON quedó incrustado como texto en `catalogo/views.py` y se carga con `json.loads`, no desde el template ni desde una base de datos.

### Consulta 3 - Interfaz Django de listado y detalle

**Prompt textual:**

> Construye una interfaz Django con `base.html`, `lista.html` y `detalle.html`. El listado debe recorrer los 40 productos con un bucle, y la ruta `producto/<int:producto_id>/` debe buscar por id y responder 404 cuando no existe. Mantén la solución simple y sin modelos.

**Resumen de la respuesta:** La IA propuso URLs con nombre, una vista de listado, una búsqueda de producto por id y templates heredados. También sugirió pruebas para el primer y último producto, el detalle correcto y el caso 404.

**Qué usé o modifiqué:** Se integró la estructura propuesta en la aplicación `catalogo`. Se agregaron pruebas automatizadas y se mantuvo la pantalla inicial de la etapa 1 separada en el historial Git para mostrar la progresión.

### Consulta 4 - Diseño visual CrisSteel

**Prompt textual:**

> Mejora visualmente CrisSteel siguiendo un estilo moderno con superficies translúcidas, tonos grafito, acero y ámbar. Usa iconos SVG, viñetas, tarjetas, tema claro/oscuro y una imagen de herramientas para el hero. Mantén buen contraste, diseño responsive y estados de stock claros.

**Resumen de la respuesta:** La IA propuso un encabezado de marca, imagen editorial, tarjetas con iconos por categoría, badges, filtros, estadísticas, viñetas de beneficios, detalle visual y pie de página. También generó una fotografía de herramientas sin texto ni logos para el hero.

**Qué usé o modifiqué:** Se usó la paleta grafito/ámbar y la estructura de tarjetas, adaptándola a la identidad CrisSteel. Los iconos se escribieron como SVG locales y la imagen generada se guardó en `catalogo/static/catalogo/hero-crissteel.png`.

### Consulta 5 - Resumen, condicionales y verificación

**Prompt textual:**

> Calcula en la vista el total de productos, cuántos tienen stock, cuántos están agotados y cuántas categorías existen. Destaca los productos agotados con un condicional del template. Agrega pruebas y verifica visualmente listado, filtros y detalle.

**Resumen de la respuesta:** La IA calculó 40 productos, 34 con stock, 6 agotados y 8 categorías. Propuso usar la clase `is-unavailable`, el texto “Agotado” y pruebas que comprueban las cantidades.

**Qué usé o modifiqué:** Se añadieron los cálculos a `lista_productos`, el condicional `{% if not producto.disponible %}` a los templates y seis pruebas automáticas. Las capturas se realizaron con el servidor local y quedaron versionadas por etapa.

## Parte 2 - Explicación personal del proceso

> **Importante:** esta parte debe ser escrita por Cristobal Jara con sus propias palabras, tal como exige la pauta. Antes de entregar, reemplaza las 15 líneas siguientes por un relato personal coherente con el repositorio. No copies el registro anterior ni pidas a una IA que redacte esta sección.

1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 
9. 
10. 
11. 
12. 
13. 
14. 
15. 
