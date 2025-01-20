from django.contrib import admin
from.models import Usuario
from.models import Evento
from.models import Reserva
from.models import Comentario

# Register your models here.
# "Vista personalizada tabla evento"
class EventoAdmin (admin.ModelAdmin):
    list_display = ('titulo','usuario','fechaYhora')
    search_fields = ('titulo','fechaYhora')
    list_filter = ('titulo',)

#invocación_personalizado
admin.site.register(Evento, EventoAdmin)
#invocacion vistas genéricas
admin.site.register(Usuario)
admin.site.register(Reserva)
admin.site.register(Comentario)
