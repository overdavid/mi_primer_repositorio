from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

def formulario(request):
    return render(request, 'home6.html')

def insert(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")

    prioridad = request.POST["name_prioridad"]
    titulo = request.POST["nombre_titulo"]
    nota = request.POST["name_nota"]

    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO nota VALUES ('{prioridad}','{titulo}','{nota}');")
    conn.commit()
    cursor.close()
    conn.close()

    return HttpResponse(f'Insertado <br> '
                        f'prioridad: {prioridad}<br>'
                        f'titulo: {titulo}<br>'
                        f'nota: {nota}<br>')






