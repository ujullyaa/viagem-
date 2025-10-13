from view.tela_passagem import TelaPassagem
from model.passagem import Passagem
from model.pessoa import Pessoa
from model.pagamento import Pagamento
from model.meio_transporte import MeioTransporte

class ControladorPassagem:
    def __init__(self, controlador_controladores):
        self.__passagens = []
        self.__tela_passagem = TelaPassagem()
        self.__controlador_controladores = controlador_controladores

    def pega_passagem_por_numero(self, numero: int):
        for passagem in self.__passagens:
            if passagem.numero == numero:
                return passagem
        return None

    def incluir_passagem(self):
        dados_passagem = self.__tela_passagem.pega_dados_passagem()
        if not dados_passagem:
            self.__tela_passagem.mostra_mensagem(" Dados inválidos.")
            return

        # Cria a passagem (sem vincular objetos reais de Pessoa/Pagamento ainda)
        passagem = Passagem(
            dados_passagem["numero"],
            dados_passagem["assento"],
            dados_passagem["data_viagem"],
            dados_passagem["valor"],
            pessoa=dados_passagem["pessoa"],
            pagamento=dados_passagem["pagamento"],
            meio_transporte=dados_passagem["meio_transporte"]
        )

        self.__passagens.append(passagem)
        self.__tela_passagem.mostra_mensagem(" Passagem cadastrada com sucesso!")

    def listar_passagens(self):
        if not self.__passagens:
            self.__tela_passagem.mostra_mensagem(" Nenhuma passagem cadastrada.")
            return

        for passagem in self.__passagens:
            self.__tela_passagem.mostra_passagem({
                "numero": passagem.numero,
                "assento": passagem.assento,
                "data_viagem": passagem.data_viagem,
                "valor": passagem.valor,
                "pessoa": passagem.pessoa,
                "pagamento": passagem.pagamento,
                "meio_transporte": passagem.meio_transporte
            })

    def alterar_passagem(self):
        numero = self.__tela_passagem.seleciona_passagem()
        passagem = self.pega_passagem_por_numero(numero)

        if passagem:
            novos_dados = self.__tela_passagem.pega_dados_passagem()
            if not novos_dados:
                self.__tela_passagem.mostra_mensagem(" Dados inválidos.")
                return

            passagem.numero = novos_dados["numero"]
            passagem.assento = novos_dados["assento"]
            passagem.data_viagem = novos_dados["data_viagem"]
            passagem.valor = novos_dados["valor"]
            passagem.pessoa = novos_dados["pessoa"]
            passagem.pagamento = novos_dados["pagamento"]
            passagem.meio_transporte = novos_dados["meio_transporte"]

            self.__tela_passagem.mostra_mensagem(" Passagem alterada com sucesso!")
        else:
            self.__tela_passagem.mostra_mensagem(" Passagem não encontrada.")

    def excluir_passagem(self):
        self.listar_passagens()
        numero = self.__tela_passagem.seleciona_passagem()
        passagem = self.pega_passagem_por_numero(numero)

        if passagem:
            self.__passagens.remove(passagem)
            self.__tela_passagem.mostra_mensagem(" Passagem excluída com sucesso!")
        else:
            self.__tela_passagem.mostra_mensagem(" Passagem não encontrada.")

    def retornar(self):
        self.__controlador_controladores.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_passagem,
            2: self.alterar_passagem,
            3: self.listar_passagens,
            4: self.excluir_passagem,
            0: self.retornar
        }

        continua = True
        while continua:
            opcao = self.__tela_passagem.tela_opcoes()
            funcao = opcoes.get(opcao)
            if funcao:
                funcao()
            else:
                self.__tela_passagem.mostra_mensagem(" Opção inválida!")
            if opcao == 0:
                continua = False

