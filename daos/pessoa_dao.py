from daos.dao import DAO
from model.pessoa import Pessoa

class PessoaDAO(DAO):
    def __init__(self):
        super().__init__('pessoa.pkl')

    def add(self, pessoa: Pessoa):
        if pessoa is not None:
            super().add(pessoa.cpf, pessoa)

    def update(self, pessoa: Pessoa):
        if pessoa is not None:
            super().update(pessoa.cpf, pessoa)

    def get(self, cpf: str):
        return super().get(cpf)

    def remove(self, cpf: str):
        super().remove(cpf)

    def get_all(self):
        return list(super().get_all())
