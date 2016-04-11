from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pessoa(models.Model):
        nome = models.CharField(max_length=100)
        cpf = models.CharField(max_length=20)

        def __unicode__(self):
                return self.nome
