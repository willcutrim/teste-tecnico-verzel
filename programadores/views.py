from rest_framework.views import APIView
from rest_framework.response import Response

from programadores.business import ProgramadoresBusiness
from programadores.serializers import ProgramadorSerializer

from .models import Programador


class ProgramadoresListarTodosProgramadoresListView(APIView):
    queryset = Programador
    serializer_class = ProgramadorSerializer

    @property
    def programadores(self):
        return self.queryset.objects.all()

    def get(self, *args, **kwargs):
        programadores_serializer = self.serializer_class(self.programadores, many=True)
        return Response(programadores_serializer.data)


class ProgramadoresCriarProgramadorView(APIView):
    queryset = Programador
    serializer_class = ProgramadorSerializer
    business = ProgramadoresBusiness

    @property
    def programador(self):
        return self.queryset

    def post(self, *args, **kwargs):
        programador = self.business.criar_programador(**self.request.data)
        programador_serializer = self.serializer_class(programador)
        return Response(programador_serializer.data)


class ProgramadoresFiltrarPorIDView(APIView):
    queyset = Programador
    serializer_class = ProgramadorSerializer

    @property
    def programador(self):
        try:
            return self.queryset.objects.get(id=self.kwargs.get('programador_id'))

        except self.queyset.DoesNotExist:
            return None

    def get(self, *args, **kwargs):
        programador_serializer = self.serializer_class(self.programador)
        return Response(programador_serializer.data)


class ProgramadoresDeletarProgramadorDeleteView(APIView):
    business = ProgramadoresBusiness()

    def delete(self, *args, **kwargs):
        programdor = self.business.deletar_programador(**kwargs)
        if not programdor:
            return Response({'message': 'Programador nao encontrado'}, status=404)

        return Response({'message': 'Programador deletado com sucesso'})
