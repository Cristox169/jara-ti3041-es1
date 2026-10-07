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

### Consulta 6 - Landing y punto de venta interactivo

**Prompt textual:**

> Hagamos más evidente el landing page con una frase fuerza que destaque el objetivo del sitio. Genera un carrito de compra estilo punto de venta con productos seleccionables, controles para sumar, restar y eliminar, total destacado, búsqueda, filtros por categoría y un comprobante con una pequeña animación ficticia de impresión.

**Resumen de la respuesta:** La IA propuso reforzar el mensaje principal de CrisSteel y crear una pantalla de caja separada. El punto de venta muestra las 40 fichas, permite buscarlas y filtrarlas, administra las cantidades del carro respetando el stock y genera una boleta visual al finalizar.

**Qué usé o modifiqué:** Se incorporó la frase “Todo para construir. En un solo lugar.” en la portada, un acceso visible a la caja y la ruta `/punto-de-venta/`. La interacción se implementó en JavaScript sin pagos ni persistencia, y el comprobante se presenta como una simulación académica. También se agregaron dos pruebas para verificar la nueva vista y sus controles.

### Consulta 7 - Imágenes autocontenidas para los productos

**Prompt textual:**

> El punto de venta no debe tener landing page, solo el sitio principal. Realiza scraping para encontrar imágenes para cada uno de los productos y usa Base64 para que sea autocontenido.

**Resumen de la respuesta:** La IA eliminó el bloque tipo landing del punto de venta y buscó una imagen abierta para cada uno de los 40 artículos mediante la API de Wikimedia Commons. Las imágenes se normalizaron, comprimieron en WebP y se incrustaron como URI Base64 para evitar dependencias externas durante la navegación.

**Qué usé o modifiqué:** Se conservaron la portada y su frase fuerza únicamente en el inicio. El POS ahora abre directamente en su barra operativa, búsqueda, filtros, productos y carro. Las imágenes se incorporaron al listado, al detalle y a la caja; además se guardaron una hoja de contacto, el importador reproducible y una tabla con autoría, URL y licencia.

### Consulta 8 - Reparación del proyecto ES2 y apertura en el puerto 8000

**Prompt textual:**

> Agrégale al ZIP el enlace `http://127.0.0.1:8000/` y haz que aparezca al ejecutar `python manage.py runserver`. Crea una página para una ferretería que se abra con ese enlace y que cumpla los cambios solicitados en el documento Word y en el PDF.

**Resumen de la respuesta:** La IA revisó la pauta entregada en Word y PDF, inspeccionó el proyecto comprimido y reparó archivos que contenían saltos de línea escritos como texto, lo que impedía iniciar Django. También cambió la ruta principal para que el catálogo de la ferretería se abriera directamente en `/`, conservó las vistas de catálogo, detalle, punto de venta y administración, y unificó la ejecución local en el puerto 8000.

**Qué usé o modifiqué:** Se corrigieron la configuración de Django, las rutas y las dependencias. Además, se agregó un comando `runserver` personalizado que muestra `Sitio principal: http://127.0.0.1:8000/` al iniciar el servidor. Se mantuvieron el modelo de productos, las migraciones, la carga de 40 productos, los filtros, la vista de detalle, el punto de venta y Django Admin. Para que el ZIP pudiera probarse de inmediato se dejó SQLite como configuración predeterminada, con soporte opcional para MariaDB mediante variables de entorno.

### Consulta 9 - Verificación y entrega del ZIP corregido

**Prompt textual:**

> Pásame un ZIP para descargar con lo que hiciste.

**Resumen de la respuesta:** La IA comprobó el proyecto antes de empaquetarlo: ejecutó las validaciones de Django, creó una base de datos limpia, aplicó las migraciones, cargó los 40 productos y verificó que la portada, el detalle de producto, el punto de venta y Django Admin respondieran correctamente. También revisó visualmente la página en tamaños de escritorio y móvil.

**Qué usé o modifiqué:** Se generó un nuevo archivo ZIP sin entornos virtuales ni archivos temporales. Después se extrajo en una carpeta limpia y se volvió a probar para confirmar que la entrega fuera reproducible y que pudiera ejecutarse con `python manage.py runserver`.

### Consulta 10 - Actualización del repositorio de GitHub de ES2

**Prompt textual:**

> Actualiza `https://github.com/Cristox169/CristobalJara-ti3041-es2` con lo que hiciste.

**Resumen de la respuesta:** La IA clonó la versión vigente del repositorio ES2, preservó su configuración de MariaDB y sus módulos existentes, y aplicó únicamente los cambios necesarios para que la tienda se abriera en `http://127.0.0.1:8000/`, para que el servidor mostrara ese enlace y para que la documentación coincidiera con el comportamiento real del proyecto.

**Qué usé o modifiqué:** Se actualizaron las rutas principales, el comando de ejecución, las pruebas y la documentación. Los cambios fueron verificados y publicados en la rama `main` de GitHub mediante el commit `95f53e9`.

### Consulta 11 - Superusuario y botón para Django Admin

**Prompt textual:**

> Crea el superusuario con nombre `admin` y contraseña `jarax`, actualiza el ZIP y agrega en la página un botón que permita acceder a la Administración de Django. Después actualiza el enlace de GitHub.

**Resumen de la respuesta:** La IA creó las credenciales de desarrollo solicitadas, agregó en la navegación de la tienda un botón visible hacia `/admin/` y ajustó el diseño para que funcionara correctamente en escritorio y dispositivos móviles. En el proyecto MariaDB también automatizó la creación o actualización del administrador al cargar los datos iniciales.

**Qué usé o modifiqué:** Se actualizó la base de datos incluida en el ZIP con el usuario `admin`, se modificaron las plantillas y los estilos, y se añadieron pruebas para comprobar el enlace de administración y el acceso del superusuario. En GitHub se amplió el comando de carga inicial para aceptar `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL` y `DJANGO_SUPERUSER_PASSWORD`, con los valores de desarrollo solicitados como predeterminados. Esta actualización se publicó en la rama `main` mediante el commit `c76db0d`.

## Parte 2 - Explicación personal del proceso

Fue un proyecto desafiante en el cual ni siquiera podia correr Django en mi equipo, por lo tanto me di la labor de investigar y descubri que las variables de entorno en ocasiones dan multiples problemas, sobre todo con Java, pero no es el caso. Como llevo utilzando este euqipo sin formatear desde inicio de la carrera iba a ser un caos solucionar los conflictos con las variables de entorno. En su lugar encontre la forma de crear entornos aislados utilizables solo para el proyecto, asi di con los .venv que me permitieron instalar las dependencias localmente en la carpeta del proyecto sin tener que batallar con los distintos vestigios de mis años de carrera pasados.

Una vez con Django corriendo la vida fue mas facil, comenze a desarrollar los distintos layout requeridos para esta primera etapa, css siempre es un desafio por sus diferentes gerarquias, pero afortunadamente pudo ser sorteado ccon problemas minimos. Al continuar trabajando, pese a los cambios de plataforma, me refiero a que siempre hemos programado localmente y ahora estando en una aplicacion web las librerias continuan siendo las mismas, incluso nuestro buen amigo os, con la cual pude acceder a las direcciones fisicas en las cuales crearia y se almacenarian los archivos json.

Debo confesar que jamas habia entendido el uso del try y catch hasta ahora. El try es un intento por alcanzar u obtener algo, y en caso que no pueda se encuentran ahi los catch que brindan apoyo en caso que no sea alcanzable el objetivo. Explicado de otra forma si intentaramos saltar desde el sexto piso de Inacap con afan de volar, obviamente no podriamos. Pero abajo se encontrara el catch para hacer de red de seguridad para que asi tanto mi vida como el programa no se cuelguen. En Python no se llama catch la instruccion inclusive tiene una arista mas qque seria finally, para dejarlo totalmente claro podriamos decir que en nuestro finally habran felicitaciones por ejemplo si salto y logro volar habran felicitaciones, en contraste si salto y no logro volar estara  mi red de seguridad llamado Except/catch que me protejera de la caida y igualmente estaran las felicitaciones alojadas en el finally, no por haber volado, pero si por tener la valentia de saltar.
