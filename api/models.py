from django.db import models

# Create your models here.
class Prueba(models.Model):
    id_prueba = models.AutoField(primary_key=True)
    edad = models.IntegerField()
    fecha = models.DateField()
    descripcion = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=9, decimal_places=2)
    
    class Meta:
        db_table = 'prueba'