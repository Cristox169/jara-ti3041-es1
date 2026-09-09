from django.test import TestCase
from django.urls import reverse

from .imagenes_productos import PRODUCT_IMAGE_DATA
from .views import PRODUCTOS


class CatalogoViewsTests(TestCase):
    def test_catalogo_contiene_cuarenta_productos(self):
        self.assertEqual(len(PRODUCTOS), 40)
        self.assertEqual(len(PRODUCT_IMAGE_DATA), 40)
        self.assertEqual(len(set(PRODUCT_IMAGE_DATA.values())), 40)
        self.assertTrue(
            all(image.startswith('data:image/webp;base64,') for image in PRODUCT_IMAGE_DATA.values())
        )

    def test_listado_responde_y_muestra_todos_los_productos(self):
        response = self.client.get(reverse('catalogo:lista'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['productos']), 40)
        self.assertContains(response, 'Taladro percutor 13 mm')
        self.assertContains(response, 'Flexible agua HI-HI 40 cm')

    def test_detalle_busca_producto_por_id(self):
        response = self.client.get(reverse('catalogo:detalle', args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Taladro percutor 13 mm')

    def test_detalle_inexistente_retorna_404(self):
        response = self.client.get(reverse('catalogo:detalle', args=[999]))

        self.assertEqual(response.status_code, 404)

    def test_resumen_se_calcula_en_la_vista(self):
        response = self.client.get(reverse('catalogo:lista'))

        self.assertEqual(response.context['resumen']['total'], 40)
        self.assertEqual(response.context['resumen']['con_stock'], 34)
        self.assertEqual(response.context['resumen']['sin_stock'], 6)
        self.assertEqual(response.context['resumen']['categorias'], 8)

    def test_template_destaca_productos_sin_stock(self):
        response = self.client.get(reverse('catalogo:lista'))

        self.assertContains(response, 'product-card is-unavailable', count=6)
        self.assertContains(response, 'Agotado', count=6)

    def test_punto_venta_muestra_los_cuarenta_productos(self):
        response = self.client.get(reverse('catalogo:punto_venta'))
        content = response.content.decode()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['productos']), 40)
        self.assertContains(response, 'data-pos-product', count=40)
        self.assertContains(response, 'Carro de compra')
        self.assertEqual(content.count('src="data:image/webp;base64,'), 40)
        self.assertNotContains(response, 'Construye la compra.')

    def test_punto_venta_incluye_controles_y_comprobante(self):
        response = self.client.get(reverse('catalogo:punto_venta'))

        self.assertContains(response, 'pos-search')
        self.assertContains(response, 'Finalizar compra')
        self.assertContains(response, 'receipt-paper')
