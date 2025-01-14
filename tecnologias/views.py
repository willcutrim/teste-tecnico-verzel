from rest_framework.views import APIView
from rest_framework.response import Response
from .business import TecnologiasBusiness
from .models import Tecnologia
from .serializers import TecnologiaSerializer


class TecnologiasListarTecnologiasListView(APIView):
    serializer_class = TecnologiaSerializer
    queryset = Tecnologia
    
    @property
    def tecnologias(self): 
        return self.queryset.objects.all() 

    def get(self, *args, **kwargs):
        tecnologias_serializer = self.serializer_class(self.tecnologias, many=True)
        return Response(tecnologias_serializer.data)


class TecnologiasBuscarPorIDView(APIView):
    serializer_class = TecnologiaSerializer
    queryset = Tecnologia

    @property
    def tecnologia(self):
        try:
            return self.queryset.objects.get(id=self.kwargs.get('tecnologia_id'))

        except self.queryset.DoesNotExist:
            return None

    def get(self, *args, **kwargs):
        if not self.tecnologia:
            return Response({'message': 'Tecnologia não encontrada'}, status=404)

        tecnologia_serializer = self.serializer_class(self.tecnologia)
        return Response(tecnologia_serializer.data)


class TecnologiasCriarTecnologiaCreateView(APIView):
    serializer_class = TecnologiaSerializer
    business = TecnologiasBusiness()

    def post(self, *args, **kwargs):
        tecnologia = self.business.criar_tecnologia(**self.request.data)
        tecnologia_serializer = self.serializer_class(tecnologia)
        return Response(tecnologia_serializer.data)


class TecnologiasAtualizarTecnologiaUpdateView(APIView):
    serializer_class = TecnologiaSerializer
    business = TecnologiasBusiness()

    def put(self, *args, **kwargs):
        tecnologia = self.business.atualizar_tecnologia(**self.request.data, **kwargs)
        tecnologia_serializer = self.serializer_class(tecnologia)
        return Response(tecnologia_serializer.data)


class TecnologiasDeletarTecnologiaDeleteView(APIView):
    business = TecnologiasBusiness()

    def delete(self, *args, **kwargs):
        programador = self.business.deletar_tecnologia(**kwargs)
        if not programador:
            return Response({'message': 'Tecnologia nao encontrada'}, status=404)
        
        return Response({'message': 'Tecnologia deletada com sucesso'})
