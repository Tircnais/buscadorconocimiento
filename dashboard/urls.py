from django.urls import path
# para USAR url en lugar de PATH
from django.conf.urls import include
# para acceso controlado por LOGEO 
from django.contrib.auth.views import login_required

from . import views

# es necesario importar las VISTAS
from .views import *

# PARA LAS API
from rest_framework import routers
# Routers para las API (Ej. http://127.0.0.1:8000/panel/api/niveles/)
# La API necesita un Serializador, Vista y esta ruta
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('areasdigcomp', AreasdViewSet)
router.register('competencias', CompetencesViewSet)
router.register('grupos', GroupViewSet)
router.register('niveles', NivelesdViewSet)
router.register('det_competencias', DetalleCompetenciaViewSet)
router.register('ejemplo', EjemploCompetenciaViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    # PARA LAS API
    path('api/', include(router.urls)),
    # path('^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # Registro de Usuarios
    path('registro', RegistroUsuario.as_view(), name='nuevoUs'),
    path('misCompetencias/', CompetenciasUsuarioListView.as_view(), name='misComp'),
    path('registroCompetencias/', RegistroCompetenciasView.as_view(), name='nuevasComp'),
    # path('actualizarCompetencias/', ActualizarCompetenciasView.as_view(), name='actualizarComp'),
    path('actualizarCompetencias/<int:pk>', ActualizarCompetenciasView.as_view(), name='actualizarComp'),
    
    # Funciones Ajax
    path(r'detalleCompetencia/', views.DetalleCompetencia, name='ajaxDetalleComp'),
]