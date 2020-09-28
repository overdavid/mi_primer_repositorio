
import random

from django.shortcuts import render
# Create your views here.
def home_page_view(request):
   return render(request, 'Recetas.html')

def about(request):
   parametros = {'numero_favorito': random.randrange(10)}
   return render(request, 'about.html', parametros)

def over(request):
   return render(request, 'test.html')

