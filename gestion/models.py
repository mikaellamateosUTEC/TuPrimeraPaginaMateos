from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    
    def __str__(self):
        return self.nombre

class Tester(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre

class CasoPrueba(models.Model):

    PRIORIDAD_CHOICES = [
        ('Alta', 'Alta'),
        ('Media', 'Media'),
        ('Baja', 'Baja'),
    ]

    id_caso = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precondiciones = models.TextField()
    datos_entrada = models.TextField(null=True, blank=True)
    pasos_ejecutar = models.TextField()
    resultado_esperado = models.TextField()
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, default='Media')
    dependencias = models.TextField(blank=True, null=True)
    notas = models.TextField(blank=True, null=True)
    
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    tester = models.ForeignKey(Tester, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_caso} - {self.nombre}"
