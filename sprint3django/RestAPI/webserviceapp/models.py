# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tcomentarios(models.Model):
    comentario = models.CharField(max_length=2000, blank=True, null=True)
    usuarioid = models.ForeignKey('Tusuario', models.DO_NOTHING, db_column='usuarioId', blank=True, null=True)  # Field name made lowercase.
    libroid = models.ForeignKey('Tlibros', models.DO_NOTHING, db_column='libroId', blank=True, null=True)  # Field name made lowercase.
    fechacomentario = models.DateField(db_column='fechaComentario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tCOMENTARIOS'


class Tlibros(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    url_imagen = models.CharField(max_length=400, blank=True, null=True)
    autor = models.CharField(max_length=50, blank=True, null=True)
    numpaginas = models.IntegerField(db_column='numPaginas', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tLIBROS'


class Tusuario(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(unique=True, max_length=200, blank=True, null=True)
    contraseña = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tUSUARIO'
