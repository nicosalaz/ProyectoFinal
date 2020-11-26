from django.shortcuts import render,HttpResponse,redirect
from .forms import Cliente_form
from .models import Cliente,Inventario,Carrito
from django.db.models import Q
from django.views.generic import TemplateView,CreateView,ListView
from  django.urls import reverse_lazy
# Create your views here.

class Index(ListView,CreateView):
    model = Inventario
    template_name = 'Tienda/index.html'
    queryset = Inventario.objects.filter(cantidad__gt=0)

    def get(self, request, *args, **kwargs):
        queryset = request.GET.get("buscar")
        posts = Inventario.objects.filter(cantidad__gt = 0)
        if queryset:
            posts = Inventario.objects.filter(
                Q(categoria_id__nombre__icontains=queryset) |
                Q(persona_id__nombre__icontains=queryset),
                categoria_id__gt=0
            ).distinct()
        return render(request,self.template_name,{'posts':posts})

    model = Carrito
    success_url = reverse_lazy('Index')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            print(request.POST)
            print('hola')
        return HttpResponse('')

class Registrar(CreateView):
    model = Cliente
    form_class = Cliente_form
    template_name = 'Tienda/register.html'
    success_url = reverse_lazy('login')

class Index_login(ListView):
    model = Inventario
    template_name = 'Tienda/indexLogin.html'
    queryset = Inventario.objects.filter(cantidad__gt=0)

    def get(self, request, *args, **kwargs):
        queryset = request.GET.get("buscar")
        object_list = Inventario.objects.filter(cantidad__gt = 0)
        if queryset:
            object_list = Inventario.objects.filter(
                Q(categoria_id__nombre__icontains = queryset) |
                Q(persona_id__nombre__icontains = queryset),
                categoria_id__gt=0
            ).distinct()
        return render(request,self.template_name,{'object_list':object_list})

class agregar_carrito(CreateView):
    model = Carrito
    template_name = 'Tienda/index.html'
    success_url = reverse_lazy('Index')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            print(request.POST)
            print('hola')
        return HttpResponse('')