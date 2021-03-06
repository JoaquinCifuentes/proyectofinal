# Generated by Django 2.2.4 on 2021-05-22 05:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)])),
                ('descripcion', models.CharField(max_length=250, validators=[django.core.validators.MinLengthValidator(2)])),
                ('fecha', models.DateField()),
                ('ubicacion', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('capacidad', models.FloatField(default=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
