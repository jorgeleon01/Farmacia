from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=60)

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60)
