from django.contrib import admin

# Register your models here.
from dashboard.models import *
# Modelo DigComp
admin.site.register(Areas)
admin.site.register(Competences)
admin.site.register(Linecompetences)
admin.site.register(Examples)
admin.site.register(Groups)
admin.site.register(Proficiencylevels)
admin.site.register(Competenciasusuario)

"""
  dashboard/migrations/0001_initial.py
    - Create model Areas
    - Create model Competences
    - Create model Examples
    - Create model Groups
    - Create model Linecompetences
    - Create model Proficiencylevels

  dashboard/migrations/0002_authuser.py
    - Create model AuthUser
        
    - Create model AuthGroup
    - Create model AuthGroupPermissions
    - Create model AuthPermission
    - Create model AuthUserGroups
    - Create model AuthUserUserPermissions
    - Create model DjangoAdminLog
    - Create model DjangoContentType
    - Create model DjangoMigrations
    - Create model DjangoSession

Migrations for 'dashboard':
  dashboard/migrations/0003_competenciasusuario.py
    - Create model Competenciasusuario

"""