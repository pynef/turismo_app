#enconding:utf-8
from principal.models import Provincia, Lugar, Danza,  Artesania, Meses, Evento, Lugares_turisticos, Tipo_lugar_turistico 

Lugar.objects.create(
	nombre = 'Valle del Mantaro',
	descripcion = 'Valle del Mantaro')

Lugar.objects.create(
	nombre = 'Selva Central',
	descripcion = 'Selva Central')

Lugar.objects.create(
	nombre = 'Alto Andino',
	descripcion = 'Alto Andino')

Provincia.objects.create(
	nombre = 'Huancayo',
	clima = 'seco',
	altitud_logitud = '-46468688,-546464674',
	ciudadcapital = 'Huancayo',
	lugar = Lugar.objects.get(pk=1)
)

Provincia.objects.create(
	nombre = 'Concepcion',
	clima = 'seco y frio',
	altitud_logitud = '-46468688,-546464674',
	ciudadcapital = 'Huancayo',
	lugar = Lugar.objects.get(pk=1)
)

Provincia.objects.create(
	nombre = 'Jauja',
	clima = 'frio',
	altitud_logitud = '-46468688,-546464674',
	ciudadcapital = 'xauxa',
	lugar = Lugar.objects.get(pk=1)
)

Provincia.objects.create(
	nombre = 'Chupaca',
	clima = 'helado',
	altitud_logitud = '-46468688,-546464674',
	ciudadcapital = 'agua',
	lugar = Lugar.objects.get(pk=1)
)

Provincia.objects.create(
	nombre = 'Chanchamayo',
	clima = 'calido',
	altitud_logitud = '-46468688,-546464674',
	ciudadcapital = 'Chancha',
	lugar = Lugar.objects.get(pk=2)
)

Provincia.objects.create(
	nombre = 'Satipo',
	clima = 'humedo',
	altitud_logitud = '-46468688,-546464674',
	ciudadcapital = 'la merced',
	lugar = Lugar.objects.get(pk=2)
)

Provincia.objects.create(
	nombre = 'Tarma',
	clima = 'calidez',
	altitud_logitud = '-46468688,-546464674',
	ciudadcapital = 'tarma',
	lugar = Lugar.objects.get(pk=2)
)

Provincia.objects.create(
	nombre = 'Junin',
	clima = 'helado',
	altitud_logitud = '-46468688,-546464674',
	ciudadcapital = 'junin',
	lugar = Lugar.objects.get(pk=3)
)

Provincia.objects.create(
	nombre = 'Yauli',
	clima = 'seco y frio',
	altitud_logitud = '-46468688,-546464674',
	ciudadcapital = 'yauli',
	lugar = Lugar.objects.get(pk=3)
)

Tipo_lugar_turistico.objects.create(
	nombre = 'Lugares Arqueologicos',
	descripcion = 'Lugares Arqueologicos')

Tipo_lugar_turistico.objects.create(
	nombre = 'Parques Emblematicos',
	descripcion = 'Parques Emblematicos')


Tipo_lugar_turistico.objects.create(
	nombre = 'Museos',
	descripcion = 'Museos')


Meses.objects.create(
	nombre = 'Enero',
	descripcion = 'Esasadsad'
	)
Meses.objects.create(
	nombre = 'Febrero',
	descripcion = 'fasdsadasd'
	)
Meses.objects.create(
	nombre = 'Marzo',
	descripcion = 'MarzoMarzo'
	)
Meses.objects.create(
	nombre = 'Abril',
	descripcion = 'Museos'
	)
Meses.objects.create(
	nombre = 'Mayo',
	descripcion = 'Museos'
	)
Meses.objects.create(
	nombre = 'Junio',
	descripcion = 'Museos'
	)
Meses.objects.create(
	nombre = 'Julio',
	descripcion = 'Museos'
	)
Meses.objects.create(
	nombre = 'Agosto',
	descripcion = 'Museos'
	)
Meses.objects.create(
	nombre = 'Setiembre',
	descripcion = 'Museos'
	)
Meses.objects.create(
	nombre = 'Octubre',
	descripcion = 'Museos'
	)
Meses.objects.create(
	nombre = 'Noviembre',
	descripcion = 'Museos'
	)
Meses.objects.create(
	nombre = 'Diciembre',
	descripcion = 'Museos'
	)