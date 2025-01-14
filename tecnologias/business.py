from .models import Tecnologia

class TecnologiasBusiness:
    model_object = Tecnologia

    @property
    def tecnologias(self):
        return self.model_object

    def criar_tecnologia(self, **kwargs):
        try:
            tecnologia = self.tecnologias.objects.create(nome=kwargs.get('nome'))
            return tecnologia

        except Exception as err:
            raise Exception('Erro ao criar tecnologia')

    def atualizar_tecnologia(self, **kwargs):
        def _get_tecnologia(id_tecnologia):
            try:
                tecnologia = self.tecnologias.objects.get(id=id_tecnologia)
                return tecnologia
            
            except self.tecnologias.DoesNotExist:
                return None

        try:
            tecnologia = _get_tecnologia(kwargs.get('tecnologia_id'))
            if not tecnologia:
                return None

            tecnologia.nome = kwargs.get('nome')
            tecnologia.save()

            return tecnologia

        except Exception as err:
            raise Exception('Erro ao atualizar tecnologia')

    def deletar_tecnologia(self, **kwargs):
        def _get_tecnologia(**kwargs):
            try:
                tecnologia = self.tecnologias.objects.get(id=kwargs.get('tecnologia_id'))
                return tecnologia
            
            except self.tecnologias.DoesNotExist:
                return None

        try:
            tecnologia = _get_tecnologia(**kwargs)
            if not tecnologia:
                return None

            tecnologia.delete()

        except Exception as err:
            raise Exception('Erro ao deletar tecnologia')
