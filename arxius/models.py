from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Carpeta(models.Model):
	class Meta:
		verbose_name_plural = "carpetes"
	nom = models.CharField(max_length=200)
	data_creacio = models.DateTimeField(null=False, blank=False)
	creador = models.ForeignKey(User, on_delete = models.CASCADE)
	carpeta_pare = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True) 
	def __str__(self):
		return str(self.id) + '-' + self.nom


class Arxiu(models.Model):
	nom = models.CharField(max_length=200)
	data_creacio = models.DateTimeField(null=False, blank=False)
	creador = models.ForeignKey(User, on_delete = models.CASCADE)
	carpeta_pare = models.ForeignKey("Carpeta", on_delete=models.CASCADE, null=True, blank=True) 
	def __str__(self):
		return str(self.id) + '-' + self.nom
