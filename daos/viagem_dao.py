
from daos.dao import DAO
from model.viagem import Viagem


class ViagemDAO(DAO):
    def __init__(self):
        super().__init__('viagem.pkl')

    def add(self, viagem: Viagem):
        if viagem is not None:
            super().add(viagem.codigo, viagem)

    def update(self, viagem: Viagem):
        if viagem is not None:
            super().update(viagem.codigo, viagem)

    def get(self, codigo: int):
        return super().get(codigo)

    def remove(self, codigo: int):
        super().remove(codigo)

    def get_all(self):
        return list(super().get_all())
