from django.shortcuts import render, HttpResponse, redirect
from .formulario import *
from .models import *
from apps.usuarios.models import *
from apps.cursos.models import *
from datetime import datetime, date, time, timedelta
from dateutil.relativedelta import relativedelta
from time import strftime

def index(request):
    return HttpResponse("inscripciones")

def crear(request):
    if request.method == "POST":
        formulario = FormularioInscripcion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("../../cursos/crear/")
        else:
            context={
                "formularioInscripcion":formulario
            }
            return render(request, "inscripciones/inscribir.html", context)
    else:
        context={
            "formularioInscripcion": FormularioInscripcion(),
        }
        return render(request, "inscripciones/inscribir.html", context)

def inscribirAlumno(request, idCurso):
    if request.session["acceso"] == '0':
        esteCurso=Curso.objects.filter(id=idCurso).first()
        esteAlumno=Usuario.objects.filter(id=request.session["id"]).first()
        existeInscripcion = Inscripcion.objects.filter(participante=esteAlumno).filter(taller=esteCurso)
        print(len(existeInscripcion))
        if len(existeInscripcion)>0:
            return redirect("../../cursos/mostrar/")
        estaInscripcion=Inscripcion.objects.create(
            participante = esteAlumno,
            taller = esteCurso)
        return redirect("../../cursos/mostrar/")
    return redirect("../../cursos/mostrar/")
def miCalendario(request):
#################
    misCursos=Curso.objects.filter(inscripcionCurso__participante__id=request.session["id"])
    print("calendario")
    print(len(misCursos))
    fecha_hoy = datetime.strptime(strftime("%Y-%m-%d"), '%Y-%m-%d')
    diadelasemana=strftime("%w")
    esteLunes=date.today() - timedelta(days=int(diadelasemana)-1)
    esteMartes= esteLunes + timedelta(days=1)
    esteMiercoles= esteLunes + timedelta(days=2)
    esteJueves=esteLunes + timedelta(days=3)
    esteViernes=esteLunes + timedelta(days=4)
    esteSabado=esteLunes + timedelta(days=5)
    lunes=Inscripcion.objects.filter(taller__fecha=esteLunes).filter(participante__id=request.session["id"])
    martes=Inscripcion.objects.filter(taller__fecha=esteMartes).filter(participante__id=request.session["id"])
    miercoles=Inscripcion.objects.filter(taller__fecha=esteMiercoles).filter(participante__id=request.session["id"])
    jueves=Inscripcion.objects.filter(taller__fecha=esteJueves).filter(participante__id=request.session["id"])
    viernes=Inscripcion.objects.filter(taller__fecha=esteViernes).filter(participante__id=request.session["id"])
    
    proxLunes= esteLunes + timedelta(days=7)
    proxMartes= esteLunes + timedelta(days=8)
    proxMiercoles= esteLunes + timedelta(days=9)
    proxJueves=esteLunes + timedelta(days=10)
    proxViernes=esteLunes + timedelta(days=11)
    proxSabado=esteLunes + timedelta(days=12)
    proxlunes=Inscripcion.objects.filter(taller__fecha=proxLunes).filter(participante__id=request.session["id"])
    proxmartes=Inscripcion.objects.filter(taller__fecha=proxMartes).filter(participante__id=request.session["id"])
    proxmiercoles=Inscripcion.objects.filter(taller__fecha=proxMiercoles).filter(participante__id=request.session["id"])
    proxjueves=Inscripcion.objects.filter(taller__fecha=proxJueves).filter(participante__id=request.session["id"])
    proxviernes=Inscripcion.objects.filter(taller__fecha=proxViernes).filter(participante__id=request.session["id"])
    
    context={
            
            "lunes":lunes,
            "martes":martes,
            "miercoles":miercoles,
            "jueves":jueves,
            "viernes":viernes,
            "proxlunes":proxlunes,
            "proxmartes":proxmartes,
            "proxmiercoles":proxmiercoles,
            "proxjueves":proxjueves,
            "proxviernes":proxviernes,
            "dialunes":esteLunes.strftime("%d"),
            "diamartes":esteMartes.strftime("%d"),
            "diamiercoles":esteMiercoles.strftime("%d"),
            "diajueves":esteJueves.strftime("%d"),
            "diaviernes":esteViernes.strftime("%d"),
            "diaproxlunes":proxLunes.strftime("%d"),
            "diaproxmartes":proxMartes.strftime("%d"),
            "diaproxmiercoles":proxMiercoles.strftime("%d"),
            "diaproxjueves":proxJueves.strftime("%d"),
            "diaproxviernes":proxViernes.strftime("%d"),
            "fecha_hoy":fecha_hoy.strftime("%d-%B-%Y"),
    }
    return render(request, "inscripciones/miCalendario.html", context)
    
def mostrar(request):
    context={
        "inscripcionesTotales":Inscripcion.objects.filter(confirmado=1).order_by("taller__fecha")
    }
    return render(request, "inscripciones/mostrar.html", context)

def misCursos(request):
    
    context={
        "misCursos":Inscripcion.objects.filter(participante__id=request.session["id"]).order_by("taller__fecha")
    }
    return render(request, "inscripciones/misCursos.html", context)

def eliminarInscripcion(request, idInscripcion):
    estaInscripcion=Inscripcion.objects.get(id=idInscripcion)
    estaInscripcion.delete()
    #estaInscripcion.confirmado = 0
    #estaInscripcion.save()
    return redirect("../../cursos/mostrar")



    pass
# Create your views here.
