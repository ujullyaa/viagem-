from model.pessoa import Pessoa


class ControladorPessoa:
    def __init__(self):
        self.pessoas = []

    def incluir_pessoa(self, nome: str, idade: int, cpf: str, telefone: str):
        for pessoa in self.pessoas:
            if pessoa in self.pessoas:
                raise ValueError(f"Pessoa ja cadastrada com cpf {cpf}.")
        nova_pessoa = Pessoa(nome, idade, cpf, telefone)
        self.pessoas.append(nova_pessoa)
        return nova_pessoa

    def listar_pesso(self):
        return self.pessoas

    def buscar_pessoa(self, cpf: str):
        for pessoa in self.pessoas:
            if pessoa.cpf == cpf:
                return pessoa
        return None

    def atualizar_pessoa(self, cpf: str, nome: str = None, idade: int = None, telefone: str = None):
        pessoa = self.buscar_pessoa(cpf)
        if pessoa:
            if nome:
                pessoa.nome = nome
            if idade:
                pessoa.idade = idade
            if telefone:
                pessoa.telefone = telefone
            return pessoa
        else:
            raise ValueError(f"Pessoa com CPF {cpf} nao encontrada")

    def excluir_pessoa(self, cpf: str):
        pessoa = self.buscar_pessoa(cpf)
        if pessoa:
            self.pessoa.remove(pessoa)
            return pessoa
        else:
            raise ValueError(f"Pessoa com CPF {cpf} não encontrada")
