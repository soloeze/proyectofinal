from django.contrib import admin
from .models import Tarea, Personas_del_equipo, Contacto
# Register your models here.
admin.site.register(Tarea)
admin.site.register(Personas_del_equipo)
admin.site.register(Contacto)