from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .business import AlocacoesBusiness
from .models import Alocacao
from .serializers import AlocacaoSerializer


class AlocacoesAllListView(APIView):
    serializer_class = AlocacaoSerializer
    queryset = Alocacao
    
    @property
    def alocacoes(self): 
        return self.queryset.objects.all() 

    def get(self, *args, **kwargs):
        alocacores_serializer = self.serializer_class(self.alocacoes, many=True)

        return Response(alocacores_serializer.data)


class AlocacoesPorProjetoView(APIView):
    queryset = Alocacao

    @property
    def alocacoes(self): 
        return self.queryset 

    def get(self, *args, **kwargs):
        alocacao = self.alocacoes.objects.filter(projeto=kwargs['projeto_id'])
        alocacao_serializer = AlocacaoSerializer(alocacao)

        return Response(alocacao_serializer.data)


class AlocacoesCriarAlocaaoCreateView(APIView):
    serializer_class = AlocacaoSerializer
    queryset = Alocacao
    business = AlocacoesBusiness

    def post(self, *args, **kwargs):
        alocacao = self.business.criar_alocacao(**kwargs)

        alocacao_serializer = self.serializer_class(alocacao)

        return Response(alocacao_serializer.data)
        

class AlocacoesDeletarAlocaaoDeleteView(APIView):
    business = AlocacoesBusiness

    def delete(self, *args, **kwargs):
        self.business.deletar_alocacao(alocacao_id=kwargs['alocacao_id'])
        return Response({'message': 'Alocação deletada com sucesso'})