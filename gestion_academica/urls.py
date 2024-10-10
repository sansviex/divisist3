# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gestion_academica.views import UsuarioViewSet, EstudianteViewSet, ProfesorViewSet, CursoViewSet, EvaluacionViewSet, \
    SolicitudViewSet, AdministrativoViewSet, EstadoEstudianteViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'estudiantes', EstudianteViewSet)
router.register(r'profesores', ProfesorViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'evaluaciones', EvaluacionViewSet)
router.register(r'solicitudes', SolicitudViewSet)
router.register(r'EstadoEstudiante', EstadoEstudianteViewSet)
router.register(r'administrativo', AdministrativoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
