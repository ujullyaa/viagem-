from daos.dao import DAO
from model.pessoa import Pessoa

class PessoaDAO(DAO):
    def __init__(self):
        super().__init__('pessoa.pkl')

    def add(self, pessoa: Pessoa):
        if pessoa is not None and isinstance(pessoa, Pessoa):
            super().add(pessoa.cpf, pessoa)

    def update(self, pessoa: Pessoa):
        if pessoa is not None and isinstance(pessoa, Pessoa):
            super().update(pessoa.cpf, pessoa)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
