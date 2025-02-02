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
from django.contrib import admin
from django.urls import path
from eventoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista_evento/',views.listar_evento),
    path('evento/',views.eventos_por_nombre),
    path('eventos/',views.eventos_por_paginas),
    path('crear_evento/',views.crear_evento),
    path('actuazalizar_evento/<int:id>/',views.actuazalizar_evento),
    path('eliminar_evento/<int:id>/', views.eliminar_evento),
    path('listar_reserva/<int:id>/',views.listar_reserva_usuario),
    path('crear_reserva/',views.crear_reserva),
    path('eliminar_reserva/<int:id>/',views.eliminar_reserva),
    path('listar_comentarios_evento/<int:id>/',views.listar_comentarios_evento),
    path('crear_comentario/',views.crear_comentario),
    path('login/',views.login),
    path('registrar/',views.registrar),
]
