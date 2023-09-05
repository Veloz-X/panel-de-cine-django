from django.db import models

class Pelicula(models.Model):
    name = models.CharField(max_length=200)
    img = models.CharField(max_length=200,default='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/mBgynPDplmo5JTY9VfGqY35OjDu.jpg')
    
    def __str__(self):
        return self.name

class VentasCliente(models.Model):
    nombre = models.CharField(max_length=200)
    cedula = models.CharField(max_length=200)
    numeroEntradas = models.IntegerField()
    fecha = models.CharField(max_length=200)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    entrada2x1 = models.BooleanField(default=False)
    
    def __str__(self):
        return self.pelicula.name