from rest_framework import viewsets
from .serializer import RegisterSerializer
from .models import Register


# Create your views here.
class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = Register.objects.all()