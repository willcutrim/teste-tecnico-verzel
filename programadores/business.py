from programadores.models import Programador


class ProgramadoresBusiness:
    model_object = Programador

    @property
    def programadores(self):
        return self.model_object
    
    def criar_programador(self, **kwargs):
        try:
            return self.programadores.objects.create(**kwargs)
        
        except Exception as err:
            raise Exception('Erro ao criar programador')

    def deletar_programador(self, **kwargs):
        def _get_programador(**kwargs):
            try:
                programador = self.programadores.objects.get(id=kwargs.get('programador_id'))
                return programador
            
            except self.programadores.DoesNotExist:
                return None
        
        try:
            programador = _get_programador(**kwargs)
            if not programador:
                return None

            programador.delete()

        except Exception as err:
            raise Exception('Erro ao deletar programador')