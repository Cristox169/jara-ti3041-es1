# CrisSteel - Catálogo online

Proyecto individual para la Evaluación Sumativa 1 de Programación Back End (TI3041). Presenta el catálogo estático de una ferretería local mediante Django, sin conexión a base de datos.

## Características

- 40 productos de ferretería cargados desde JSON en `catalogo/views.py`.
- Listado completo mediante un bucle de template.
- Ficha de detalle por id y respuesta 404 para ids inexistentes.
- Resumen calculado: total, productos con stock, agotados y categorías.
- Destacado condicional de productos sin stock.
- Filtros por categoría, tema claro/oscuro e interfaz responsive.
- Landing con una frase fuerza y acceso directo al flujo de venta.
- Punto de venta interactivo con búsqueda, filtros, carro y control de cantidades.
- Comprobante visual con animación ficticia de impresión al terminar la compra.
- Iconos SVG locales e imagen original de portada.
- Ocho pruebas automatizadas.
- Cinco etapas documentadas con capturas en `docs/evidencias/`.

## Instalación y ejecución

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py runserver
```

### macOS o Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py runserver
```

Abrir `http://127.0.0.1:8000/` en el navegador.

## Verificación

```bash
python manage.py check
python manage.py test
```

## Estructura principal

```text
catalogo/
├── static/catalogo/        # Estilos, scripts, icono e imagen de portada
├── templates/catalogo/     # Base, listado, detalle, punto de venta e iconos
├── tests.py                # Pruebas del catálogo
├── urls.py                 # Rutas con nombre
└── views.py                # JSON, cálculos, listado y detalle
docs/
├── commits.md              # Relato visual de las cinco etapas
└── evidencias/             # Pantallazos versionados
uso_ia.md                   # Registro de consultas y sección personal
```

## Evidencias y uso de IA

- [Evidencias de commits](docs/commits.md)
- [Registro de uso de IA](uso_ia.md)

La Parte 2 de `uso_ia.md` fue redactada personalmente por el estudiante, tal como exige la pauta.
