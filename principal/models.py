#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Lugar(models.Model):
	nombre = models.CharField(max_length=150, verbose_name='Nombre Lugares')
	descripcion = models.CharField(max_length=150, verbose_name="Lugar Descripción")
	def __unicode__(self):
		return self.nombre

class Provincia(models.Model):
	nombre = models.CharField(max_length=150, verbose_name='Nombre Provincia')
	clima = models.CharField(max_length=200 , verbose_name='Clima')
	altitud_logitud = models.CharField(max_length=200 ,verbose_name='Altitud y Longitud')
	ciudadcapital = models.CharField(max_length=200 , verbose_name='Ciudad Capital')
	lugar = models.ForeignKey(Lugar)
	def __unicode__(self):
		return self.nombre

class Tipo_lugar_turistico(models.Model):
	nombre = models.CharField(max_length=200,)
	descripcion = models.TextField()
	def __unicode__(self):
		return self.nombre

class Galeria_turismo(models.Model):
	nombre = models.CharField(max_length=200)
	imagen = models.ImageField(upload_to='lugares_turisticos/galeria')
	def __unicode__(self):
		return self.nombre

class Lugares_turisticos(models.Model):
	nombre = models.CharField(max_length=150, verbose_name='Nombre')
	descripcion = models.TextField(help_text='descripcion', verbose_name='Descripción')
	portada = models.ImageField(upload_to='lugares_turisticos', verbose_name='Portada del Lugar')
	ruta = models.CharField(max_length=300, help_text="Separar con ','", verbose_name='Recorrido a llegar')
	latitud_longitud = models.CharField(max_length=400, verbose_name='Latitud y Longitud')
	facebook = models.CharField(max_length=200, null= True, blank= True)
	twitter = models.CharField(max_length=200, null= True, blank= True)
	youtube = models.CharField(max_length=200, null= True, blank= True)
	google = models.CharField(max_length=200, null= True, blank= True)
	Tipo_lugar_turistico = models.ForeignKey(Tipo_lugar_turistico)
	provincia = models.ForeignKey(Provincia)
	galeria_imagenes = models.ManyToManyField(Galeria_turismo, null= True, blank= True)
	def __unicode__(self):
		return self.nombre

class Galeria_danzas(models.Model):
	nombre = models.CharField(max_length=200)
	imagen = models.ImageField(upload_to='danzas/galeria')
	def __unicode__(self):
		return self.nombre

class Danza(models.Model):
	nombre = models.CharField(max_length=150, verbose_name='Danzas')
	descripcion = models.TextField(help_text='descripcion', verbose_name='Descripción')
	portada = models.ImageField(upload_to='danzas', verbose_name='Portada')
	latitud_longitud = models.CharField(max_length=400, verbose_name='Latitud y Longitud')
	facebook = models.CharField(max_length=200, null= True, blank= True)
	twitter = models.CharField(max_length=200, null= True, blank= True)
	youtube = models.CharField(max_length=200, null= True, blank= True)
	google = models.CharField(max_length=200, null= True, blank= True)
	Tipo_lugar_turistico = models.ForeignKey(Tipo_lugar_turistico)
	provincia = models.ForeignKey(Provincia)
	galeria_imagenes = models.ManyToManyField(Galeria_danzas, null= True, blank= True)
	def __unicode__(self):
		return self.nombre

class Galeria_artesanias(models.Model):
	nombre = models.CharField(max_length=200)
	imagen = models.ImageField(upload_to='artesanias/galeria')
	def __unicode__(self):
		return self.nombre

class Artesania(models.Model):
	nombre = models.CharField(max_length=150, verbose_name='Artesania')
	descripcion = models.TextField(help_text='descripcion', verbose_name='Descripción')
	portada = models.ImageField(upload_to='artesanias', verbose_name='Portada')
	latitud_longitud = models.CharField(max_length=400, verbose_name='Latitud y Longitud')
	facebook = models.CharField(max_length=200, null= True, blank= True)
	twitter = models.CharField(max_length=200, null= True, blank= True)
	youtube = models.CharField(max_length=200, null= True, blank= True)
	google = models.CharField(max_length=200, null= True, blank= True)
	Tipo_lugar_turistico = models.ForeignKey(Tipo_lugar_turistico)
	provincia = models.ForeignKey(Provincia)
	galeria_imagenes = models.ManyToManyField(Galeria_artesanias, null= True, blank= True)
	def __unicode__(self):
		return self.nombre

class Galeria_eventos(models.Model):
	nombre = models.CharField(max_length=200)
	imagen = models.ImageField(upload_to='eventos/galeria')
	def __unicode__(self):
		return self.nombre

class Meses(models.Model):
	nombre = models.CharField(max_length=100, verbose_name='Nombre del Mes')
	descripcion = models.TextField()
	def __unicode__(self):
		return self.nombre

class Evento(models.Model):
	nombre = models.CharField(max_length = 250, verbose_name='Nombre del Evento')
	dia_evento = models.IntegerField()
	mes_evento = models.IntegerField()
	anio_evento = models.IntegerField()
	fecha_creacion = models.DateField(auto_now='True')
	descripcion = models.TextField(help_text='descripcion', verbose_name='Descripción')
	portada = models.ImageField(upload_to='eventos', verbose_name='Portada del Evento')
	latitud_longitud = models.CharField(max_length=400, verbose_name='Latitud y Longitud')
	facebook = models.CharField(max_length=200, null= True, blank= True)
	twitter = models.CharField(max_length=200, null= True, blank= True)
	youtube = models.CharField(max_length=200, null= True, blank= True)
	google = models.CharField(max_length=200, null= True, blank= True)
	Tipo_lugar_turistico = models.ForeignKey(Tipo_lugar_turistico)
	provincia = models.ForeignKey(Provincia)
	galeria_imagenes = models.ManyToManyField(Galeria_eventos, null= True, blank= True)
	def __unicode__(self):
		return self.nombre
 


