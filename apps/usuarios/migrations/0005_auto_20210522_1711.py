# Generated by Django 2.2.4 on 2021-05-22 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20210521_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='acceso',
            field=models.CharField(choices=[('0', 'alumno'), ('1', 'profesor'), ('9', 'administrador')], default=0, max_length=1),
        ),
    ]
