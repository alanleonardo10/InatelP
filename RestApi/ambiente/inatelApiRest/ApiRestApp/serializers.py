from rest_framework import serializers
from talk.models import Post


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	"""Serialização de produtos"""
	class Meta:
		model = null
		fields = ('url', 'name', 'price', 'feature_a', 'feature_b', 'feature_c')
		