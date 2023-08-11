from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Perro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=256)
    raza = models.CharField(max_length=256)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=20, blank=True)
    duenio = models.CharField(max_length=256)
    foto = models.ImageField(null=True, blank=True, upload_to='media')

    class Meta:
        ordering = ['usuario', '-foto']

    def __str__(self):
        return f"{self.nombre}, {self.raza}"


class Comentario(models.Model):
    comentario = models.ForeignKey(Perro, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)
