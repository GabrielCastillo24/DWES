"""
URL configuration for RestAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webserviceapp import views

#Los path de las url que se van a hacer las peticiones 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test',views.pagina_de_prueba),
    path('libros',views.devolver_libros),
    path('libros/<int:id_solicitado>',views.devolver_libro_por_id),
    path('libros/<int:libro_id>/comentarios',views.guardar_comentario)
]
