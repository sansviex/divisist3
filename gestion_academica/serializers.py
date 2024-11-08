from rest_framework import serializers
from .models import Usuario, Estudiante, Profesor, Curso, Evaluacion, Solicitud

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'codigo', 'nombre', 'correo', 'telefono', 'es_profesor', 'foto_perfil']

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ['id', 'codigo', 'nombre', 'correo', 'promedio', 'creditos_acumulados', 'telefono', 'foto_perfil']
       

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ['id', 'codigo', 'nombre', 'correo', 'telefono', 'departamento']
      

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'codigo', 'nombre', 'descripcion', 'creditos']
       

class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = ['id', 'curso', 'fecha', 'descripcion', 'nota']
       

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ['id', 'estudiante', 'tipo_solicitud', 'estado', 'fecha_creacion']
      
