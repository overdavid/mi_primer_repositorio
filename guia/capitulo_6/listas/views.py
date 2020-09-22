from django.shortcuts import render, redirect
from django.http import HttpResponse
import psycopg2

def formulario(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Nota;")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    params = {'notas': 'funciona'}
    return render(request, 'home6.html', params)

def insert(request):
    print('hola')
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")

    prioridad = request.POST["name_prioridad"]
    titulo = request.POST["nombre_titulo"]
    nota = request.POST["name_nota"]

    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO nota VALUES ('{prioridad}','{titulo}','{notas}');")
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('notas')






