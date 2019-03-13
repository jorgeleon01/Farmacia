from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=60)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60)
    precio = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre