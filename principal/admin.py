#se crea este archivo
#encoding:utf-8
from principal.models import Provincia, Lugar, Danza,  Artesania, Meses, Evento, Lugares_turisticos, Tipo_lugar_turistico, Galeria_turismo, Galeria_danzas, Galeria_artesanias, Galeria_eventos
from django.contrib import admin
admin.site.register(Provincia)
admin.site.register(Lugar)
admin.site.register(Danza)
admin.site.register(Meses)
admin.site.register(Artesania)
admin.site.register(Evento)
admin.site.register(Tipo_lugar_turistico)
admin.site.register(Lugares_turisticos)
admin.site.register(Galeria_turismo)
admin.site.register(Galeria_danzas)
admin.site.register(Galeria_artesanias)
admin.site.register(Galeria_eventos)