from daos.dao import DAO
from model.passagem import Passagem

class PassagemDAO(DAO):
    def __init__(self):
        super().__init__('passagem.pkl')

    def add(self, passagem: Passagem):
        if passagem is not None:
            super().add(passagem.numero, passagem)

    def update(self, passagem: Passagem):
        if passagem is not None:
            super().update(passagem.numero, passagem)

    def get(self, numero: str):
        return super().get(numero)

    def remove(self, numero: str):
        super().remove(numero)

    def get_all(self):
        return list(super().get_all())
