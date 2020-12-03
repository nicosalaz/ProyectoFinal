from django.test import TestCase
from .models import *
from .views import *
from .forms import *
import unittest

class Test_models(unittest.TestCase):

    def setUp(self):
        self.form_cli = Cliente_form()
        self.datos_correctos = {'identificacion': '17362546',
                 'nombre': 'Daniela',
                 'apellido': 'Torres',
                 'telefono': '3014567892',
                 'direccion': 'cll 45 # 12-32',
                 'fecha_nacimiento': '1995-05-12',
                 'usuario': 'daniT@gmail.com',
                 'password': 'daniTorres'}
        self.datos_incorrectos = {'nombre': 'Daniela',
                                'telefono': '3014567892',
                                'direccion': 'cll 45 # 12-32',
                                'fecha_nacimiento': '1995-05-12',
                                'usuario': 'daniT@gmail.com',
                                'password': 'daniTorres'}


    def test_model_producto(self):
        pro = Producto.objects.create(nombre = "Botella de Agua",
                                    contenido = "250ml",
                                    especificacion = "Botella de agua para resfrescar tu dia")
        pro_ver = Producto.objects.filter(nombre = pro.nombre).exists()
        self.assertEqual(str(pro),"Botella de Agua")
        self.assertTrue(pro_ver,'Si existe el producto')
        Producto.objects.filter(nombre=pro.nombre).delete()

    def test_model_Categoria(self):
        cat = Categoria.objects.create(nombre = 'Lacteos',
                                        especificacion = 'Productos con contenido de lactosa')
        cat_ver = Categoria.objects.filter(nombre = cat.nombre).exists()
        self.assertEqual(str(cat),'Lacteos')
        self.assertTrue(cat_ver,'si existe la categoria')
        Categoria.objects.filter(nombre=cat.nombre).delete()


    def test_cliente(self):
        cl = Cliente.objects.create(
            identificacion=17362546,
            nombre = 'Daniela',
            apellido = 'Torres',
            telefono = '3014567892',
            direccion = 'cll 45 # 12-32',
            fecha_nacimiento = '1995-05-12',
            usuario = 'daniT@gmail.com',
            password = 'daniTorres'
        )
        verificar = Cliente.objects.filter(nombre = cl.nombre).exists()
        self.assertEqual(cl.nombre,'Daniela')
        self.assertTrue(verificar, 'si existe el cliente')
        Cliente.objects.filter(nombre=cl.nombre).delete()

    def test_form_cliente(self):
        fomulario = Cliente_form(data=self.datos_correctos)
        self.assertTrue(fomulario.is_valid())
        formulario2 = Cliente_form(data = self.datos_incorrectos)
        self.assertFalse(formulario2.is_valid())




if __name__ == '__main__':
    unittest.main()
