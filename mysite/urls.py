from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventario.urls')),
]

# Configuración de manejadores de errores
handler404 = 'inventario.views.error_404'
handler500 = 'inventario.views.error_500'
handler403 = 'inventario.views.error_403'
handler400 = 'inventario.views.error_400'