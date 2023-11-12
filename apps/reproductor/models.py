# En tu archivo reproductor/models.py
from django.db import models

class Cancion(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='canciones_fotos/', null=True, blank=True)
    archivo_musical = models.FileField(upload_to='canciones/')
