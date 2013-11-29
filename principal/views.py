# Create your views here.
from principal.models import Lugar, Provincia, Tipo_lugar_turistico, Lugares_turisticos,Artesania,Danza,Meses,Evento
#Provincia, Lugar, Actividad, ParqueEmblematico, LugarNatural, LugarAtractivo, LugarArqueologico, Danza, Museo, Artesania, Evento
#from principal.forms import LugarForm, ProvinciaForm, LugarNaturalForm, LugarArqueologicoForm, LugarAtractivoForm, ParqueEmblematicoForm, ArtesaniaForm, MuseoForm, ActividadForm, DanzaForm, EventoForm
#from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext

def base(request):
	return render_to_response('base.html', context_instance=RequestContext(request))

def mas(request):
	return render_to_response('mas.html', context_instance=RequestContext(request))

def mas_detalle(request):
	lugares = Lugar.objects.all()
	return render_to_response('mas_detalle.html', {'lugares':lugares}, context_instance=RequestContext(request))

def detalle(request):
	lugares = Lugar.objects.all()
	return render_to_response('detalle.html',{'lugares':lugares}, context_instance=RequestContext(request))

def lista_lugares(request, lugares):
	dato = Lugar.objects.get(pk=lugares)
	provincias = Provincia.objects.filter(lugar=dato)
	return render_to_response('lugares.html',{'provincias':provincias}, context_instance=RequestContext(request))

def vista_lugar(request, provincia):
	provincias = Provincia.objects.get(pk=provincia)
	lugares = Tipo_lugar_turistico.objects.all()
	return render_to_response('lugares_tipo.html',{'lugares':lugares,'provincias':provincias}, context_instance=RequestContext(request))

def lugares_turisticos(request, sitio, tipo_lugar):
	lugares_turisticos = Lugares_turisticos.objects.filter(provincia=sitio).filter(Tipo_lugar_turistico=tipo_lugar)
	print lugares_turisticos
	return render_to_response('lugares_turisticos.html',{'lugares_turisticos':lugares_turisticos}, context_instance=RequestContext(request))

def lugar_turistico(request, id):
	lugar_turistico = get_object_or_404(Lugares_turisticos, pk=id)
	lugar_turisticos = Lugares_turisticos.objects.filter(id=id)
	return render_to_response('lugar_turistico.html',{'lugar_turistico':lugar_turistico}, context_instance=RequestContext(request))

def mapa_turistica(request, id):
	lugar_turistico = get_object_or_404(Lugares_turisticos, pk=id)
	return render_to_response('mapa_turistico.html',{'lugar_turistico':lugar_turistico}, context_instance=RequestContext(request))

def galeria_turistica(request, id):
	lugar_turistico = Lugares_turisticos.objects.get(id=id)
	imagenes = lugar_turistico.galeria_imagenes.all()
	return render_to_response('galeria_turistico.html',{'lugar_turistico':lugar_turistico,'imagenes':imagenes}, context_instance=RequestContext(request))

#rutas
def ruta_detalle(request):
	lugares = Lugar.objects.all()
	return render_to_response('ruta_detalle.html',{'lugares':lugares}, context_instance=RequestContext(request))

def ruta_lugares(request, lugares):
	dato = Lugar.objects.get(pk=lugares)
	provincias = Provincia.objects.filter(lugar=dato)
	print "ruta lugares"
	return render_to_response('rutas.html',{'provincias':provincias}, context_instance=RequestContext(request))

def vista_ruta(request, provincia):
	provincias = Provincia.objects.get(pk=provincia)
	lugares = Tipo_lugar_turistico.objects.all()
	print "ruta vista"
	return render_to_response('rutas_tipo.html',{'lugares':lugares,'provincias':provincias}, context_instance=RequestContext(request))

def rutas_turisticos(request, sitio, tipo_lugar):
	lugares_turisticos = Lugares_turisticos.objects.filter(provincia=sitio).filter(Tipo_lugar_turistico=tipo_lugar)
	print lugares_turisticos
	return render_to_response('rutas_turisticos.html',{'lugares_turisticos':lugares_turisticos}, context_instance=RequestContext(request))

def ruta_turistico(request, id):
	lugar_turistico = get_object_or_404(Lugares_turisticos, pk=id)
	rutas = lugar_turistico.ruta
	print rutas
	return render_to_response('ruta_turistico.html',{'lugar_turistico':lugar_turistico}, context_instance=RequestContext(request))

def detalle_artesania(request):
	lugares = Lugar.objects.all()
	return render_to_response('detalle_artesania.html',{'lugares':lugares}, context_instance=RequestContext(request))

def lista_artesania(request, lugares):
	dato = Lugar.objects.get(pk=lugares)
	provincias = Provincia.objects.filter(lugar=dato)
	return render_to_response('artesanias.html',{'provincias':provincias}, context_instance=RequestContext(request))

def vista_artesania(request, provincia):
	provincias = Provincia.objects.get(pk=provincia)
	lugares = Tipo_lugar_turistico.objects.all()
	return render_to_response('artesania_tipo.html',{'lugares':lugares,'provincias':provincias}, context_instance=RequestContext(request))

def lugares_artesanias(request, sitio, tipo_lugar):
	lugares_turisticos = Artesania.objects.filter(provincia=sitio).filter(Tipo_lugar_turistico=tipo_lugar)
	return render_to_response('lugares_artesanias.html',{'lugares_turisticos':lugares_turisticos}, context_instance=RequestContext(request))

def lugar_artesania(request, id):
	lugar_turistico = get_object_or_404(Artesania, pk=id)
	return render_to_response('lugar_artesania.html',{'lugar_turistico':lugar_turistico}, context_instance=RequestContext(request))

def mapa_artesania(request, id):
	lugar_turistico = get_object_or_404(Artesania, pk=id)
	return render_to_response('mapa_artesania.html',{'lugar_turistico':lugar_turistico}, context_instance=RequestContext(request))

def galeria_artesania(request, id):
	lugar_turistico = Artesania.objects.get(id=id)
	imagenes = lugar_turistico.galeria_imagenes.all()
	return render_to_response('galeria_artesania.html',{'lugar_turistico':lugar_turistico,'imagenes':imagenes}, context_instance=RequestContext(request))

def detalle_danza(request):
	lugares = Lugar.objects.all()
	return render_to_response('detalle_danza.html',{'lugares':lugares}, context_instance=RequestContext(request))

def lista_danza(request, lugares):
	dato = Lugar.objects.get(pk=lugares)
	provincias = Provincia.objects.filter(lugar=dato)
	return render_to_response('danzas.html',{'provincias':provincias}, context_instance=RequestContext(request))

def vista_danza(request, provincia):
	provincias = Provincia.objects.get(pk=provincia)
	lugares = Tipo_lugar_turistico.objects.all()
	return render_to_response('danza_tipo.html',{'lugares':lugares,'provincias':provincias}, context_instance=RequestContext(request))

def lugares_danzas(request, sitio, tipo_lugar):
	lugares_turisticos = Danza.objects.filter(provincia=sitio).filter(Tipo_lugar_turistico=tipo_lugar)
	return render_to_response('lugares_danzas.html',{'lugares_turisticos':lugares_turisticos}, context_instance=RequestContext(request))

def lugar_danza(request, id):
	lugar_turistico = get_object_or_404(Danza, pk=id)
	return render_to_response('lugar_danza.html',{'lugar_turistico':lugar_turistico}, context_instance=RequestContext(request))

def mapa_danza(request, id):
	lugar_turistico = get_object_or_404(Danza, pk=id)
	return render_to_response('mapa_danza.html',{'lugar_turistico':lugar_turistico}, context_instance=RequestContext(request))

def galeria_danza(request, id):
	lugar_turistico = Danza.objects.get(id=id)
	imagenes = lugar_turistico.galeria_imagenes.all()
	return render_to_response('galeria_danza.html',{'lugar_turistico':lugar_turistico,'imagenes':imagenes}, context_instance=RequestContext(request))


def detalle_evento(request):
	lugares = Lugar.objects.all()
	return render_to_response('detalle_evento.html',{'lugares':lugares}, context_instance=RequestContext(request))

def lista_evento(request, lugares):
	dato = Lugar.objects.get(pk=lugares)
	provincias = Provincia.objects.filter(lugar=dato)
	return render_to_response('eventos.html',{'provincias':provincias}, context_instance=RequestContext(request))

def vista_evento(request, provincia):
	provincias = Provincia.objects.get(pk=provincia)
	lugares = Tipo_lugar_turistico.objects.all()
	return render_to_response('evento_tipo.html',{'lugares':lugares,'provincias':provincias}, context_instance=RequestContext(request))

def meses(request, sitio, tipo_lugar):
	meses = Meses.objects.all()
	return render_to_response('meses.html',{'meses':meses,'sitio':sitio,'tipo_lugar':tipo_lugar}, context_instance=RequestContext(request))

def lugares_eventos(request, sitio, tipo_lugar, mes):
	lugares_turisticos = Evento.objects.filter(provincia=sitio).filter(Tipo_lugar_turistico=tipo_lugar).filter(mes_evento=mes)
	return render_to_response('lugares_eventos.html',{'lugares_turisticos':lugares_turisticos}, context_instance=RequestContext(request))

def lugar_evento(request, id):
	lugar_turistico = get_object_or_404(Evento, pk=id)
	return render_to_response('lugar_evento.html',{'lugar_turistico':lugar_turistico}, context_instance=RequestContext(request))

def mapa_evento(request, id):
	lugar_turistico = get_object_or_404(Evento, pk=id)
	return render_to_response('mapa_evento.html',{'lugar_turistico':lugar_turistico}, context_instance=RequestContext(request))

def galeria_evento(request, id):
	lugar_turistico = Evento.objects.get(id=id)
	imagenes = lugar_turistico.galeria_imagenes.all()
	return render_to_response('galeria_evento.html',{'lugar_turistico':lugar_turistico,'imagenes':imagenes}, context_instance=RequestContext(request))
