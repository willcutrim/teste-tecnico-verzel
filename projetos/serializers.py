from rest_framework import serializers
from .models import Projeto


class ProjetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'