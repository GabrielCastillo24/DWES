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
        "idEvento": event.id,
        "descripcion": event.descripcion,
        "fechaYhora": event.fechaYhora,
        "capacidadAsistente": event.capacidadAsistente,
        "urlImg":event.urlImg,
        "usuario": event.usuario.id
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
        info = json.loads(request.body)
        nombreRequest = info["nombreUser"]
        #Filtra en la base de datos para que me busque el usuario
        bucarUsuario = Usuario.objects.get(username=nombreRequest)
        #Verifica si el usaurio es un organizador
        if bucarUsuario.rol == "organizador":
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
            return JsonResponse({"Mensaje": "No se pudo crear el Evento "})

@csrf_exempt
def actuazalizar_evento(request, id):
    #verifca que metodo es
    if request.method in ["PUT","PATCH"]:
        info = json.loads(request.body)
        #toma el ide del usuario
        idUser = info.get("iduser","")
        #toma el evento
        evento = Evento.objects.get(id=id)
        #toma al usuario
        usuario = Usuario.objects.get(id=idUser)
        #si el usuario es el mismo que el que tiene el evento actualaiza el evento
        if usuario == evento.usuario:
            evento.titulo = info.get("titulo",evento.titulo)
            evento.descripcion = info.get("descripcion",evento.descripcion)
            evento.fechaYhora = info.get("fechaYhora",evento.fechaYhora)
            evento.capacidadAsistente = info.get("capacidadAsistente",evento.capacidadAsistente)
            evento.urlImg = info.get("urlImg",evento.urlImg)
            evento.save()
            return JsonResponse({"mensaje": "Evento actualizado"})
        else:
            return  JsonResponse({"mensaje": "No se pudo actualizar"})

@csrf_exempt
def eliminar_evento(request,id):
    info = json.loads(request.body)
    #toma el rol que se le envia por json
    rol_dicc = info["rol"]
    #verifica si es organizador y si es borra el evento
    if request.method == "DELETE" and rol_dicc == "organizador":
        print(info)
        print(rol_dicc)
        evento = Evento.objects.get(id=id)
        evento.delete()
        return JsonResponse ({"Mensaje" : "Evento eliminado"})


def listar_reserva_usuario(request,id):
    #Toma el id del usuario
    usuario = Usuario.objects.get(id=id)
    #devuelve la reserva que pertenzcan a ese usuario
    reservas = Reserva.objects.select_related('usuario').filter(usuario=usuario)
    lista =[{
        "idreserva": reserv.id,
        "evento": reserv.evento.titulo,
        "idEvento": reserv.evento.id,
        "numeroEntradas": reserv.numeroEntradas,
        "estado": reserv.estado,
        "usuario": reserv.usuario.username,
        "iduser": reserv.usuario.id
        }
    for reserv in reservas]
    return JsonResponse(lista, safe=False)

@csrf_exempt
def crear_reserva(request):
    #verifica si es un POST
    if request.method == "POST":
        info = json.loads(request.body)
        nombreUsuario = info['nombre']
        nombreEvento = info['titulo']
        #toma el usaurio y el vento
        usuarioReserva = Usuario.objects.get(username=nombreUsuario)
        eventoReserva = Evento.objects.get(titulo=nombreEvento)
        #crea la reserva del suario y el evento que tomo
        reserva = Reserva.objects.create(
            usuario= usuarioReserva,
            evento = eventoReserva,
            numeroEntradas=info['numeroEntradas'],
            estado = info['estado']
        )
        return JsonResponse({"id": reserva.id, "mensaje": "La reserva a sido creada exitosamente"})

@csrf_exempt
def eliminar_reserva(request,id):
    #toma el evento por el id que se le pasa por parametro
    reserva = Reserva.objects.get(id=id)
    info = json.loads(request.body)

    idUser = info['iduser']

    usuario = Usuario.objects.get(id= idUser)
    #verifica si el usuario que se le pasa es el mismo de la reserva y si lo es lo borra
    if reserva.usuario == usuario:
        reserva.delete()
        return  JsonResponse ({"id": reserva.id,"Mensaje" : "Reserva eliminado"})
    else:
        return JsonResponse({"Mensaje": "No se a podido eliminar la reserva"})

def listar_comentarios_evento(request,id):
    evento =  Evento.objects.get(id=id)
    #busca los comentarios que tiene el evento
    comentarios = Comentario.objects.select_related('evento').filter(evento=evento)
    #cuepor de la respuesta
    lista = [{
        "Comentario": comentario.textComentario,
        "fecha": comentario.fechaComentario,
        "idevento":comentario.evento.id,
        "evento": comentario.evento.titulo
    }
        for comentario in comentarios]

    return JsonResponse(lista, safe=False)

@csrf_exempt
def crear_comentario(request):
    info = json.loads(request.body)
    #toma los datos
    if info["sesion"] == "si":
        nombreUser = info["nombreUser"]
        nombreEvento = info["nombreEvento"]
        comentarioTxt = info["comentario"]
        fecha = info["fecha"]
        #toma el usuario y el evento al cual va ir dirijido el comentario
        usuario = Usuario.objects.get(username__iexact=nombreUser)
        evento = Evento.objects.get(titulo__iexact=nombreEvento)
        comentario = Comentario.objects.create(
            textComentario = comentarioTxt,
            usuario =usuario,
            evento = evento,
            fechaComentario =fecha
        )
        return JsonResponse({"id": comentario.id, "mensaje": "El Comentario se ha creado correctamente."})
    else:
        return JsonResponse({"Tienes que estar autenticado para hacer un comentario"})


@csrf_exempt
def login(request):
    info = json.loads(request.body)
    nombreUser = info.get("NombreUsuario", "")
    contraseña = info["Contraseña"]
    #verifica si el campo viene vacio
    if nombreUser == "":
        return JsonResponse({"mensaje":"El nombre de usuario esta bacio"})
    else:
        usuario = Usuario.objects.get(username=nombreUser)

        if usuario.password == contraseña:
            return JsonResponse({"mensaje":"Login correcto"})




@csrf_exempt
def registrar(request):
    info =  json.loads(request.body)
    nombreUsuario= info["NombreUsuario"]
    emailU = info["Email"]
    contarseña = info["Contraseña"]
    rol = "participante"
    biografia = info["biografia"]
    #verifica si no existe el usuario y si no existe deja crear el objeto 
    if Usuario.objects.filter(username=nombreUsuario).exists():
        return JsonResponse({"Mensaje": "No se puede crear el usuario"})
    else:
        usuario = Usuario.objects.create_user(
            username=nombreUsuario,
            email=emailU,
            password=contarseña,
            rol= rol,
            biografia=biografia
        )
        return JsonResponse({"Mensaje": "Te haz registrado correctamente "})


