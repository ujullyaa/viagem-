from view.tela_viagem import TelaViagem
from model.viagem import Viagem
from model.pessoa import Pessoa
from model.itinerario import Itinerario
from model.meio_transporte import MeioTransporte
from model.empresa_transporte import EmpresaTransporte
from model.pagamento import Pagamento


class ControladorViagem():
    def __init__(self, controlador_controladores):
        self.__viagens = []
        self.__tela_viagem = TelaViagem()
        self.__controlador_controladores = controlador_controladores

    def pega_viagem_por_codigo(self, codigo: int):
        for viagem in self.__viagens:
            if viagem.codigo == codigo:
                return viagem
        return None

    def incluir_viagem(self):
        dados_viagem = self.__tela_viagem.pega_dados_viagem()

        if self.__pega_viagem_por_codigo(dados_viagem["codigo"]) is None:
            self.__tela_viagem.mostra_mensagem("Viagem ja existente!")
            return

        nova_viagem = Viagem(
            codigo=dados_viagem["codigo"],
            data_partida=dados_viagem["data_partida"],
            data_chegada=dados_viagem["data_chegada"],
            itinerario=dados_viagem["itinerario"],
            meio_transporte=dados_viagem["meio_transporte"],
            empresa_transporte=dados_viagem["empresa_transporte"],
            pagamento=dados_viagem["pagamento"],
            pessoa=dados_viagem["pessoa"]

        )

        self.__viagens.append(Viagem)
        self.__tela_viagem.mostra_mensagem("Viagem cadastrada com sucesso!")

    def listar_viagens(self):
        if not self.__viagens:
            self.__tela_viagem.mostra_mensagem("Nenhuma viagem cadastrada.")
            return
        for viagem in self.__viagens:
            self.__tela_viagem.mostra_viagem({
                "codigo": viagem.codigo,
                "data_partida": viagem.data_partida,
                "data_chegada": viagem.data_chegada,
                "itinerario": viagem.itinerario,
                "meio_transporte": viagem.meio_transporte,
                "empresa_transporte": viagem.empresa_transporte,
                "pagamento": viagem.pagamento,
                "pessoa": viagem.pessoa
            })

    def reservar_viagem(self):
        self.listar_viagens()
        codigo = self.__tela_viagem.seleciona_viagem()
        viagem = self.pega_viagem_por_codigo(codigo)

        if viagem is None:
            self.__tela_viagem.mostra_mensagem("Viagem não encontrada.")
            return

        passageiro = input("Nome do passageiro: ")
        assento = input("Número do assento: ")
        reserva = viagem.reservar_passagem(
            Pessoa(passageiro, idade=0), assento)
        if reserva:
            self.__tela_viagem.mostra_mensagem(
                "Reserva realizada com sucesso!")
        else:
            self.__tela_viagem.mostra_mensagem("Falha ao reserva passagem.")

    def cancelar_viagem(self):
        codigo = self.__tela_viagem.seleciona_viagem()
        viagem = self.pega_viagem_por_codigo(codigo)
        if viagem is None:
            self.__tela_viagem.mostra_mensagem("Viagem não encontrada.")
            return

        num_pasasagem = input("Número da passagem a cancelar: ")
        if viagem.cancelar_passagem(num_pasasagem):
            self.__tela_viagem.mostra_mensagem(
                "Passagem cancelada com sucesso!")
        else:
            self.__tela_viagem.mostra_mensagem("Falha ao cancelar passagem.")

    def atualizar_viagem(self):
        codigo = self.__tela_viagem.seleciona_viagem()
        viagem = self.pega_viagem_por_codigo(codigo)
        if viagem:
            novo_status = input("Novo status da viagem: ")
            viagem.atualizar_status(novo_status)
            self.__tela_viagem.mostra_mensagem(
                "Status atualizado com sucesso!")
        else:
            self.__tela_viagem.mostra_mensagem("Viagem não encontrada.")

    def excluir_viagem(self):
        codigo = self.__tela_viagem.seleciona_viagem()
        viagem = self.pega_viagem_por_codigo(codigo)

        if viagem:
            self.__viagens.remove(viagem)
            self.__tela_viagem.mostra_mensagem("Viagem excluída com sucesso!")
        else:
            self.__tela_viagem.mostra_mensagem("Viagem não encontrada.")

    def retornar(self):
        self.__controlador_controladores.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_viagem,
            2: self.listar_viagens,
            3: self.reservar_viagem,
            4: self.cancelar_viagem,
            5: self.atualizar_viagem,
            6: self.excluir_viagem,
            0: self.retornar
        }
        while True:
            opcao = self.__tela_viagem.tela_opcoes()
            funcao = opcoes.get(opcao)
            if funcao:
                funcao()
            else:
                self.__tela_viagem.mostra_mensagem("Opção inválida.")
