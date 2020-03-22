from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField( verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(verbose_name="URL", null=True, blank = True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    #La sig. clase nos permite cambiar los nombre de los campos (estan en inglés) por los que especifiquemos en las sig.variables.
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        #Nos permite ordenar los proyectos de manera descendente.
        ordering = ["-created"]
        
    #Con el sig. metodo conseguiremos mostrar el título del proyecto en vez de lo que salía por defecto en el panel de administración.
    def __str__(self):
        return self.title