# Generated by Django 4.2.4 on 2023-08-18 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuarios',
            new_name='Usuario',
        ),
    ]