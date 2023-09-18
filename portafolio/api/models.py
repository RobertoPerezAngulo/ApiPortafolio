from django.db import models

# Create your models here.

class Register(models.Model):
    """
    Modelo para el registro de usuarios, para ponernos en contacto

    Respuestas:
    - 200 OK: Se devuelve la información de la torre.
    - 404 Not Found: Si la torre no existe.
    - 400 Bad Request: Si hay un problema en la solicitud.
    - 500 Internal Server Error: Si ocurre un error interno en el servidor.
    
    """
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(max_length=500, null=True)
    
    def __str__(self):
        return self.title

class Denuncia(models.Model):
    """
    Modelo para el registro de denuncias, para ponernos en contacto

    Respuestas:
    - 200 OK: Se devuelve la información de la torre.
    - 404 Not Found: Si la torre no existe.
    - 400 Bad Request: Si hay un problema en la solicitud.
    - 500 Internal Server Error: Si ocurre un error interno en el servidor.
    """
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.IntegerField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    descripcion = models.TextField(max_length=500)
    def __str__(self):
        return self.nombre
    
class About(models.Model):
    """
    Modelos para mi informacion
    
    Respuestas:
    - 200 OK: Se devuelve la información de la torre.
    - 404 Not Found: Si la torre no existe.
    - 400 Bad Request: Si hay un problema en la solicitud.
    - 500 Internal Server Error: Si ocurre un error interno en el servidor.
    """
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    
    def __str__(self):
        return self.title