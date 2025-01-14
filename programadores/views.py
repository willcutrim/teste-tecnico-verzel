from django.shortcuts import render
from rest_framework import viewsets
from .models import Programador
from .serializers import ProgramadorSerializer

# Create your views here.

class ProgramadorViewSet(viewsets.ModelViewSet):
    queryset = Programador.objects.all()
    serializer_class = ProgramadorSerializer
