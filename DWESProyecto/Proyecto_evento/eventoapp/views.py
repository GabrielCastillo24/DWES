from django.http import JsonResponse
from django.shortcuts import render
from .models import  Evento
from .models import *


# Create your views here.
def listar_evento (request):
    eventos = Evento.objects.all()
    lista = [{
        "titulo":event.titulo,
        "descripcion": event.descripcion,
        "fechaYhora": event.fechaYhora,
        "capacidadAsistente": event.capacidadAsistente,
        "urlImg":event.urlImg
        }

             for event in eventos]
    """
    for valor in eventos:
        evento ={
           "titulo": valor.titulo,
            "descripcion": valor.descripcion,
            "fecha": valor.fechaYhora,
            "capacidadDeAsistentes": valor.capacidadAsistente,
            "urlimg": valor.urlImg,
        }
        lista.append(evento)"""
    return JsonResponse(lista,safe=False)

