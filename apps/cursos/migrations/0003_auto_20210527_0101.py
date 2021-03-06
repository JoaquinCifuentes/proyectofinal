# Generated by Django 2.2.4 on 2021-05-27 05:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_curso_activo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ['fecha']},
        ),
        migrations.AlterField(
            model_name='curso',
            name='capacidad',
            field=models.FloatField(default=10, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(2)]),
        ),
    ]
