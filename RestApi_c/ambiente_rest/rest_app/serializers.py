from rest_framework import serializers
from models import Product

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		field = ('id', 'name', 'price', 'featurea', 'featureb', 'featurec')