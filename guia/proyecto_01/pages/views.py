from django.http import HttpResponse
# Create your views here.
def home_page_view(request):
   return HttpResponse('<!DOCTYPE html> <html> <body> <h1>hola mundo!</h1></body></html>')