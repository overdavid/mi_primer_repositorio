from django.shortcuts import render

def home_page_view(request):
   return render(request, 'examen.html')

def django(request):
   return render (request, 'django.html')

