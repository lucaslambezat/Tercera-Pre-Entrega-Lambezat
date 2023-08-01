from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Creo un path por aplicación. Para que todas las rutas relacionadas a la aplicación las encuentre en un archivo.
    #Cada vez que encuentre una ruta que empiece por aplicación, busca esa ruta en este archivo. Dentro del paquete "aplicacion", el módulo "urls".
    path('aplicacion/', include('aplicacion.urls')),
]
