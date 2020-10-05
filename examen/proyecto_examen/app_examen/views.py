from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

def home_page_view(request):
   return render(request, 'examen.html')

def django(request):
   return render (request, 'django.html')

def insert(request):
    conn = psycopg2.connect(dbname="capitulo_4_db",
                        	user="capitulo_4_user",
                        	password="patata")
    with open("debug.log", "a+") as debug_file:
        print("Funciona!", file=debug_file)
    return HttpResponse('Funciona!')

