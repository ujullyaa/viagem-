from daos.dao import DAO
from model.pessoa import Pessoa

class PessoaDAO(DAO):
    def __init__(self):
        super().__init__('pessoa.pkl')

    def add(self, pessoa: Pessoa):
        if isinstance(pessoa, Pessoa) and pessoa is not None:
            super().add(pessoa.cpf, pessoa)

    def update(self, pessoa: Pessoa):
        if isinstance(pessoa, Pessoa) and pessoa is not None:
            # Atualiza baseado na chave (CPF)
            super().update(pessoa.cpf, pessoa)

    def get(self, cpf: str):
        return super().get(cpf)

    def remove(self, cpf: str):
        # O remove do DAO pai espera a chave (cpf), não o objeto
        if isinstance(cpf, str):
            super().remove(cpf)

    def get_all(self):
        return list(super().get_all())