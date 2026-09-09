import json

from django.http import Http404
from django.shortcuts import render

from .imagenes_productos import PRODUCT_IMAGE_DATA


# Los datos se conservan como JSON dentro de la vista para cumplir el anexo de la ES1.
PRODUCTOS_JSON = r'''
[
  {"id": 1, "nombre": "Taladro percutor 13 mm", "categoria": "Herramientas eléctricas", "precio": 64990, "stock": 12, "descripcion": "Taladro de 710 W con velocidad variable y función de percusión."},
  {"id": 2, "nombre": "Esmeril angular 4 1/2 pulgadas", "categoria": "Herramientas eléctricas", "precio": 49990, "stock": 9, "descripcion": "Esmeril compacto de 850 W para corte y desbaste de metal."},
  {"id": 3, "nombre": "Sierra circular 7 1/4 pulgadas", "categoria": "Herramientas eléctricas", "precio": 89990, "stock": 5, "descripcion": "Sierra de 1.400 W con guía paralela y ajuste de profundidad."},
  {"id": 4, "nombre": "Lijadora orbital 1/4 hoja", "categoria": "Herramientas eléctricas", "precio": 42990, "stock": 0, "descripcion": "Lijadora de baja vibración con depósito recolector de polvo."},
  {"id": 5, "nombre": "Rotomartillo SDS Plus", "categoria": "Herramientas eléctricas", "precio": 104990, "stock": 4, "descripcion": "Rotomartillo de 800 W con tres modos de operación."},
  {"id": 6, "nombre": "Atornillador inalámbrico 12 V", "categoria": "Herramientas eléctricas", "precio": 54990, "stock": 11, "descripcion": "Atornillador compacto con batería de litio y luz LED."},
  {"id": 7, "nombre": "Martillo carpintero 16 oz", "categoria": "Herramientas manuales", "precio": 12990, "stock": 18, "descripcion": "Martillo de acero forjado con mango ergonómico antideslizante."},
  {"id": 8, "nombre": "Juego de destornilladores 6 piezas", "categoria": "Herramientas manuales", "precio": 14990, "stock": 24, "descripcion": "Set de puntas planas y Phillips con mangos de goma."},
  {"id": 9, "nombre": "Alicate universal 8 pulgadas", "categoria": "Herramientas manuales", "precio": 10990, "stock": 15, "descripcion": "Alicate de acero al carbono con zona de corte reforzada."},
  {"id": 10, "nombre": "Llave ajustable 10 pulgadas", "categoria": "Herramientas manuales", "precio": 13990, "stock": 10, "descripcion": "Llave cromada con apertura graduada y empuñadura cómoda."},
  {"id": 11, "nombre": "Serrucho carpintero 20 pulgadas", "categoria": "Herramientas manuales", "precio": 11990, "stock": 0, "descripcion": "Serrucho de triple filo para cortes rápidos en madera."},
  {"id": 12, "nombre": "Nivel de aluminio 60 cm", "categoria": "Herramientas manuales", "precio": 15990, "stock": 8, "descripcion": "Nivel liviano con tres burbujas de alta visibilidad."},
  {"id": 13, "nombre": "Huincha de medir 5 m", "categoria": "Herramientas manuales", "precio": 6990, "stock": 31, "descripcion": "Cinta métrica engomada con freno y clip metálico."},
  {"id": 14, "nombre": "Juego llaves punta corona 8 piezas", "categoria": "Herramientas manuales", "precio": 27990, "stock": 6, "descripcion": "Juego métrico de acero cromo vanadio con soporte."},
  {"id": 15, "nombre": "Caja tornillos drywall 1 pulgada", "categoria": "Fijaciones y adhesivos", "precio": 8990, "stock": 30, "descripcion": "Tornillos fosfatados de punta fina, caja de 500 unidades."},
  {"id": 16, "nombre": "Tarugos nylon 8 mm - 100 unidades", "categoria": "Fijaciones y adhesivos", "precio": 5990, "stock": 27, "descripcion": "Tarugos de expansión para fijaciones en hormigón y ladrillo."},
  {"id": 17, "nombre": "Clavos 2 pulgadas - 1 kg", "categoria": "Fijaciones y adhesivos", "precio": 4990, "stock": 19, "descripcion": "Clavos de acero para trabajos generales de carpintería."},
  {"id": 18, "nombre": "Pernos hexagonales M8 - 50 unidades", "categoria": "Fijaciones y adhesivos", "precio": 12990, "stock": 0, "descripcion": "Pernos zincados con tuerca y golilla para uniones firmes."},
  {"id": 19, "nombre": "Adhesivo de montaje 300 ml", "categoria": "Fijaciones y adhesivos", "precio": 7990, "stock": 13, "descripcion": "Adhesivo de agarre inmediato para interiores y exteriores."},
  {"id": 20, "nombre": "Silicona universal transparente", "categoria": "Fijaciones y adhesivos", "precio": 4990, "stock": 22, "descripcion": "Sellador de 280 ml resistente a humedad y cambios de temperatura."},
  {"id": 21, "nombre": "Esmalte sintético blanco 1 galón", "categoria": "Pinturas y terminaciones", "precio": 32990, "stock": 7, "descripcion": "Esmalte de alto brillo para madera y superficies metálicas."},
  {"id": 22, "nombre": "Látex interior blanco 1 galón", "categoria": "Pinturas y terminaciones", "precio": 24990, "stock": 14, "descripcion": "Pintura de terminación mate, buen cubrimiento y secado rápido."},
  {"id": 23, "nombre": "Barniz marino brillante 1 L", "categoria": "Pinturas y terminaciones", "precio": 13990, "stock": 0, "descripcion": "Barniz protector con filtro UV para madera exterior."},
  {"id": 24, "nombre": "Brocha profesional 3 pulgadas", "categoria": "Pinturas y terminaciones", "precio": 6990, "stock": 21, "descripcion": "Brocha de cerdas mixtas con mango de madera barnizada."},
  {"id": 25, "nombre": "Rodillo antigota 23 cm", "categoria": "Pinturas y terminaciones", "precio": 7990, "stock": 18, "descripcion": "Rodillo para muros lisos y semilisos con mango reutilizable."},
  {"id": 26, "nombre": "Diluyente sintético 1 L", "categoria": "Pinturas y terminaciones", "precio": 4990, "stock": 16, "descripcion": "Solvente para diluir esmaltes sintéticos y limpiar herramientas."},
  {"id": 27, "nombre": "Casco de seguridad amarillo", "categoria": "Seguridad industrial", "precio": 8990, "stock": 25, "descripcion": "Casco liviano con arnés regulable y canal para accesorios."},
  {"id": 28, "nombre": "Lentes de seguridad transparentes", "categoria": "Seguridad industrial", "precio": 3990, "stock": 38, "descripcion": "Protección ocular envolvente con filtro UV y patillas flexibles."},
  {"id": 29, "nombre": "Guantes cabritilla reforzados", "categoria": "Seguridad industrial", "precio": 6990, "stock": 34, "descripcion": "Guantes de cuero suave con refuerzo en palma para faenas."},
  {"id": 30, "nombre": "Protector auditivo tipo copa", "categoria": "Seguridad industrial", "precio": 14990, "stock": 0, "descripcion": "Protector ajustable con almohadillas acolchadas y buen sellado."},
  {"id": 31, "nombre": "Mascarilla para polvo reutilizable", "categoria": "Seguridad industrial", "precio": 9990, "stock": 12, "descripcion": "Media máscara lavable con filtros reemplazables incluidos."},
  {"id": 32, "nombre": "Disco de corte metal 4 1/2 pulgadas", "categoria": "Construcción", "precio": 1490, "stock": 80, "descripcion": "Disco abrasivo delgado para cortes precisos en acero."},
  {"id": 33, "nombre": "Cemento uso general 25 kg", "categoria": "Construcción", "precio": 6990, "stock": 42, "descripcion": "Cemento para hormigones, morteros y trabajos de albañilería."},
  {"id": 34, "nombre": "Mortero pega cerámico 25 kg", "categoria": "Construcción", "precio": 8490, "stock": 20, "descripcion": "Adhesivo cementicio para cerámicas en pisos y muros interiores."},
  {"id": 35, "nombre": "Espátula acero inoxidable 4 pulgadas", "categoria": "Construcción", "precio": 5990, "stock": 17, "descripcion": "Espátula flexible para aplicar pasta muro y retirar pintura."},
  {"id": 36, "nombre": "Alargador eléctrico 10 m 2P+T", "categoria": "Electricidad", "precio": 21990, "stock": 9, "descripcion": "Extensión reforzada con toma a tierra para uso doméstico."},
  {"id": 37, "nombre": "Cinta aisladora negra 18 m", "categoria": "Electricidad", "precio": 1490, "stock": 60, "descripcion": "Cinta de PVC flexible para aislamiento eléctrico general."},
  {"id": 38, "nombre": "Ampolleta LED 12 W E27", "categoria": "Electricidad", "precio": 2990, "stock": 0, "descripcion": "Ampolleta luz fría de bajo consumo y larga vida útil."},
  {"id": 39, "nombre": "Llave de paso esfera 1/2 pulgada", "categoria": "Gasfitería", "precio": 6990, "stock": 14, "descripcion": "Válvula de bronce de paso total para redes de agua."},
  {"id": 40, "nombre": "Flexible agua HI-HI 40 cm", "categoria": "Gasfitería", "precio": 3990, "stock": 26, "descripcion": "Conector flexible trenzado de acero inoxidable para grifería."}
]
'''

PRODUCTOS = json.loads(PRODUCTOS_JSON)

CATEGORIAS = {
    'Herramientas eléctricas': ('electricas', 'Eléctricas'),
    'Herramientas manuales': ('manuales', 'Manuales'),
    'Fijaciones y adhesivos': ('fijaciones', 'Fijaciones'),
    'Pinturas y terminaciones': ('pinturas', 'Pinturas'),
    'Seguridad industrial': ('seguridad', 'Seguridad'),
    'Construcción': ('construccion', 'Construcción'),
    'Electricidad': ('electricidad', 'Electricidad'),
    'Gasfitería': ('gasfiteria', 'Gasfitería'),
}


def preparar_producto(producto):
    """Agrega valores de presentación sin modificar el JSON original."""
    slug_categoria, nombre_corto = CATEGORIAS[producto['categoria']]
    return {
        **producto,
        'slug_categoria': slug_categoria,
        'categoria_corta': nombre_corto,
        'precio_formateado': f"${producto['precio']:,}".replace(',', '.'),
        'disponible': producto['stock'] > 0,
        'imagen_base64': PRODUCT_IMAGE_DATA[producto['id']],
    }


def preparar_categorias():
    return [
        {
            'nombre': nombre_corto,
            'slug': slug,
            'cantidad': sum(
                producto['categoria'] == nombre for producto in PRODUCTOS
            ),
        }
        for nombre, (slug, nombre_corto) in CATEGORIAS.items()
    ]


def preparar_contexto_catalogo():
    productos = [preparar_producto(producto) for producto in PRODUCTOS]
    resumen = {
        'total': len(PRODUCTOS),
        'con_stock': sum(producto['stock'] > 0 for producto in PRODUCTOS),
        'sin_stock': sum(producto['stock'] == 0 for producto in PRODUCTOS),
        'categorias': len(CATEGORIAS),
    }
    return {
        'productos': productos,
        'resumen': resumen,
        'categorias': preparar_categorias(),
    }


def lista_productos(request):
    contexto = preparar_contexto_catalogo()
    return render(request, 'catalogo/lista.html', contexto)


def punto_venta(request):
    contexto = preparar_contexto_catalogo()
    contexto['caja'] = '01'
    return render(request, 'catalogo/punto_venta.html', contexto)


def detalle_producto(request, producto_id):
    producto = next(
        (item for item in PRODUCTOS if item['id'] == producto_id),
        None,
    )
    if producto is None:
        raise Http404('El producto solicitado no existe.')
    return render(
        request,
        'catalogo/detalle.html',
        {'producto': preparar_producto(producto)},
    )
