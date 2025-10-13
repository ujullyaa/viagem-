from model.pessoa import Pessoa
from view.tela_pessoa import TelaPessoa


class ControladorPessoa:
    def __init__(self, controlador_controladores):
        self.__pessoas = []
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_controladores = controlador_controladores

    def pega_pessoa_por_cpf(self, cpf):
        for pessoa in self.__pessoas:
            if pessoa.cpf == cpf:
                return pessoa
        return None

    def incluir_pessoa(self):
        dados = self.__tela_pessoa.pega_dados_pessoa()
        if self.__pega_pessoa_por_cpf(dados["cpf"]) is None:
            self.__tela_pessoa.mostra_mensagem("CPF cadastrado com sucesso!")
        else:
            pessoa = Pessoa(dados["nome"], dados["cpf"], dados["telefone"])
            self.__pessoas.append(pessoa)
            self.__tela_pessoa.mostra_mensagem(
                "Pessoa cadastrada com sucesso!")

    def alterar_pessoa(self):
        self.__listar_pessoas()
        cpf = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.__pega_pessoa_por_cpf(cpf)

        if pessoa is not None:
            novos_dados = self.__tela_pessoa.pega_dados_pessoa()
            pessoa.nome = novos_dados["nome"]
            pessoa.idade = novos_dados["idade"]
            pessoa.telefone = novos_dados["telefone"]
            self.__tela_pessoa.mostra_mensagem("Pessoa alterada com sucesso!")
        else:
            self.__tela_pessoa.mostra_mensagem("Pessoa não encontrada.")

    def listar_pessoas(self):
        if not self.__pessoas:
            self.__tela_pessoa.mostra_mensagem("Nenhuma pessoa cadastrada.")
        else:
            for pessoa in self.__pessoas:
                self.__tela_pessoa.mostra_pessoa({
                    "nome": pessoa.nome,
                    "idade": pessoa.idade,
                    "cpf": pessoa.cpf,
                    "telefone": pessoa.telefone
                })

    def excluir_pessoa(self):
        self.__listar_pessoas()
        cpf = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.__pega_pessoa_por_cpf(cpf)

        if pessoa is not None:
            self.__pessoas.remove(pessoa)
            self.__tela_pessoa.mostra_mensagem("Pessoa excluída com sucesso!")
        else:
            self.__tela_pessoa.mostra_mensagem("Pessoa não encontrada.")

    def retornar(self):
        self.__controlador_controladores.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_pessoa,
            2: self.alterar_pessoa,
            3: self.listar_pessoas,
            4: self.excluir_pessoa,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_pessoa.mostra_opcoes()
            funcao = lista_opcoes.get(opcao)
            if funcao:
                funcao()
            else:
                break
