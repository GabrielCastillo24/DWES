from symtable import Class
from unittest.mock import DEFAULT

from django.template.defaulttags import comment
from django.contrib.auth.models import AbstractUser
from django.db import models

#Modelo de usuario
class Usuario(AbstractUser):
    #Tipo de usuarios que puede haber 
    TIPO_USER =[
        ("organizador","Organizador"),
        ("participante","Participante")
    ]
    rol = models.CharField(max_length=100, choices=TIPO_USER)
    biografia = models.CharField(max_length=500, null=True)
    def __str__(self):
        return  self.username,self.rol

#modelo de evento
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    fechaYhora = models.DateTimeField()
    capacidadAsistente = models.IntegerField()
    urlImg = models.CharField(max_length=400)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo,self.fechaYhora

#Modelo de Reserva
class Reserva(models.Model):
    #Donde guardamos los posibles estados que puede tener una reserva
    ESTADO_RESERVA=[
        ("pendiente","Pendiente"),
        ("confirmada","Confirmada"),
        ("cancelada","Cancelada")
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    numeroEntradas = models.IntegerField()
    estado = models.CharField(max_length=100, choices=ESTADO_RESERVA, default="pendiente")
    def __str__(self):
        return self.usuario, self.estado

class Comentario(models.Model):
    textComentario = models.CharField(max_length=500)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fechaComentario = models.DateField()
    def __str__(self):
        return self.textComentario
