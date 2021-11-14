from datetime import datetime

from django.db import models
from django.db.models import CharField, TextField, ImageField, DateField


class post(models.Model):

    titulo= CharField(max_length=100)
    descripcion=TextField()
    imagen=ImageField(upload_to='blog/images')
    fecha= DateField()