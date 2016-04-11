from django.shortcuts import render

from comentarios.models import Comentario
from comentarios.serializers import ComentarioSerializer
from rest_framework import mixins
from rest_framework import generics

# Create your views here.

class ComentarioList(mixins.ListModelMixin,
					mixins.CreateModelMixin,
					generics.GenericAPIView):
	queryset = Comentario.objects.all()
	serializer_class = ComentarioSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class ComentarioDetail(mixins.RetrieveModelMixin,
						mixins.UpdateModelMixin,
						mixins.DestroyModelMixin,
						generics.GenericAPIView):
	queryset = Comentario.objects.all()
	serializer_class = ComentarioSerializer

	def get(self, request, *args, **kwargs):
		print("teste")
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
