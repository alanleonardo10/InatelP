from django.shortcuts import render
from django.http import HttpResponse
   
def index(request):
	dicionario_contexto = {'msgnegrito': "Testando fonte em negrito..."}	
	return render(request, 'django/index.html', dicionario_contexto)

