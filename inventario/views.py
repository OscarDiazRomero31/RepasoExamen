from django.shortcuts import render, get_object_or_404
from .models import Categoria, Proveedor, Fruta, Cliente, Pedido, DetallePedido, DetalleInventario, Descuento

# Índice para acceder a todas las URLs
def index(request):
    """Muestra el índice con enlaces a todas las funcionalidades."""
    return render(request, 'inventario/index.html')

# Vista para listar categorías
def categoria_list(request):
    """Muestra una lista de todas las categorías."""
    categorias = Categoria.objects.all()
    return render(request, 'inventario/categoria_list.html', {'categorias': categorias})

# Vista para listar proveedores
def proveedor_list(request):
    """Muestra una lista de todos los proveedores."""
    proveedores = Proveedor.objects.all()
    return render(request, 'inventario/proveedor_list.html', {'proveedores': proveedores})

# Vista para listar frutas
def fruta_list(request):
    """Muestra una lista de todas las frutas y sus categorías."""
    frutas = Fruta.objects.select_related('categoria').all()
    return render(request, 'inventario/fruta_list.html', {'frutas': frutas})

# Vista para listar clientes
def cliente_list(request):
    """Muestra una lista de todos los clientes."""
    clientes = Cliente.objects.all()
    return render(request, 'inventario/cliente_list.html', {'clientes': clientes})

# Vista para listar pedidos
def pedido_list(request):
    """Muestra una lista de todos los pedidos realizados por los clientes."""
    pedidos = Pedido.objects.select_related('cliente').all()
    return render(request, 'inventario/pedido_list.html', {'pedidos': pedidos})

# Vista para mostrar detalles del inventario
def inventario_detalle(request):
    """Muestra detalles del inventario para cada fruta."""
    inventario = DetalleInventario.objects.select_related('fruta').all()
    return render(request, 'inventario/inventario_detalle.html', {'inventario': inventario})

# Vista para listar descuentos en frutas
def descuento_list(request):
    """Muestra una lista de todos los descuentos en frutas."""
    descuentos = Descuento.objects.select_related('fruta').all()
    return render(request, 'inventario/descuento_list.html', {'descuentos': descuentos})

# Vista para detalles de un pedido específico
def detalle_pedido(request, pedido_id):
    """Muestra los detalles de un pedido, incluyendo cada fruta pedida y su cantidad."""
    pedido = get_object_or_404(Pedido, id=pedido_id)
    detalles = pedido.detalles.select_related('fruta').all()
    return render(request, 'inventario/detalle_pedido.html', {'pedido': pedido, 'detalles': detalles})

# Vista para filtrar frutas por categoría
def frutas_por_categoria(request, categoria_nombre):
    """Muestra una lista de frutas que pertenecen a una categoría específica."""
    categoria = get_object_or_404(Categoria, nombre=categoria_nombre)
    frutas = categoria.frutas.all()
    return render(request, 'inventario/frutas_por_categoria.html', {'categoria': categoria, 'frutas': frutas})

# Errores
def error_404(request, exception):
    """Página de error personalizada para error 404 - Página no encontrada."""
    return render(request, 'errors/404.html', status=404)

def error_500(request):
    """Página de error personalizada para error 500 - Error del servidor."""
    return render(request, 'errors/500.html', status=500)

def error_403(request, exception):
    """Página de error personalizada para error 403 - Acceso prohibido."""
    return render(request, 'errors/403.html', status=403)

def error_400(request, exception):
    """Página de error personalizada para error 400 - Solicitud incorrecta."""
    return render(request, 'errors/400.html', status=400)
