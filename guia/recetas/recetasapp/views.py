from django.shortcuts import render
# Create your views here.
def recetas_home_page_view(request):
   return render(request, 'Recetas_Home.html')

def canelones(request):
   return render(request, 'Canelones.html')

def menú_infantil(request):
   return render(request, 'Menú_Infantil.html')

def mafe(request):
   return render(request, 'Mafe.html')

def feijoada(request):
   return render(request, 'Feijoada.html')

def pizza(request):
   return render(request, 'Pizza.html')

def flor_de_calabacin(request):
   return render(request, 'Flor_de_Calabacin.html')

def gazpacho(request):
   return render(request, 'Gazpacho.html')

def sopa_de_noodles(request):
   return render(request, 'Sopa_de_Noodles.html')

def ensaladilla_rusa(request):
   return render(request, 'Ensaladilla_Rusa.html')

def carbonara(request):
   return render(request, 'Carbonara.html')

def receta_facil(request):
   return render(request, 'Receta_Facil.html')

#llamada del documento a HTML devuelve Recetas Facil HTML