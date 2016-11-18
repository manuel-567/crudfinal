from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Categoria(models.Model):
    """ Categorias para clasificar las fotos """
    Nombre_Categoria = models.CharField(max_length=50)
    Descripcion_Categoria = models.TextField()

    def __str__(self):
        return self.Nombre_Categoria

class Foto(models.Model):
    """ Fotos del album """
    Autor_Foto = models.ForeignKey('auth.User')
    Nombre_Foto = models.CharField(max_length=50,default='Sin titulo')
    Descripcion_Foto = models.CharField(max_length=200,blank=True)
    Fecha_Foto = models.DateTimeField(default=timezone.now)
    Archivo_Foto = models.ImageField(upload_to='media/Fotos/')
    categoria = models.ManyToManyField(Categoria,blank=True)
    ##categoria = models.ForeignKey(Categoria, null=True, blank=True,on_delete=models.CASCADE)
    ##categoria = models.ManyToManyField(Categoria, null=True, blank=True,on_delete=models.CASCADE)
    ##nombre = models.ManyToManyField(Categoria,null=True,blank=True)
    def publish(self):
        self.Fecha_Foto = timezone.now()
        self.save()

    def __str__(self):
        return self.Nombre_Foto

@receiver(post_delete, sender=Foto)
def photo_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.foto.delete(False)

class Puntuacion(models.Model):
    Autor_Puntuacion = models.ForeignKey('auth.User')
    Voto_Puntuacion = models.IntegerField(default=1,validators=[MaxValueValidator(10),MinValueValidator(1)])
    Comentario_Puntuacion = models.CharField(max_length=200,blank=True)
    foto = models.ForeignKey(Foto,on_delete = models.CASCADE)

    def __int__(self):
        return self.Voto_Puntuacion
##class comentario(models.Model)
