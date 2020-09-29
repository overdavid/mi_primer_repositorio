from django.http import HttpResponse
# Create your views here.
def home_page_view(request):
   return HttpResponse('<!DOCTYPE html> <html> <body> <h1>Pagina principal del Examen</h1></body></html>')