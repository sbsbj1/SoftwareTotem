from django.db import models

# Create your models here.

class Region (models.Model): 
    idRegion = models.IntegerField(primary_key=True, verbose_name='Id de Region')
    nombreRegion= models.CharField(max_length=50, verbose_name='Nombre de Region')

    def __str__(self):
        return self.nombreRegion


class Cliente(models.Model):
    rut = models.CharField(max_length=10, primary_key=True, verbose_name='Rut')
    nombre= models.CharField(max_length=20, verbose_name='Nombre')
    apellido=models.CharField(max_length=40, verbose_name='Apellido')
    direccion=models.CharField(max_length=40, verbose_name='Direccion')
    region=models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut
