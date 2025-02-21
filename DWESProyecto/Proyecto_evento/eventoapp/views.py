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
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import render
from .models import *

class VerificarUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.rol == "organizador"


# Create your views here.



def login(request):
    return render(request, 'login.html')

def reservas(request):
    return render(request, 'reservas.html')

#Esto ya lo hace enlistar eventos
#def inicio(request):
#    return render(request, 'inicio.html')


#--------------------Vistas para html----------------------------------------

def eventos_html(request):
    eventos = Evento.objects.all()
    return render(request, 'inicio.html', {'eventos': eventos})


#----------------------------Postman--------------------------------

class listarEventos(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_description="Obtener lista de productos",
        responses={200: openapi.Response("Lista de productos")},
    )
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
    @swagger_auto_schema(
        operation_description="Lista eventos filtrados por título.",
        manual_parameters=[
            openapi.Parameter(
                'titulo', openapi.IN_QUERY,
                description="Filtrar eventos por título",
                type=openapi.TYPE_STRING
            ),
        ],responses={200: openapi.Response(description="Listar evento por nombre")})
    def get(self,request):
        titulo = request.GET.get("titulo","")
        evento = Evento.objects.filter(titulo=titulo)
        lista = [{"titulo": event.titulo,"Descripcion": event.descripcion ,"fecha y hora":event.fechaYhora}for event in evento]
        return Response({"datos":lista})

class eventosPorPaginas(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_description="Lista eventos paginados filtrados por título y ordenados por un campo específico.",
        manual_parameters=[
            openapi.Parameter(
                'titulo', openapi.IN_QUERY,
                description="Filtrar eventos por título",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'orden', openapi.IN_QUERY,description="Ordenar por un campo (ej: titulo, fechaYhora)",type=openapi.TYPE_STRING),
            openapi.Parameter(
                'limite', openapi.IN_QUERY, description="Cantidad de eventos por página",type=openapi.TYPE_INTEGER),
            openapi.Parameter(
                'pagina', openapi.IN_QUERY,description="Número de la página a consultar", type=openapi.TYPE_INTEGER),
        ],responses={200: openapi.Response(description="Listar evento por nombre")})
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

    @swagger_auto_schema(
        operation_description="Crea un nuevo evento si el usuario es organizador.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["nombreUser", "titulo", "descripcion", "fechaYhora", "capacidadAsistente", "urlImg"],
            properties={
                "nombreUser": openapi.Schema(type=openapi.TYPE_STRING, description="Nombre de usuario del creador"),
                "titulo": openapi.Schema(type=openapi.TYPE_STRING, description="Título del evento"),
                "descripcion": openapi.Schema(type=openapi.TYPE_STRING, description="Descripción del evento"),
                "fechaYhora": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME,
                                             description="Fecha y hora del evento (YYYY-MM-DDTHH:MM:SSZ)"),
                "capacidadAsistente": openapi.Schema(type=openapi.TYPE_INTEGER,
                                                     description="Capacidad máxima de asistentes"),
                "urlImg": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI,
                                         description="URL de la imagen del evento"),
            }
        ),responses={201: openapi.Response(description="Evento creado"),403: openapi.Response(description="No tienes permisos para crear eventos.")})
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

    @swagger_auto_schema(
        operation_description="Actualiza un evento si el usuario es el creador.",
        manual_parameters=[
            openapi.Parameter(
                'id', openapi.IN_PATH,
                description="ID del evento a actualizar",
                type=openapi.TYPE_INTEGER
            )
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["iduser"],
            properties={
                "iduser": openapi.Schema(type=openapi.TYPE_INTEGER,
                                         description="ID del usuario que intenta actualizar el evento"),
                "titulo": openapi.Schema(type=openapi.TYPE_STRING, description="Nuevo título del evento (opcional)"),
                "descripcion": openapi.Schema(type=openapi.TYPE_STRING,
                                              description="Nueva descripción del evento (opcional)"),
                "fechaYhora": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME,
                                             description="Nueva fecha y hora del evento (YYYY-MM-DDTHH:MM:SSZ) (opcional)"),
                "capacidadAsistente": openapi.Schema(type=openapi.TYPE_INTEGER,
                                                     description="Nueva capacidad de asistentes (opcional)"),
                "urlImg": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI,
                                         description="Nueva URL de la imagen del evento (opcional)"),
            }
        ),responses={201: openapi.Response(description="Evento actualizado")})
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
    @swagger_auto_schema(
        operation_description="Elimina un evento por su ID.",
        manual_parameters=[
            openapi.Parameter(
                'id', openapi.IN_PATH,
                description="ID del evento a eliminar",
                type=openapi.TYPE_INTEGER
            )
        ],responses={201: openapi.Response(description="Evento eliminado")})
    def delete(self,request,id):
        #verifica si es organizador y si es borra el evento
        if request.method == "DELETE":
            evento = Evento.objects.get(id=id)
            evento.delete()
            return Response ({"Mensaje" : "Evento eliminado"})

class ListarReservaUsuario(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Lista todas las reservas realizadas por un usuario específico.",
        manual_parameters=[
            openapi.Parameter(
                'id', openapi.IN_PATH,
                description="ID del usuario cuyas reservas se listarán",
                type=openapi.TYPE_INTEGER
            )
        ],responses={201: openapi.Response(description="lista reservas de usuario ")})
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
    @swagger_auto_schema(
        operation_description="Crea una nueva reserva para un usuario en un evento.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["nombre", "titulo", "numeroEntradas", "estado"],
            properties={
                "nombre": openapi.Schema(type=openapi.TYPE_STRING, description="Nombre de usuario que realiza la reserva"),
                "titulo": openapi.Schema(type=openapi.TYPE_STRING, description="Título del evento a reservar"),
                "numeroEntradas": openapi.Schema(type=openapi.TYPE_INTEGER, description="Número de entradas reservadas"),
                "estado": openapi.Schema(type=openapi.TYPE_STRING, description="Estado de la reserva (ejemplo: Confirmada, Pendiente, Cancelada)")
            }
        ),responses={201: openapi.Response(description="Crear reserva")})
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
    @swagger_auto_schema(
        operation_description="Elimina una reserva si el usuario que la creó la solicita.",
        manual_parameters=[
            openapi.Parameter(
                'id', openapi.IN_PATH,
                description="ID de la reserva a eliminar",
                type=openapi.TYPE_INTEGER
            )
        ],responses={201: openapi.Response(description="Eliminar reserva")})
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
    @swagger_auto_schema(
        operation_description="Obtener lista de Comentario",
        responses={200: openapi.Response("Comentarios")},
    )
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

        @swagger_auto_schema(
            operation_description="Lista todos los comentarios de un evento específico.",
            manual_parameters=[
                openapi.Parameter(
                    'id', openapi.IN_PATH,
                    description="ID del evento cuyos comentarios se listarán",
                    type=openapi.TYPE_INTEGER
                )
            ],responses={200: openapi.Response("Comentarios de eventos")},)
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
    @swagger_auto_schema(
        operation_description="Crea un comentario en un evento específico.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["nombreUser", "nombreEvento", "comentario", "fecha"],
            properties={
                "nombreUser": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Nombre del usuario que realiza el comentario"
                ),
                "nombreEvento": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Título del evento al que se dirige el comentario"
                ),
                "comentario": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Texto del comentario"
                ),
                "fecha": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format="date",
                    description="Fecha del comentario (YYYY-MM-DD)"
                ),
            }
        ),responses={200: openapi.Response("Crear comentario")},)
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
    @swagger_auto_schema(
        operation_description="Registra un nuevo usuario con el rol de participante.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["NombreUsuario", "Email", "Contraseña", "biografia"],
            properties={
                "NombreUsuario": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Nombre de usuario"
                ),
                "Email": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format="email",
                    description="Correo electrónico del usuario"
                ),
                "Contraseña": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Contraseña del usuario"
                ),
                "biografia": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Biografía del usuario"
                ),
            }
        ),responses={200: openapi.Response("Reguistrado")},)

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
            return Response({"Mensaje": "Te haz registrado correctamente uwu"})


