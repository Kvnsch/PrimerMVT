from django.http import HttpResponse
from appFamilia.models import Familiar
from django.template import loader
from django.shortcuts import render
# Create your views here.


def inicio(request):
    return HttpResponse()

def familiaList(request):
    familiar1 = Familiar(nombre='Agustin Perez', nacimiento=('1990-03-25'), numFavorito=19) 
    familiar1.save()

    familiar2 = Familiar(nombre='Rodrigo Silva',nacimiento=('1992-09-05'), numFavorito=33)
    familiar2.save()

    familiar3 = Familiar(nombre='Gabriela Rodriguez',nacimiento='1968-02-29',numFavorito=91)    
    familiar3.save()

    familiares = Familiar.objects.all()

    return render( request, 'index.html', {"familiares":familiares
        })
  
 
 