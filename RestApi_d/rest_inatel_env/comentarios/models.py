from django.db import models

# Create your models here.

class Comentario(models.Model):
	titulo = models.CharField("Titulo", max_length=255)
	comentario = models.TextField("comentario")
