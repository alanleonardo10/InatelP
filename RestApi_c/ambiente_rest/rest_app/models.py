from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=100, unique=True, blank=True)
	price = models.CharField(max_length=50)
	featurea = models.CharField(max_length=100)
	featureb = models.CharField(max_length=100)
	featurec = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name