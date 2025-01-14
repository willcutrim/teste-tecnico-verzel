from rest_framework import serializers
from .models import Alocacao


class AlocacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alocacao
        fields = '__all__'
