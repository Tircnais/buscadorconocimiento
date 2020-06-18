from django.urls import path

# es necesario importar las VISTAS
from . import views

urlpatterns = [
    path('', views.index, name='busca_home'),
    path(route='', view=views.abstractDigcomp, name='busca_abs'),
    
]