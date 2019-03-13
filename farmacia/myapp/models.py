from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombrec = models.CharField(max_length=60)

class Producto(object):
    categoria = models.Foreignkey(Categoria)
    nombrep = models.CharField(max_length=60)
