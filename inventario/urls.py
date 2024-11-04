from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('', views.index, name='index'),  # Índice de todas las URLs
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('proveedores/', views.proveedor_list, name='proveedor_list'),
    path('frutas/', views.fruta_list, name='fruta_list'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('pedidos/', views.pedido_list, name='pedido_list'),
    path('inventario/', views.inventario_detalle, name='inventario_detalle'),
    path('descuentos/', views.descuento_list, name='descuento_list'),
    path('pedido/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
    path('frutas/categoria/<str:categoria_nombre>/', views.frutas_por_categoria, name='frutas_por_categoria'),
]
