from __future__ import unicode_literals
from django.db import models
from apps.cursos.models import *
from apps.usuarios.models import *


      
class Chat(models.Model):
    mensaje = models.CharField(max_length=250)
    participante = models.ForeignKey(Usuario, related_name="mensajes", on_delete=models.CASCADE)
    taller = models.ForeignKey(Curso, related_name="chats", on_delete=models.CASCADE, null=True)
    confirmado = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.mensaje}"
# Create your models here.
