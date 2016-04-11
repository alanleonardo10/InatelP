from django.shortcuts import render

# Create your views here.
def home(request):
        context = {'texto': 'Seu primeiro projeto Django no Linux/Ubuntu com Sublime Text 3'}
        return render(request, 'index.html', context)