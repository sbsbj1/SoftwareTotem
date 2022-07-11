from multiprocessing.connection import Client
from django.shortcuts import render, redirect
from django.views.decorators import csrf
from .models import Cliente
from .forms import ClienteForm 

# Create your views here.
def home(request):
    return render (request, 'home.html')

def ver(request):
    return render (request, 'ver.html')

def mostrar(request):
    clientes = Cliente.objects.all()
    datos = {
        'clientes' : clientes
    }
    return render(request, 'mostrar.html', datos)


def form_cliente(request): 

    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect ('mostrar')
    else:
        cliente_form = ClienteForm()
    return render(request, 'form_crear_cliente.html', {'cliente_form': cliente_form})


def form_modcliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    datos = {
        'form': ClienteForm(instance = cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance = cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect ('mostrar')
        
    return render(request, 'form_modcliente.html', datos)


def form_del_cliente(request,id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect('mostrar')