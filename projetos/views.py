from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .business import ProjetosBusiness
from .models import Projeto
from .serializers import ProjetosSerializer


class ProjetosCriarProjetoCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    model = Projeto
    business = ProjetosBusiness
    serializer_class = ProjetosSerializer

    def post(self, *args, **kwargs):
        projeto = self.business.criar_projeto(**kwargs)
        projeto_serializer = self.serializer_class(projeto)
        return Response(projeto_serializer.data)


class ProjetosListarTodosProjetosListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    model = Projeto
    serializer_class = ProjetosSerializer

    @property
    def projetos(self):
        return self.model.objects.all()

    def get(self, *args, **kwargs):
        projetos_serializer = self.serializer_class(self.projetos, many=True)
        return Response(projetos_serializer.data)


class ProjetosFiltrarPorIDView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    model = Projeto
    serializer_class = ProjetosSerializer

    @property
    def projeto(self):
        return self.model.objects.filter(id=self.kwargs['projeto_id'])

    def get(self, *args, **kwargs):
        projeto_serializer = self.serializer_class(self.projeto)
        return Response(projeto_serializer.data)
    

class ProjetosDeletarProjetoDeleteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    model = Projeto
    business = ProjetosBusiness

    def delete(self, *args, **kwargs):
        projeto_business = self.business.deletar_projeto(**kwargs)
        if not projeto_business:
            return Response({'message': 'Projeto nao encontrado'}, status=404)

        return Response({'message': 'Projeto deletado com sucesso'})
    

class ProjetosAtualizarProjetoUpdateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    model = Projeto
    business = ProjetosBusiness

    def put(self, *args, **kwargs):
        projeto = self.business.atualizar_projeto(**kwargs)
        if not projeto:
            return Response({'message': 'Projeto nao encontrado'}, status=404)

        projeto_serializer = self.serializer_class(projeto)
        return Response(projeto_serializer.data)