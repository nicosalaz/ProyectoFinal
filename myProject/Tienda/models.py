from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50,null=False,blank=False)
    contenido = models.CharField(max_length=100,null=False,blank=False)
    especificacion = models.TextField(max_length=100,null=False,blank=False)

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    especificacion = models.TextField(max_length=100)

class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    cantidad = models.FloatField(blank=False,null=False)
    persona_id = models.ForeignKey(Producto,on_delete=models.CASCADE,null=False)
    categoria_id = models.ForeignKey(Categoria,on_delete=models.CASCADE,null=False)

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    identificacion = models.IntegerField(null=False,blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    telefono = models.CharField(max_length=20, null=False, blank=False)
    direccion = models.CharField(max_length=20, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False)
    usuario = models.EmailField(max_length=200)
    password = models.CharField(max_length=30,null=False,blank=False)

class Carrito(models.Model):
    id_carrito = models.AutoField(primary_key = True)
    cantidad_producto = models.IntegerField(null=False,blank=False)
    cliente_id = models.ForeignKey(Cliente,on_delete=models.CASCADE,null=False)
    inventario_id = models.ForeignKey(Inventario,on_delete=models.CASCADE)
