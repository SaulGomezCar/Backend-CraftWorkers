from django.contrib import admin

from .models import Perfil, Trabajador, Categoria

# Register your models here.
admin.site.register(Perfil)
admin.site.register(Trabajador)
admin.site.register(Categoria)
