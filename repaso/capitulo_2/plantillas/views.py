from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


from django.shortcuts import render
def home_page_view(request):
   return render (request,'Hola Mundo!')

def about (request):
   return render (request, 'about.html')

def test(request):
      return render(request, 'test.html')


