from django.shortcuts import render, redirect
from django.db import models
from .models import Proyecto, Tester, CasoPrueba
from .forms import ProyectoForm, TesterForm, CasoPruebaForm, BuscarCasoForm


def index(request):
    casos = CasoPrueba.objects.all()
    proyectos = Proyecto.objects.all()
    testers = Tester.objects.all()
    return render(request, 'gestion/index.html', {
        'casos': casos,
        'proyectos': proyectos,
        'testers': testers
    })

def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_casos')
    else:
        form = ProyectoForm()
    return render(request, 'gestion/crear_proyecto.html', {'form': form})

def crear_tester(request):
    if request.method == 'POST':
        form = TesterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_casos')
    else:
        form = TesterForm()
    return render(request, 'gestion/crear_tester.html', {'form': form})

def lista_casos(request):
    casos = CasoPrueba.objects.all()
    return render(request, 'gestion/lista_casos.html', {'casos': casos})

def crear_caso(request):
    if request.method == 'POST':
        form = CasoPruebaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_casos')
    else:
        form = CasoPruebaForm()
    return render(request, 'gestion/crear_caso.html', {'form': form})


def detalle_caso(request, pk):
    caso = get_object_or_404(CasoPrueba, pk=pk)
    return render(request, 'gestion/detalle_caso.html', {'caso': caso})


def buscar_caso(request):
    form = BuscarCasoForm(request.GET or None)
    resultados = []

    if form.is_valid():
        titulo = form.cleaned_data.get('titulo')
        if titulo:
            resultados = CasoPrueba.objects.filter(nombre__icontains=titulo)
        else:
            resultados = CasoPrueba.objects.all()

    return render(request, 'gestion/buscar.html', {
        'form': form,
        'resultados': resultados
    })
