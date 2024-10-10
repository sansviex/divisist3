# serializers.py
from rest_framework import serializers
from .models import Usuario, Estudiante, Profesor, Curso, Evaluacion, Solicitud

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'correo', 'telefono', 'es_profesor']

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = '__all__'

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'
