from django.shortcuts import render
from django.http import HttpResponse
from appSitio.models import *
from appSitio.forms import *

# Create your views here.

def inicio(request):
    return render(request, "appSitio/index.html")

def madre(request):
    return render(request, "appSitio/madre.html")

def bebe(request):
    return render(request, "appSitio/bebe.html")

def semana(request):
    return render(request, "appSitio/semana.html")

def creacionMadre(request):
    if request.method == "POST":
        formulario = MadreFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            madre = Madre(nombre = data["nombre"], edad=data["edad"], peso=data["peso"])
            madre.save()

            return render(request, "appSitio/madre.html")
    
    formulario = MadreFormulario()

    contexto = {"formulario" : formulario}
    return render(request, "appSitio/madre_formulario.html", contexto)

def creacionBebe(request):
    if request.method == "POST":
        formulario = BebeFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            bebef = Bebe(dia= data["dia"], mes= data["mes"], year= data["year"])
            bebef.save()

            return render(request, "appSitio/bebe.html")
    
    formulario = BebeFormulario()

    contexto = {"formulario" : formulario}
    return render(request, "appSitio/bebe_formulario.html", contexto)

def creacionSemana(request):
    if request.method == "POST":
        formulario = SemanaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            semana = Semana(semana = data["semana"])
            semana.save()

            return render(request, "appSitio/semana.html")
    
    formulario = SemanaFormulario()

    contexto = {"formulario" : formulario}
    return render(request, "appSitio/semana_formulario.html", contexto)

def buscarSemana(request):
    return render(request, "appSitio/buscar_semana.html")

def resultadoSemana(request):
    res_semana = request.GET["nro_semana"]
    semanas = Semana.objects.filter(semana__icontains = res_semana)
    return render(request, "appSitio/resultado_semana.html", {"Semanas" : semanas})
    