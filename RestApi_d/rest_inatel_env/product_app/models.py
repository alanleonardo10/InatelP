from django.db import models

# Create your models here.

class Product(models.Model):
	titulo = models.CharField("Name", max_length=255)
	price = models.TextField("Price")
	featurea = models.TextField("Feature 1")
	featureb = models.TextField("Feature 2")
	featurec = models.TextField("Feature 3")