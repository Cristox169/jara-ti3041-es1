from django.test import TestCase
from django.urls import reverse

from .views import PRODUCTOS


class CatalogoViewsTests(TestCase):
    def test_catalogo_contiene_cuarenta_productos(self):
        self.assertEqual(len(PRODUCTOS), 40)

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
