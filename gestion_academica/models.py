from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

# Manager para el modelo de usuario
class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El correo electrónico es obligatorio")
        email = self.normalize_email(email)
        usuario = self.model(email=email, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

# Clase base de Usuario
class Usuario(AbstractUser):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email_institucional = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

    # Agregar related_name para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios_gestion_academica',
        blank=True,
        help_text='Los grupos a los que pertenece el usuario.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_gestion_academica',
        blank=True,
        help_text='Permisos específicos del usuario.'
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo Estudiante
class Estudiante(Usuario):
    historial_academico = models.JSONField(null=True, blank=True)
    promedio = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    creditos_acumulados = models.IntegerField(default=0)

    def __str__(self):
        return f"Estudiante: {self.nombre} {self.apellido}"

# Modelo Profesor
class Profesor(Usuario):
    cursos_asignados = models.ManyToManyField('Curso', related_name='profesores')

    def __str__(self):
        return f"Profesor: {self.nombre} {self.apellido}"

# Modelo Administrador
class Administrador(Usuario):
    def __str__(self):
        return f"Administrador: {self.nombre} {self.apellido}"

# Modelo Curso
class Curso(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    estudiantes = models.ManyToManyField(Estudiante, related_name='cursos_inscritos', blank=True)

    def __str__(self):
        return f"Curso: {self.nombre}"

# Modelo Documento
class Documento(models.Model):
    tipo = models.CharField(max_length=50)
    titulo = models.CharField(max_length=100)
    fecha_subida = models.DateField(auto_now_add=True)
    archivo = models.FileField(upload_to='documentos/')

    def __str__(self):
        return f"Documento: {self.titulo}"

# Modelo Evaluacion
class Evaluacion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='evaluaciones')
    tipo = models.CharField(max_length=50)
    fecha = models.DateField()
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    retroalimentacion = models.TextField(blank=True)

    def __str__(self):
        return f"Evaluacion: {self.tipo} en {self.curso.nombre}"

# Modelo Notificacion
class Notificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='notificaciones')
    tipo = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notificacion: {self.tipo} para {self.usuario.email}"

# Modelo Solicitud
class Solicitud(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitudes')
    tipo = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud: {self.tipo} por {self.usuario.email}"
