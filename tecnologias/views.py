from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .business import TecnologiasBusiness
from .models import Tecnologia
from .serializers import TecnologiaSerializer
from bases.mixins import FilterByFieldsMixin


class TecnologiasListarTecnologiasListView(APIView):
    serializer_class = TecnologiaSerializer
    queryset = Tecnologia
    
    @property
    def tecnologias(self): 
        return self.queryset.objects.all() 

    def get(self, *args, **kwargs):
        tecnologias_serializer = self.serializer_class(self.tecnologias, many=True)
        return Response(tecnologias_serializer.data)


class TecnologiasPorFiltroView(FilterByFieldsMixin, APIView):
    serializer_class = TecnologiaSerializer
    queryset = Tecnologia
    filter_fields = ['id', 'nome']

    @property
    def tecnologias(self): 
        return self.queryset 

    def get(self, *args, **kwargs):
        tecnologia = self.tecnologias.objects.filter(projeto=kwargs['projeto_id'])
        tecnologia_serializer = self.serializer_class(tecnologia, many=True)
        return Response(tecnologia_serializer.data)


class TecnologiasCriarTecnologiaCreateView(APIView):
    serializer_class = TecnologiaSerializer
    business = TecnologiasBusiness()

    def post(self, *args, **kwargs):
        tecnologia = self.business.criar_tecnologia(**self.request.data)
        tecnologia_serializer = self.serializer_class(tecnologia)
        return Response(tecnologia_serializer.data)


class TecnologiasDeletarTecnologiaDeleteView(APIView):
    business = TecnologiasBusiness()

    def delete(self, *args, **kwargs):
        self.business.deletar_tecnologia(tecnologia_id=kwargs['tecnologia_id'])
        return Response({'message': 'Tecnologia deletada com sucesso'})
