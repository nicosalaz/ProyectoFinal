from django.shortcuts import render,HttpResponse,redirect
from .forms import Cliente_form
from django.forms import modelform_factory
from .models import Cliente
# Create your views here.

def login(request):
    return render(request,'Tienda/login.html')

def registrar(request):
    #return render(request,'Tienda/register.html')
    cliente_form = Cliente_form(Cliente)
    if request.method == 'POST':
         cliente_form = Cliente_form(request.POST)
         if cliente_form.is_valid():
             cliente_form.save()
             return redirect('login')
    else:
        cliente_form = Cliente_form()
        print(cliente_form)
    return render(request,'Tienda/register.html',{'cliente_form':cliente_form})