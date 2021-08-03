from django.shortcuts import render, redirect, get_object_or_404
from .models import Login, Producto
from .forms import LoginForm, ProductoForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request, 'petSalud/home.html')


def loginVista(request):
    data = {
        'form': AuthenticationForm()
    }
    if request.method == "POST":
        formulario = AuthenticationForm(data=request.POST)
        if formulario.is_valid():
            formulario.username = request.POST['username']
            formulario.password = request.POST['password']

            if formulario.username=="administrador":
                return HttpResponseRedirect('/menu_gestion/')           
            else:
                return HttpResponseRedirect('/nuestros_productos/')
                        
        data["form"] = formulario
    
    return render(request, 'petSalud/loginvista.html', data)
            


def registro(request):
    return render(request, 'petSalud/registrarvista.html')


def nuestros_productos(request):
    return render(request, 'petSalud/nuestros_productos.html')


def menu_gestion(request):
    return render(request, 'petSalud/menuGestion.html')


def descripcion(request):
    return render(request, 'petSalud/descripcion.html')


def agregar(request):
    
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario    

    return render(request, 'petSalud/formulario_agregar.html', data)


def eliminar(request):
    return render(request, 'petSalud/formulario_eliminar.html')

def listar_productos(request):
    
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }
    return render(request, 'petSalud/listar.html', data)


def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar_productos')
        data["from"] = formulario

    return render(request, 'petSalud/modificar.html', data)


def eliminar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to='listar_productos')