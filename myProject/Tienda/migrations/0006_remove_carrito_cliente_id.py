# Generated by Django 3.1.2 on 2020-11-30 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0005_auto_20201130_0839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='cliente_id',
        ),
    ]
