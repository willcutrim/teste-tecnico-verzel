from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .business import AlocacoesBusiness
from .models import Alocacao
from .serializers import AlocacaoSerializer


class AlocacoesAllListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = AlocacaoSerializer
    model = Alocacao
    
    @property
    def alocacoes(self):
        return self.model

    def get(self, *args, **kwargs):
        alocacores_serializer = self.serializer_class(self.alocacoes, many=True)
        return Response(alocacores_serializer.data)


class AlocacoesPorProjetoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    model = Alocacao

    @property
    def alocacoes(self): 
        return self.model 

    def get(self, *args, **kwargs):
        alocacao = self.alocacoes.objects.filter(projeto=kwargs['projeto_id'])
        alocacao_serializer = AlocacaoSerializer(alocacao)

        return Response(alocacao_serializer.data)


class AlocacoesCriarAlocaaoCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = AlocacaoSerializer
    business = AlocacoesBusiness

    def post(self, *args, **kwargs):
        alocacao = self.business.criar_alocacao(**kwargs)

        alocacao_serializer = self.serializer_class(alocacao)

        return Response(alocacao_serializer.data)
        

class AlocacoesDeletarAlocaaoDeleteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    business = AlocacoesBusiness

    def delete(self, *args, **kwargs):
        self.business.deletar_alocacao(alocacao_id=kwargs['alocacao_id'])
        return Response({'message': 'Alocação deletada com sucesso'})