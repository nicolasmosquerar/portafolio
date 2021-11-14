from django.db import models
from django.db.models import ImageField
from django.db.models.fields import CharField, TextField, URLField


# Create your models here.


class proyecto(models.Model):

    titulo  =   CharField(max_length=100)
    descripcion =   TextField(max_length=255)
    imagenes    =   ImageField(upload_to='portafolio/imagenes/')
    url =  URLField(blank=True)


