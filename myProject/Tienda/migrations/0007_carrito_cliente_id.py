# Generated by Django 3.1.2 on 2020-11-30 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0006_remove_carrito_cliente_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='cliente_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Tienda.cliente'),
            preserve_default=False,
        ),
    ]