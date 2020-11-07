from django.contrib.auth.forms import AuthenticationForm

class FomularioLogin(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(FomularioLogin,self).__init__(*args,**kwargs)
        self.fields['usuario'].widgets.attr['class'] = 'form-control'