from django.contrib import admin
from .models import Project

# Register your models here.
# Con la sig.clase conseguiremos extender las funcionalidades del panel de administración
class ProjectAdmin(admin.ModelAdmin):
    #El contenido de la sig. Tupla son los campos de nuestra tabla Projects
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmin)
