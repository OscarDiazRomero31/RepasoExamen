# Generated by Django 5.1.2 on 2024-11-04 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=15)),
                ('puesto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=50)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Fruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frutas', to='inventario.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleInventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_disponible', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=100)),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('fruta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventario.fruta')),
            ],
        ),
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje', models.DecimalField(decimal_places=2, max_digits=4)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('fruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.fruta')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Enviado', 'Enviado'), ('Entregado', 'Entregado')], max_length=50)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='inventario.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.fruta')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='inventario.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Suministro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha_suministro', models.DateField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.fruta')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.proveedor')),
            ],
        ),
        migrations.AddField(
            model_name='fruta',
            name='proveedores',
            field=models.ManyToManyField(through='inventario.Suministro', to='inventario.proveedor'),
        ),
    ]