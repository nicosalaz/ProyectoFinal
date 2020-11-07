from django import forms
from .models import Cliente

class Cliente_form(forms.ModelForm):
    class Meta:
         model = Cliente
         fields = ['identificacion','nombre','apellido','telefono','direccion','fecha_nacimiento',
                  'usuario','password']
         label = {'identificacion':'Identificacion',
                  'nombre':'Nombre',
                  'apellido':'Apellido',
                  'telefono':'Telefono',
                  'direccion':'Dirección',
                  'fecha_nacimiento':'Fecha Nacimiento',
                  'usuario':'Usuario',
                  'password':'Password'}
         widgets ={
             'identificacion': forms.NumberInput(
                 attrs={
                     'class': 'form-control',
                     'placeholder': 'identificacion',
                     'autocomplete': 'off'
                 }),
             'nombre': forms.TextInput(
                 attrs={
                     'class': 'form-control',
                     'placeholder': 'Nombre',
                     'autocomplete': 'off'
                 }),
             'apellido': forms.TextInput(
                 attrs={
                     'class': 'form-control',
                     'placeholder': 'Apellido',
                     'autocomplete': 'off'
                 }),
             'telefono': forms.TextInput(
                 attrs={
                     'class': 'form-control',
                     'placeholder': 'Telefono',
                     'autocomplete': 'off'
                 }),
             'direccion': forms.TextInput(
                 attrs={
                     'class': 'form-control',
                     'placeholder': 'Direccion',
                     'autocomplete': 'off'
                 }),
             'password':forms.PasswordInput(
                 attrs={
                     'class':'form-control',
                     'placeholder':'Password',
                     'autocomplete':'off'
                 }),
             'usuario': forms.EmailInput(attrs={
                 'class': 'form-control',
                 'placeholder': 'Email',
                 'autocomplete': 'off'
             }),
             'fecha_nacimiento': forms.DateInput(attrs={
                 'type': 'date',
                 'class': 'form-control',
                 'placeholder': 'Fecha Nacimiento',
                 'autocomplete': 'off'
             }),
         }