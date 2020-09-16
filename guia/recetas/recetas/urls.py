"""recetas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path
from recetasapp import views
urlpatterns = [
    path('recetas_home/',views.recetas_home_page_view, name='home'),
    path('canelones/',views.canelones, name='canelones'),
    path('menú_infantil/',views.menú_infantil, name='menú_infantil'),
    path('receta_facil/', views.receta_facil, name='receta_facil'),
    path('mafe/', views.mafe, name='mafe'),
    path('feijoada/', views.feijoada, name='feijoada'),
    path('pizza/', views.pizza, name='pizza'),
    path('flor_de_calabacin/', views.flor_de_calabacin, name='flor_de_calabacin'),
    path('gazpacho/', views.gazpacho, name='gazpacho'),
    path('sopa_de_noodles/', views.sopa_de_noodles, name='sopa_de_noodles'),
    path('ensaladilla_rusa/', views.ensaladilla_rusa, name='ensaladilla_rusa'),
    path('carbonara/', views.carbonara, name='carbonara')

    # pach ('CArbonara = URL de la Pagina en la barra del navegador /,
    #   views.carbonara (hace referncia a la funcion vista)
    #   name= carbonara hace referencia al Home HTML<a href="{% url 'carbonara' %}"> carbonara</a>
]    #

