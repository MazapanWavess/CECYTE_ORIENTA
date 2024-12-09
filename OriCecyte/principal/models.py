from django.db import models

# Create your models here.

class Reserva(models.Model):
    nombre = models.CharField(max_length=255)
    grupo = models.CharField(max_length=255)
    servicio = models.CharField(max_length=255)
    fecha_hora = models.CharField(max_length=255)
    motivo = models.TextField(blank=True, null=True)
    contacto = models.CharField(max_length=255)

    def __str__(self):
        return f"Reserva de {self.nombre} para {self.servicio} en {self.fecha_hora}"