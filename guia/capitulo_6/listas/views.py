from django.shortcuts import render
from django.http import HttpResponse

def formulario(request):
    return render(request, 'home6.html')

def insert(request):
    prioridad = request.POST["name_prioridad"]
    titulo = request.POST["nombre_titulo"]
    nota = request.POST["name_nota"]

    return HttpResponse(f'Insertado <br> '
                        f'prioridad: {prioridad}<br>'
                        f'titulo: {titulo}<br>'
                        f'nota: {nota}<br>'
                        )






