from django.urls import path

from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.lista_productos, name='lista'),
    path('punto-de-venta/', views.punto_venta, name='punto_venta'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle'),
]
