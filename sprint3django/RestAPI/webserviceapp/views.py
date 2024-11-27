from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Tlibros
from .models import Tcomentarios

# Create your views here.
def pagina_de_prueba(request):
        return HttpResponse("<h1> Hola caracola </h1>")

#Funcion que devuelve los libros (GET)
def devolver_libros(request):
        #Hace la peticion a la base de datos y recoge todos los libros 
        lista = Tlibros.objects.all()
        #creamos una variable donde guardaremos toda la informacion 
        respuesta_final = []
        for fila_sql in lista:
                #creamos el json 
                diccionario = {}
                diccionario['id'] =fila_sql.id
                diccionario['nombre'] = fila_sql.nombre
                diccionario['url_img']= fila_sql.url_imagen
                diccionario['autor'] = fila_sql.autor
                diccionario['numpaginas'] = fila_sql.numpaginas
                #añadimos el json al dicionario
                respuesta_final.append(diccionario)
        #devolvemos al usuario el json 
        return JsonResponse(respuesta_final, safe=False)

#Funcion que devuelve un libro por id (GET)
def devolver_libro_por_id(request,id_solicitado):
    #Nos devuelve el libro filtrado por id de la base de datos 
    libro = Tlibros.objects.get(id = id_solicitado)
    #hace un join en la base de datos de las tablas(Tlibros y Tcomentarios) que recoge los comentarios por el id solicitado
    comentarios = libro.tcomentarios_set.all()
    #creamos una lista que tendra un los comentarios 
    lista_comentarios =[]
    #recorre fila por fila la columna de la peticion a la base de datos 
    for fila_comentario_sql in comentarios:
           diccionario = {}
           diccionario['id'] = fila_comentario_sql.id
           diccionario['comentario'] = fila_comentario_sql.comentario
           lista_comentarios.append(diccionario)
    #recogemos los datos del libro 
    resultado = {
            'id': libro.id,
            'nombre': libro.nombre,
            'url_imagen': libro.url_imagen,
            'autor': libro.autor,
            'numpaginas': libro.numpaginas,
            'Comentario': lista_comentarios
    }
    #devolvemos el libro con los comentarios de ese libro 
    return JsonResponse(resultado,json_dumps_params={'ensure_ascii':False})

#desavilita la poteccion de django
@csrf_exempt
#funcion que insertara un comentario a la base de datos (POST)
def guardar_comentario(request,libro_id):
       #Verifica si el metodo es un post 
       if request.method != 'POST':
              return None
       print (request.body)
       json_peticion = json.loads(request.body)
       comentario = Tcomentarios()
       comentario.comentario= json_peticion['nuevo_comentario']
       comentario.libroid =Tlibros.objects.get(id = libro_id)
       comentario.save()
       return JsonResponse({"status": "ok"})