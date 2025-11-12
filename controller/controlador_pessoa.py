from model.pessoa import Pessoa
from view.tela_pessoa import TelaPessoa
from daos.pessoa_dao import PessoaDAO

class ControladorPessoa:
    def __init__(self, controlador_controladores):
        self.__pessoa_dao = PessoaDAO()
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_controladores = controlador_controladores

    def pega_pessoa_por_cpf(self, cpf):
        for pessoa in self.__pessoa_dao.get_all:
            if pessoa.cpf == cpf:
                return pessoa
        return None

    def incluir_pessoa(self):
        dados = self.__tela_pessoa.pega_dados_pessoa()
        if dados:
            if self.pega_pessoa_por_cpf(dados["cpf"]) is None:
                pessoa = Pessoa(
                    dados["nome"],
                    dados["idade"],
                    dados["cpf"],
                    dados["telefone"]
                )
                self.__pessoa_dao.add(pessoa)
                self.__tela_pessoa.mostra_mensagem(
                    "Pessoa cadastrada com sucesso!")
            else:
                self.__tela_pessoa.mostra_mensagem("CPF já cadastrado!")
        else:
            self.__tela_pessoa.mostra_mensagem(
                "Dados inválidos. Cadastro cancelado.")

    def alterar_pessoa(self):
        self.listar_pessoas()
        cpf = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.pega_pessoa_por_cpf(cpf)

        if pessoa:
            novos_dados = self.__tela_pessoa.pega_dados_pessoa()
            if novos_dados:
                pessoa.nome = novos_dados["nome"]
                pessoa.idade = novos_dados["idade"]
                pessoa.cpf = novos_dados["cpf"]
                pessoa.telefone = novos_dados["telefone"]
                self.__tela_pessoa.mostra_mensagem(
                    "Pessoa alterada com sucesso!")
            else:
                self.__tela_pessoa.mostra_mensagem(
                    "Alteração cancelada. Dados inválidos.")
        else:
            self.__tela_pessoa.mostra_mensagem("Pessoa não encontrada.")

    def listar_pessoas(self):
        if not self.__pessoa_dao.get_all:
            self.__tela_pessoa.mostra_mensagem("Nenhuma pessoa cadastrada.")
        else:
            for pessoa in self.__pessoa_dao.get_all:
                self.__tela_pessoa.mostra_pessoa({
                    "nome": pessoa.nome,
                    "idade": pessoa.idade,
                    "cpf": pessoa.cpf,
                    "telefone": pessoa.telefone
                })

    def excluir_pessoa(self):
        self.listar_pessoas()
        cpf = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.pega_pessoa_por_cpf(cpf)

        if pessoa:
            self.__pessoa_dao.remove(pessoa)
            self.__tela_pessoa.mostra_mensagem("Pessoa excluída com sucesso!")
        else:
            self.__tela_pessoa.mostra_mensagem("Pessoa não encontrada.")

    def retornar(self):
        print("Retornando ao menu principal...")
        self.__controlador_controladores.inicializa_sistema()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_pessoa,
            2: self.alterar_pessoa,
            3: self.listar_pessoas,
            4: self.excluir_pessoa,
            0: self.retornar
        }

        sair = False
        while not sair:
            opcao = self.__tela_pessoa.tela_opcoes()
            funcao = lista_opcoes.get(opcao)
            if funcao:
                if opcao == 0:
                    sair = True
                    funcao()
                else:
                    funcao()
            else:
                print("Opção inválida. Tente novamente.")
