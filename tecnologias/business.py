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
