from rest_framework import viewsets
from .serializer import *
from .models import Register

class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = Register.objects.all()

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class DenunciaViewSet(viewsets.ModelViewSet):
    serializer_class = DenunciaSerializer
    queryset = Denuncia.objects.all()

class AboutViewSet(viewsets.ModelViewSet):
    serializer_class = AboutSerializer
    queryset = About.objects.all()