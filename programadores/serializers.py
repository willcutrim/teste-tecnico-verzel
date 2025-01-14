from rest_framework import serializers
from .models import Programador

class ProgramadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programador
        fields = '__all__'
