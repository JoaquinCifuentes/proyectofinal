from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat, name="chat"),
    path("<int:cursoId>", views.chat, name="chat"),
]