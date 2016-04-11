from django.shortcuts import render

from product_app.models import Product
from product_app.serializers import ProductSerializer
from rest_framework import mixins
from rest_framework import generics

# Create your views here.

class ProductList(mixins.ListModelMixin,
					mixins.CreateModelMixin,
					generics.GenericAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class ProductDetail(mixins.RetrieveModelMixin,
						mixins.UpdateModelMixin,
						mixins.DestroyModelMixin,
						generics.GenericAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def get(self, request, *args, **kwargs):
		print("teste")
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
