# Generated by Django 4.2.4 on 2023-08-31 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_ventascliente_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventascliente',
            name='numeroEntradas',
            field=models.IntegerField(),
        ),
    ]
