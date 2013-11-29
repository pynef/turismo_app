#encoding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','principal.views.base'),
    url(r'^base/$','principal.views.base'),
    url(r'^Mas/$','principal.views.mas'),
    #lugares turisticos
    url(r'^Lugares/$','principal.views.detalle'),
    url(r'^Lugares/(?P<lugares>\d+)/$','principal.views.lista_lugares'),
    url(r'^Lugar/(?P<provincia>\d+)/$','principal.views.vista_lugar'),
    url(r'^Lugar/(?P<sitio>\d+)/TipoDeLugar/(?P<tipo_lugar>\d+)/$','principal.views.lugares_turisticos'),
    url(r'^Lugar_Turistico/(?P<id>\d+)/$','principal.views.lugar_turistico'),
    url(r'^MapaTuristica/(?P<id>\d+)/$','principal.views.mapa_turistica'),
    url(r'^GaleriaTuristica/(?P<id>\d+)/$','principal.views.galeria_turistica'),
    #rutas
    url(r'^Rutas/$','principal.views.ruta_detalle'),
    url(r'^Rutas/(?P<lugares>\d+)/$','principal.views.ruta_lugares'),
    url(r'^Ruta/(?P<provincia>\d+)/$','principal.views.vista_ruta'),
    url(r'^Ruta/(?P<sitio>\d+)/TipoDeLugar/(?P<tipo_lugar>\d+)/$','principal.views.rutas_turisticos'),
    url(r'^Ruta_llegada/(?P<id>\d+)/$','principal.views.ruta_turistico'),
    #Artesania
    url(r'^Artesanias/$','principal.views.detalle_artesania'),
    url(r'^Artesanias/(?P<lugares>\d+)/$','principal.views.lista_artesania'),
    url(r'^Artesania/(?P<provincia>\d+)/$','principal.views.vista_artesania'),
    url(r'^Artesania/(?P<sitio>\d+)/TipoDeLugar/(?P<tipo_lugar>\d+)/$','principal.views.lugares_artesanias'),
    url(r'^Artesania_Turistico/(?P<id>\d+)/$','principal.views.lugar_artesania'),
    url(r'^MapaArtesania/(?P<id>\d+)/$','principal.views.mapa_artesania'),
    url(r'^GaleriaArtesania/(?P<id>\d+)/$','principal.views.galeria_artesania'),
    #DanzasTipicas
    url(r'^DanzasTipicas/$','principal.views.detalle_danza'),
    url(r'^DanzasTipicas/(?P<lugares>\d+)/$','principal.views.lista_danza'),
    url(r'^DanzaTipica/(?P<provincia>\d+)/$','principal.views.vista_danza'),
    url(r'^DanzaTipica/(?P<sitio>\d+)/TipoDeLugar/(?P<tipo_lugar>\d+)/$','principal.views.lugares_danzas'),
    url(r'^DanzaTipica_Turistico/(?P<id>\d+)/$','principal.views.lugar_danza'),
    url(r'^MapaDanzaTipica/(?P<id>\d+)/$','principal.views.mapa_danza'),
    url(r'^GaleriaDanzaTipica/(?P<id>\d+)/$','principal.views.galeria_danza'),
    #Eventos
    #url(r'^EventosMeses/$','principal.views.meses'),
    url(r'^Eventos/$','principal.views.detalle_danza'),
    url(r'^Eventos/(?P<lugares>\d+)/$','principal.views.lista_evento'),
    url(r'^Evento/(?P<provincia>\d+)/$','principal.views.vista_evento'),
    url(r'^Meses/Evento/(?P<sitio>\d+)/TipoDeLugar/(?P<tipo_lugar>\d+)/$','principal.views.meses'),
    url(r'^Evento/(?P<sitio>\d+)/TipoDeLugar/(?P<tipo_lugar>\d+)/Mes/(?P<mes>\d+)/$','principal.views.lugares_eventos'),
    url(r'^Evento_Turistico/(?P<id>\d+)/$','principal.views.lugar_evento'),
    url(r'^MapaEvento/(?P<id>\d+)/$','principal.views.mapa_evento'),
    url(r'^GaleriaEvento/(?P<id>\d+)/$','principal.views.galeria_evento'),
    #default
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
    			{'document_root':settings.MEDIA_ROOT,}
    	),

)
