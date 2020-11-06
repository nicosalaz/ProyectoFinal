from django import forms
from .models import Cliente

class Cliente_form(forms.ModelForm):
     class Meta:
         model = Cliente
         fields = ['identificacion','nombre','apellido','telefono','direccion','fecha_nacimiento',
                  'usuario','password']
         widgets ={
             'password':forms.PasswordInput(),
             'usuario': forms.EmailInput(),
             'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
         }