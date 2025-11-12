from daos.dao import DAO
from model.passagem import Passagem

# Implementação DAO para Passagem
class PassagemDAO(DAO):
    def __init__(self):
        super().__init__('passagem.pkl')

    def add(self, passagem: Passagem):
        if((passagem is not None) and isinstance(passagem, Passagem) and isinstance(passagem.numero, int)):
            super().add(passagem.numero, passagem)

    def update(self, passagem: Passagem):
        if((passagem is not None) and isinstance(passagem, Passagem) and isinstance(passagem.numero, int)):
            super().update(passagem.numero, passagem)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if(isinstance(key, int)):
            return super().remove(key)
