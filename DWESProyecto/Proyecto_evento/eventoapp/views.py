from itertools import product
from pydoc import describe
from rest_framework.permissions import IsAuthenticated

from django.core.paginator import Paginator
from rest_framework.response import Response
from django.db.models.fields import return_None
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.permissions import BasePermission

from rest_framework.views import APIView


from .models import *

class VerificarUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.rol == "organizador"


# Create your views here.

class listarEventos(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
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
        return Response ({"datos": lista})

class eventosPorNombre(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        titulo = request.GET.get("titulo","")
        evento = Evento.objects.filter(titulo=titulo)
        lista = [{"titulo": event.titulo,"Descripcion": event.descripcion ,"fecha y hora":event.fechaYhora}for event in evento]
        return Response({"datos":lista})

class eventosPorPaginas(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        titulo = request.GET.get("titulo","")
        orden  = request.GET.get("orden","titulo")
        limite = int(request.GET.get("limite",10))
        pagina = int(request.GET.get("pagina",1))

        evento = Evento.objects.filter(titulo=titulo).order_by(orden)

        paginator =Paginator(evento,limite)

        try:
            evento_pagina = paginator.page(pagina)
        except Exception as e:
            return  Response({"error":str(e)}, status=400)

        lista = {
            "count": paginator.count,
            "total_paginas":paginator.num_pages,
            "paginaActual":pagina,
            "Siguiente": pagina + 1 if evento_pagina.has_next() else None,
            "Anterior": pagina - 1 if evento_pagina.has_previous() else None,
            "resultado": [{"titulo": event.titulo, "Descripcion": event.descripcion, "fecha y hora": event.fechaYhora} for event in evento_pagina]
        }
        return Response({"datos":lista})

#Crear Evento
class crearEvento(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        #Verifica si el metodo es POST
        if request.method == "POST":
            #Toma el nombre de usuario del creador del evento
            info = request.data
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
                return Response({"id":evento.id, "Mensaje": "Evento creado exitosamente"})
            else:
                #No se pudo crear el evento
                return Response({"Mensaje": "No se pudo crear el Evento "})

class actualizarEvento(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request, id):
        #verifca que metodo es
        if request.method in ["PUT","PATCH"]:
            info = request.data
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
                return Response({"mensaje": "Evento actualizado"})
            else:
                return  Response({"mensaje": "No se pudo actualizar"})

class EliminarEvento(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self,request,id):
        #verifica si es organizador y si es borra el evento
        if request.method == "DELETE":
            evento = Evento.objects.get(id=id)
            evento.delete()
            return Response ({"Mensaje" : "Evento eliminado"})

class ListarReservaUsuario(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,id):
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
        return Response({"Datos": lista})

class CrearReserva(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        #verifica si es un POST
        if request.method == "POST":
            info = request.data
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
            return Response({"id": reserva.id, "mensaje": "La reserva a sido creada exitosamente"})

class EliminarReserva(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self,request,id):
        #toma el evento por el id que se le pasa por parametro
        reserva = Reserva.objects.get(id=id)

        info = request.data
        idUser = info['iduser']

        usuario = Usuario.objects.get(id= idUser)
        #verifica si el usuario que se le pasa es el mismo de la reserva y si lo es lo borra
        if reserva.usuario == usuario:
            reserva.delete()
            return  Response ({"id": reserva.id,"Mensaje" : "Reserva eliminado"})
        else:
            return Response({"Mensaje": "No se a podido eliminar la reserva"})

class ListarComentarios(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        Comentarios = Comentario.objects.all()
        lista = [{
            "idComentario": comentario.id,
            "Comentario": comentario.textComentario,
            "fecha": comentario.fechaComentario,
            "idevento": comentario.evento.id,
            "evento": comentario.evento.titulo,
            "Usuario": comentario.usuario.username,
            "IdUser": comentario.usuario.id
        }
            for comentario in Comentarios]
        return Response({"Datos": lista})


class ListarComentariosEvento(APIView):
        permission_classes = [IsAuthenticated]
        def get(self,request,id):
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

            return Response({"Datos": lista})


class CrearComentario(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        info = request.data
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


#class login(APIView):
#    def pot(self,request):
#        info = request.data
#        nombreUser = info.get("NombreUsuario", "")
#        contraseña = info["Contraseña"]
#        #verifica si el campo viene vacio
#        if nombreUser == "":
#            return JsonResponse({"mensaje":"El nombre de usuario esta bacio"})
#        else:
#            usuario = Usuario.objects.get(username=nombreUser)
#
#           if usuario.password == contraseña:
#                return Response({"mensaje":"Login correcto"})




class Resgistrar(APIView):
    def post(self,request):
        info = request.data
        nombreUsuario= info["NombreUsuario"]
        emailU = info["Email"]
        contarseña = info["Contraseña"]
        rol = "participante"
        biografia = info["biografia"]
        #verifica si no existe el usuario y si no existe deja crear el objeto
        if Usuario.objects.filter(username=nombreUsuario).exists():
            return Response({"Mensaje": "No se puede crear el usuario"})
        else:
            usuario = Usuario.objects.create_user(
                username=nombreUsuario,
                email=emailU,
                password=contarseña,
                rol= rol,
                biografia=biografia
            )
            return Response({"Mensaje": "Te haz registrado correctamente "})


