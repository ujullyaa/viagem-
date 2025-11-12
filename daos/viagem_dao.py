from daos.dao import DAO
from model.viagem import Viagem

class ViagemDAO(DAO):
    def __init__(self):
        super().__init__('viagem.pkl')

    def add(self, viagem: Viagem):
        if viagem is not None:
            super().add(viagem.codigo_viagem, viagem)

    def update(self, viagem: Viagem):
        if viagem is not None:
            super().update(viagem.codigo_viagem, viagem)

    def get(self, codigo_viagem: int):
        return super().get(codigo_viagem)

    def remove(self, codigo_viagem: int):
        super().remove(codigo_viagem)

    def get_all(self):
        return list(super().get_all())
