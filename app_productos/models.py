from django.db import models

# Create your models here.
class Productos(models.Model):
    id = models.AutoField(primary_key=True)  # Campo ID auto-incremental y clave primaria
    nombre = models.CharField(max_length=255, verbose_name="Nombre del Producto")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción del Producto")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Unitario")
    stock = models.IntegerField(default=0, verbose_name="Stock Disponible")
    modelo = models.CharField(max_length=100, blank=True, null=True, verbose_name="Modelo del Producto")

    def __str__(self):
        return self.nombre
    


    