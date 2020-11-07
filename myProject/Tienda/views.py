from django.shortcuts import render,HttpResponse,redirect
from .forms import Cliente_form
from .models import Cliente
from django.views.generic import TemplateView,CreateView
from  django.urls import reverse_lazy
# Create your views here.

class Index(TemplateView):
    template_name = 'Tienda/index.html'

class Registrar(CreateView):
    model = Cliente
    form_class = Cliente_form
    template_name = 'Tienda/register.html'
    success_url = reverse_lazy('Login')

# def registrar(request):
#     #return render(request,'Tienda/register.html')
#     cliente_form = Cliente_form(Cliente)
#     if request.method == 'POST':
#          cliente_form = Cliente_form(request.POST)
#          if cliente_form.is_valid():
#              cliente_form.save()
#              return redirect('login')
#     else:
#         cliente_form = Cliente_form()
#         print(cliente_form)
#     return render(request,'Tienda/register.html',{'cliente_form':cliente_form})