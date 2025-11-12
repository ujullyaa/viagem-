from daos.dao import DAO
from model.viagem import Viagem

# Implementação DAO para Viagem
class ViagemDAO(DAO):
    def __init__(self):
        super().__init__('viagem.pkl')

    def add(self, viagem: Viagem):
        if((viagem is not None) and isinstance(viagem, Viagem) and isinstance(viagem.codigo, str)):
            super().add(viagem.codigo, viagem)

    def update(self, viagem: Viagem):
        if((viagem is not None) and isinstance(viagem, Viagem) and isinstance(viagem.codigo, str)):
            super().update(viagem.codigo, viagem)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if(isinstance(key, str)):
            return super().remove(key)
