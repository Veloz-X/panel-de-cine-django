from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('vender/', views.vender, name='vender'),
    path('peliculas/', views.peliculas, name='peliculas'),
    path('create_pelicula/', views.create_pelicula, name='create_pelicula'),
    path('lista_ventas/', views.lista_ventas, name='lista_ventas')
    
]