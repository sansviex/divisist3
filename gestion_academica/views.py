# views.py
from rest_framework import viewsets
from .models import Usuario, Estudiante, Profesor, Curso, Evaluacion, Solicitud
from .serializers import UsuarioSerializer, EstudianteSerializer, ProfesorSerializer, CursoSerializer, EvaluacionSerializer, SolicitudSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class EvaluacionViewSet(viewsets.ModelViewSet):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer

class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

class EstadoEstudianteViewSet(viewsets.ModelViewSet):
    queryset = EstadoEstudiante.object.all()
    serializer_class = EstadoEstudianteSerializer

class AdministrativoViewSet(viewsets.ModelViewSet):
    queryset = Administrativo.object.all()
    serializer_class = AdministrativoSerializer
