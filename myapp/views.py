from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from . models import Pelicula,VentasCliente
from django.shortcuts import render,redirect,get_list_or_404
from .forms import CrearVenta,CrearPelicula



@login_required(login_url='login')
def index(request):
    title='My To-Do List'
    return render(request, 'index.html')

@login_required(login_url='login')
def vender(request):
    if request.method == 'POST':
        form = CrearVenta(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            pelicula = data['pelicula']  # Esto es una instancia de Pelicula
            nombre = data['nombre']
            cedula = data['cedula']
            numero_entradas = data['numeroEntradas']
            fecha = data['fecha']
            entrada2x1 = data['entrada2x1']
            
            venta = VentasCliente(
                pelicula=pelicula,
                nombre=nombre,
                cedula=cedula,
                numeroEntradas=numero_entradas,
                fecha=fecha,
                entrada2x1=entrada2x1
            )
            venta.save()
            return redirect('vender')  # Cambia esto a la vista deseada
    else:
        form = CrearVenta()
    
    return render(request, 'vender.html', {'form': CrearVenta()})

@login_required(login_url='login')
def peliculas(request):
    peliculas=Pelicula.objects.all()
    return render(request, 'peliculas.html', {'peliculas': peliculas})

@login_required(login_url='login')   
def create_pelicula(request):
    if request.method == 'GET':
        return render(request, 'crear_pelicula.html',{
            'form': CrearPelicula()
        })
    else:
        print(request.POST)
        Pelicula.objects.create(name=request.POST['name'], img=request.POST['img'])
        return redirect('peliculas')

@login_required(login_url='login')
def lista_ventas(request):
    ventas=VentasCliente.objects.all()
    return render(request, 'lista_ventas.html', {'ventas': ventas})