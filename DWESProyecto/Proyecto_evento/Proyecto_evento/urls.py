"""
URL configuration for Proyecto_evento project.

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
from tkinter.font import names

from django.contrib import admin
from eventoapp.views import listarEventos
from eventoapp.views import eventosPorNombre
from eventoapp.views import crearEvento
from eventoapp.views import actualizarEvento
from eventoapp.views import EliminarEvento
from eventoapp.views import ListarReservaUsuario
from eventoapp.views import CrearReserva
from eventoapp.views import EliminarReserva
from eventoapp.views import ListarComentarios
from eventoapp.views import ListarComentariosEvento
from eventoapp.views import CrearComentario
from eventoapp.views import Resgistrar
from django.urls import path
from eventoapp import views
from rest_framework.authtoken.views import ObtainAuthToken
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('inicio/', views.eventos_html, name='eventos_html'),
    path('reservas/',views.reservas, name='reservas_html'),
    #----------------------------------------------------------------
    path('lista_evento/',listarEventos.as_view(),name="listarEvento"),
    path('evento/',eventosPorNombre.as_view(), name="listarEventosPorNombre"),
    #path('eventos/',views.eventos_por_paginas),
    path('crear_evento/',crearEvento.as_view(), name="crearEvento"),
    path('actuazalizar_evento/<int:id>/',actualizarEvento.as_view(), name="Actualizar evento"),
    path('eliminar_evento/<int:id>/', EliminarEvento.as_view(), name="Eliminar evento"),
    path('listar_reserva/<int:id>/',ListarReservaUsuario.as_view(), name="Listar Reservas"),
    path('crear_reserva/',CrearReserva.as_view(), name="crear Reserva "),
    path('eliminar_reserva/<int:id>/',EliminarReserva.as_view(), name="EliminarReserva"),
    path('listarComentarios/',ListarComentarios.as_view(), name="ListarComentarios"),
    path('listar_comentarios_evento/<int:id>/',ListarComentariosEvento.as_view(), name= "ListarComentarioEvento"),
    path('crear_comentario/',CrearComentario.as_view(), name="crear comentario"),
    path('login/', ObtainAuthToken.as_view(), name='api_token_auth'),
    path('registrar/',Resgistrar.as_view(),name="Resguistrar"),
]

schema_view = get_schema_view(
    openapi.Info(
        title="API EventoApp",
        default_version="v1",
        description="Esta es una api que devuelve peticiones de Eventos ",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]