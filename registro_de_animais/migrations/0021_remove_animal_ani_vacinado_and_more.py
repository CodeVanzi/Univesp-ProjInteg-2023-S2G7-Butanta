# Generated by Django 4.2.1 on 2023-05-24 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro_de_animais', '0020_animal_ani_peso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='ani_vacinado',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='ani_vermifugado',
        ),
    ]