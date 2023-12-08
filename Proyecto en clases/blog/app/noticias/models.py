from django.db import models
from app.usuarios.models import Usuario


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Noticia(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    resumen = models.CharField(max_length=200, null=True)
    fecha_publicacion = models.DateField('Data', auto_now_add=True)
    contenido = models.TextField('Texto')
    imagenes = models.ImageField(upload_to='noticias')
    categoria_noticia = models.ForeignKey(Categoria, on_delete= models.SET_NULL, null=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=Usuario.objects.get(is_superuser=True).pk)

    
    def __str__(self):
        return self.titulo


    