from daos.dao import DAO
from model.pessoa import Pessoa

#cada entidade terá uma classe dessa, implementação bem simples.
class PessoaDAO(DAO):
    def __init__(self):
        super().__init__('pessoa.pkl')

    def add(self, pessoa: Pessoa):
        if((pessoa is not None) and isinstance(pessoa, Pessoa) and isinstance(pessoa.cpf, int)):
            super().add(pessoa.cpf, pessoa)

    def update(self, pessoa: Pessoa):
        if((pessoa is not None) and isinstance(pessoa, Pessoa) and isinstance(pessoa.cpf, int)):
            super().update(pessoa.cpf, pessoa)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)