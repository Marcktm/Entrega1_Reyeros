from django.urls import path
from appSitio.views import *

urlpatterns = [

    path("madre/", madre, name="ap-madre"),
    path("madre/crear/", creacionMadre, name='crear-madre'),
    path("bebe/", bebe, name='ap-bebe'),
    path("bebe/crear/", creacionBebe, name='crear-bebe'),
    path("semana/", semana, name='ap-semana'),
    path("semana/crear/", creacionSemana, name='crear-semana'),
    path("semana/buscar/", buscarSemana, name='busc-semana'),
    path('semana/resultado/', resultadoSemana, name='result-semana'),
    path("", inicio, name='ap-inicio'),

    
]
