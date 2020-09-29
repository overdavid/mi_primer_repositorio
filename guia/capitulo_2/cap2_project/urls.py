from django.contrib import admin
from django.urls import path
from pages import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_page_view, name='home'),
    path('about/', views.about, name='about'),
    path('Menu_Niños/', views.Menu_Ninos, name='Menu_Ninos'),

]
