from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Productos
from .forms import ProductoForm


# Create your views here.
def index(request):
    return render(request, 'productos/index.html', {
        'productos': Productos.objects.all()
    })

def view_producto(request, id):
    producto = Productos.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            new_nombre = form.cleaned_data['nombre']
            new_descripcion = form.cleaned_data['descripcion']
            new_precio = form.cleaned_data['precio']
            new_stock = form.cleaned_data['stock']
            new_modelo = form.cleaned_data['modelo']

            new_producto = Productos(
                nombre = new_nombre, 
                descripcion = new_descripcion,
                precio = new_precio,
                stock = new_stock,
                modelo = new_modelo
            )
            new_producto.save()
            return render(request, 'productos/add.html', {
                'form': ProductoForm(),
                'success': True
            })
    else:
        form = ProductoForm()
    return render(request, 'productos/add.html', {
        'form': ProductoForm()
    })

def edit(request, id):
    if request.method == 'POST':
        producto = Productos.objects.get(pk=id)
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return render(request, 'productos/edit.html', {
                'form': form, 
                'success': True
            })
    else:
        producto = Productos.objects.get(pk=id)
        form=ProductoForm(instance=producto)
    return render(request, 'productos/edit.html', {
        'form': form
    })

def delete(request, id):
    if request.method == 'POST':
        producto = Productos.objects.get(pk=id)
        producto.delete()
    return HttpResponseRedirect(reverse('index'))