from itertools import product
from pydoc import describe

from django.core.paginator import Paginator
from django.db.models.fields import return_None
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
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

def eventos_por_nombre(request):
    titulo = request.GET.get("titulo","")
    evento = Evento.objects.filter(titulo=titulo)
    lista = [{"titulo": event.titulo,"Descripcion": event.descripcion ,"fecha y hora":event.fechaYhora}for event in evento]
    return JsonResponse(lista,safe=False)


def eventos_por_paginas(request):
    titulo = request.GET.get("titulo","")
    orden  = request.GET.get("orden","titulo")
    limite = int(request.GET.get("limite",10))
    pagina = int(request.GET.get("pagina",1))

    evento = Evento.objects.filter(titulo=titulo).order_by(orden)

    paginator =Paginator(evento,limite)

    try:
        evento_pagina = paginator.page(pagina)
    except Exception as e:
        return  JsonResponse({"error":str(e)}, status=400)

    lista = {
        "count": paginator.count,
        "total_paginas":paginator.num_pages,
        "paginaActual":pagina,
        "Siguiente": pagina + 1 if evento_pagina.has_next() else None,
        "Anterior": pagina - 1 if evento_pagina.has_previous() else None,
        "resultado": [{"titulo": event.titulo, "Descripcion": event.descripcion, "fecha y hora": event.fechaYhora} for event in evento_pagina]
    }
    return JsonResponse(lista, safe=False)

#Crear Evento
@csrf_exempt
def crear_evento(request):
    #Verifica si el metodo es POST
    if request.method == "POST":
        #Toma el nombre de usuario del creador del evento
        nombreRequest = request.GET.get("nombre","")
        #Filtra en la base de datos para que me busque el usuario
        bucarUsuario = Usuario.objects.get(username=nombreRequest)
        #Verifica si el usaurio es un organizador
        if bucarUsuario.rol == "organizador":
            #Cuerpor del evento que se va a crear
            info = json.loads(request.body)
            #Creamos el evento
            evento = Evento.objects.create(
                titulo = info["titulo"],
                descripcion =info["descripcion"],
                fechaYhora = info["fechaYhora"],
                capacidadAsistente =info["capacidadAsistente"],
                urlImg= info["urlImg"],
                usuario=bucarUsuario
            )
            #Creado el evento
            return JsonResponse({"id":evento.id, "Mensaje": "Evento creado exitosamente"})
        else:
            #No se pudo crear el evento
            return JsonResponse({"Mensaje": "No se pudo crear el objeto "})

@csrf_exempt
def actuazalizar_evento(request, id):
    if request.method in ["PUT","PACHT"]:
        info = json.loads(request.body)
        rol = info.get("rol","")
        if rol == "organizador":
            evento = Evento.objects.get(id=id)
            evento.titulo = info.get("titulo",evento.titulo)
            evento.descripcion = info.get("descripcion",evento.descripcion)
            evento.fechaYhora = info.get("fechaYhora",evento.fechaYhora)
            evento.capacidadAsistente = info.get("capacidadAsistente",evento.capacidadAsistente)
            evento.urlImg = info.get("urlImg",evento.urlImg)
            evento.save()
        return JsonResponse({"mensaje": "Producto actualizado"})

