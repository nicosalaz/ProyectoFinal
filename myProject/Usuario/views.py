from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout
from .forms import FomularioLogin
# Create your views here.
class Login(FormView):
    template_name = 'Tienda/login.html'
    form_class = FomularioLogin
    success_url = reverse_lazy('Index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            #print('entro al dispatch')
            return HttpResponseRedirect(self.get_success_url())
        else:
            #print('entro al else')
            return super(Login, self).dispatch(request,*args,**kwargs)
    def form_valid(self, form):
        #print('entro al form_valid')
        login(self.request,form.get_user())
        return super(Login, self).form_valid(form)

def logout_usuario(request):
    logout(request)
    return HttpResponseRedirect('/Indexlog/')