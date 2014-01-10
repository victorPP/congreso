from django.db import models


class persona(models.Model):
		nombre = models.CharField(max_length=50)
		apeidos = models.CharField(max_length=100)
		telefono = models.CharField(max_length=50)
		direccion = models.CharField(max_length=100)
		gestion = models.TextField()
		observaciones = models.TextField()
		status = models.BooleanField(default=false)

		def __unicode__(self):

				nombreCompleto = "%s %s" %(self.nombre, self.apeidos)
					return nombreCompleto
