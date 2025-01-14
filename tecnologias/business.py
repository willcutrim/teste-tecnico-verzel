from .models import Tecnologia

class TecnologiasBusiness:
    model_object = Tecnologia

    @property
    def tecnologias(self):
        return self.model_object

    def criar_tecnologia(self, **kwargs):
        tecnologia = self.tecnologias.objects.create(nome=kwargs.get('nome'))
        return tecnologia

    def deletar_tecnologia(self, tecnologia_id):
        tecnologia = self.tecnologias.objects.get(id=tecnologia_id)
        tecnologia.delete()
