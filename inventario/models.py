from django.db import models

# Create your models here.

# Modelo 1: Categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

# Modelo 2: Proveedor
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=50)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

# Modelo 3: Fruta
class Fruta(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='frutas')
    proveedores = models.ManyToManyField(Proveedor, through='Suministro')
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

# Modelo 4: Suministro (Tabla intermedia)
class Suministro(models.Model):
    fruta = models.ForeignKey(Fruta, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_suministro = models.DateField()
    precio_unitario = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Suministro de {self.fruta.nombre} por {self.proveedor.nombre}"

# Modelo 5: Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

# Modelo 6: Pedido
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('Enviado', 'Enviado'), ('Entregado', 'Entregado')])
    total = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Pedido {self.id} de {self.cliente.nombre}"

# Modelo 7: DetallePedido
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    fruta = models.ForeignKey(Fruta, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Detalle de {self.pedido} - {self.fruta.nombre}"

# Modelo 8: Empleado
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    puesto = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Modelo 9: DetalleInventario
class DetalleInventario(models.Model):
    fruta = models.OneToOneField(Fruta, on_delete=models.CASCADE)
    cantidad_disponible = models.IntegerField()
    ubicacion = models.CharField(max_length=100)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inventario de {self.fruta.nombre}"

# Modelo 10: Descuento
class Descuento(models.Model):
    fruta = models.ForeignKey(Fruta, on_delete=models.CASCADE)
    porcentaje = models.DecimalField(max_digits=4, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"{self.porcentaje}% de descuento en {self.fruta.nombre}"
