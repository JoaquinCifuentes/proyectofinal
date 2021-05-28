from django.shortcuts import render, HttpResponse, redirect
from .formulario import *
from .models import *
from apps.usuarios.models import *
from apps.inscripciones.models import *
from apps.cursos.models import *


def chat(request, cursoId):

    if request.method == "POST":
        formulario = FormularioChat(request.POST)
        print("%"*90)
        if formulario.is_valid():
            print(formulario.__dict__)
            # user = User.objects.get(id=request.session['id'])
            chat = formulario.save(commit=False)
            chat.participante = Usuario.objects.get(id=request.session["id"])
            chat.taller = Curso.objects.get(id=cursoId)
            chat.save()
            # formulario.save()
            
            return redirect('/chat/' + str(cursoId))
        else:
            print("no es valido")
            context={
                "formularioChat":formulario
            }
            return render(request, '(f"(/chat/{cursoId}")', context)
    else:

        context={
            "formularioChat": FormularioChat(),
            "misCursos":Inscripcion.objects.filter(participante__id=request.session["id"]),
            "chats" : Chat.objects.filter(taller=cursoId).order_by('-created_at'),
            "cursoId" : cursoId,
            "nombreCurso": Curso.objects.filter(id=cursoId).first()
        }


        return render(request, "chat/chat.html", context)