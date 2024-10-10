from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email_institucional = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128)
    telefono = models.CharField(max_length=15)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/')

    def registrarse(self):
        pass

    def iniciar_sesion(self):
        pass

    def recuperar_contrasena(self):
        pass

    def actualizar_informacion(self):
        pass

class Estudiante(Usuario):
    historial_academico = models.JSONField()  # o un modelo relacionado si se prefiere
    promedio = models.DecimalField(max_digits=4, decimal_places=2)
    creditos_acumulados = models.IntegerField()

    def visualizar_historial(self):
        pass

    def visualizar_horario(self):
        pass

    def inscribirse_curso(self):
        pass

    def consultar_calificaciones(self):
        pass

class Profesor(Usuario):
    cursos_asignados = models.ManyToManyField('Curso', related_name='profesores_asignados')  # Cambiado aquí

    def subir_recursos(self):
        pass

    def calificar_estudiantes(self):
        pass

    def enviar_retroalimentacion(self):
        pass

class Administrador(Usuario):
    def publicar_anuncios(self):
        pass

    def gestionar_anuncios(self):
        pass

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=100)
    descripcion = models.TextField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='cursos_impartidos')
    estudiantes = models.ManyToManyField(Estudiante, related_name='cursos')
    documentos = models.FileField(upload_to='documentos_cursos/')

    def agregar_documento(self):
        pass

    def consultar_estado(self):
        pass

class Evaluacion(models.Model):
    id_evaluacion = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)
    fecha = models.DateField()
    nota = models.FloatField()
    retroalimentacion = models.TextField()

    def agregar_calificacion(self):
        pass

    def consultar_nota(self):
        pass

class Notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha_envio = models.DateField(auto_now_add=True)

    def enviar(self):
        pass

class Solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now_add=True)

    def crear_solicitud(self):
        pass

    def comprobar_estado(self):
        pass
