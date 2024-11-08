from rest_framework import viewsets
from .models import Usuario, Estudiante, Profesor, Curso, Evaluacion, Solicitud
from .serializers import UsuarioSerializer, EstudianteSerializer, ProfesorSerializer, CursoSerializer, EvaluacionSerializer, SolicitudSerializer
from django.shortcuts import render

# view para gestionar usuarios (estudiante y profesores)
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# view especifica para estudiantes
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

# view especifica para profesores
class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

# view para gestionar los cursos
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# view para gestionar evaluaciones de los cursos
class EvaluacionViewSet(viewsets.ModelViewSet):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer

# view para gestionar solicitudes de estudiantes 
class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

class EstadoEstudianteViewSet(viewsets.ModelViewSet):
    queryset = EstadoEstudiante.object.all()
    serializer_class = EstadoEstudianteSerializer

class AdministrativoViewSet(viewsets.ModelViewSet):
    queryset = Administrativo.object.all()
    serializer_class = AdministrativoSerializer

def index(request): 
    return render (request, 'gestionacademica/index.html')