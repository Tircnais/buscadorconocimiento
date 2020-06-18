from django.shortcuts import render, redirect

from dashboard.models import *
from django.template import RequestContext

# Create your views here.
from django.http import HttpResponse
from django.http import Http404

def index(request):
    cntxtIndex = {}
    mensaje = "index_ buscador"
    cntxtIndex = {
        'mensaje': mensaje,
    }
    return render(request, "base.html", cntxtIndex)


# Detalle de Digcomp
def abstractDigcomp():
    areaDigcomp = Areas.objects.all()
    competenciasDigcomp = Competences.objects.all()
    context = {
        'areaD': areaDigcomp,
        'competenciasDigcomp': competenciasDigcomp,
    }
    return context

"""
class BuscaCompetencesAPI(viewsets.ModelViewSet, request):
    idAreaD = request.GET.get('ididAreaD')
    queryset = Competences.objects.filter(fkarea=idAreaD)
    serializer_class = CompetencesSerializer
"""
