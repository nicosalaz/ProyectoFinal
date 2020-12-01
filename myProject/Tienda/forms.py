from django import forms
from .models import Cliente,Carrito

class Cliente_form(forms.ModelForm):
    class Meta:
         model = Cliente

         fields = ['identificacion','nombre','apellido','telefono','direccion','fecha_nacimiento','usuario','password']

         label = {'identificacion':'identificacion',
                  'nombre':'nombre',
                  'apellido':'apellido',
                  'telefono':'telefono',
                  'direccion':'direccion',
                  'fecha_nacimiento': 'fecha_nacimiento',
                  'usuario': 'usuario',
                  'password': 'password'
                  }

         widgets ={
             'identificacion': forms.NumberInput(
                 attrs={
                     'class': 'form-control',
                     'placeholder': 'Identificacion',
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
             'fecha_nacimiento': forms.DateInput(
                 attrs={
                     'class': 'form-control',
                     'type':'date',
                     'placeholder': 'Fecha_nacimiento',
                     'autocomplete': 'off'
                 }),
             'usuario': forms.EmailInput(
                 attrs={
                     'class': 'form-control',
                     'placeholder': 'Usuario',
                     'autocomplete': 'off'
                 }),
             'password': forms.PasswordInput(
                 attrs={
                     'class': 'form-control',
                     'placeholder': 'Password',
                     'autocomplete': 'off'
                 })
         }
class Carrito_form(forms.ModelForm):
    class Meta:
        model = Carrito
        fields = ['cantidad_producto','cliente_id','inventario_id','precio_unidad']

        label = {'cantidad_producto': 'cantidad_producto',
                 'cliente_id': 'cliente_id',
                 'inventario_id': 'inventario_id',
                 'precio_unidad': 'precio_unidad'

                 }
        widgets = {
            'cantidad_producto': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'cantidad producto',
                    'autocomplete': 'off'
                }),
            'cliente_id': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'precio_unidad',
                    'autocomplete': 'off'
                }),
            'inventario_id': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'inventario_id',
                    'autocomplete': 'off'
                }),
            'precio_unidad': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'precio_unidad',
                    'autocomplete': 'off'
                })
        }