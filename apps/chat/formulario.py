from django import forms
from django.core.exceptions import ValidationError
from .models import *
import apps.validaciones as validar
import apps.utilidades as util

   

class FormularioChat(forms.ModelForm):
    class Meta:
        model = Chat

        fields = ["mensaje"]