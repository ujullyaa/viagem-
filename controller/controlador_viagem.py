from view.tela_viagem import TelaViagem
from model.viagem import Viagem
from model.pessoa import Pessoa
from viajem import ViagemDAO

class ControladorViagem:
    def __init__(self, controlador_controladores):
        self.__viagem_dao = ViagemDAO()
        self.__tela_viagem = TelaViagem()
        self.__controlador_controladores = controlador_controladores

    def pega_viagem_por_codigo(self, codigo: int):
        for viagem in self.__viagem_dao.get_all:
            if viagem.codigo == codigo:
                return viagem
        return None

    def incluir_viagem(self):
        dados_viagem = self.__tela_viagem.pega_dados_viagem()

        if self.pega_viagem_por_codigo(dados_viagem["codigo"]) is not None:
            self.__tela_viagem.mostra_mensagem("Viagem já existente!")
            return

        cpf = dados_viagem["pessoa"]
        pessoa = self.__controlador_controladores.controlador_pessoa.pega_pessoa_por_cpf(
            cpf)
        if pessoa is None:
            self.__tela_viagem.mostra_mensagem(
                "Pessoa não encontrada. Cadastre antes de incluir a viagem.")
            return

        nova_viagem = Viagem(
            codigo=dados_viagem["codigo"],
            data_partida=dados_viagem["data_partida"],
            data_chegada=dados_viagem["data_chegada"],
            itinerario=dados_viagem["itinerario"],
            meio_transporte=dados_viagem["meio_transporte"],
            empresa_transporte=dados_viagem["empresa_transporte"],
            pagamento=dados_viagem["pagamento"],
            pessoa=pessoa
        )

        self.__viagem_dao.add(nova_viagem)
        self.__tela_viagem.mostra_mensagem("Viagem cadastrada com sucesso!")

    def listar_viagens(self):
        if not self.__viagem_dao.get_all:
            self.__tela_viagem.mostra_mensagem("Nenhuma viagem cadastrada.")
            return

        for viagem in self.__viagem_dao.get_all:
            self.__tela_viagem.mostra_viagem({
                "codigo": viagem.codigo,
                "data_partida": viagem.data_partida,
                "data_chegada": viagem.data_chegada,
                "itinerario": viagem.itinerario,
                "meio_transporte": viagem.meio_transporte,
                "empresa_transporte": viagem.empresa_transporte,
                "pagamento": viagem.pagamento,
                "pessoa": viagem.pessoa.nome
            })

    def reservar_viagem(self):
        self.listar_viagens()
        codigo = self.__tela_viagem.seleciona_viagem()
        viagem = self.pega_viagem_por_codigo(codigo)

        if viagem is None:
            self.__tela_viagem.mostra_mensagem("Viagem não encontrada.")
            return

        passageiro_nome = input("Nome do passageiro: ")
        assento = input("Número do assento: ")
        # Cria Pessoa temporária com dados mínimos
        passageiro = Pessoa(passageiro_nome, idade=0, cpf="", telefone="")
        reserva = viagem.reservar_passagem(passageiro, assento)

        if reserva:
            self.__tela_viagem.mostra_mensagem(
                "Reserva realizada com sucesso!")
        else:
            self.__tela_viagem.mostra_mensagem("Falha ao reservar passagem.")

    def cancelar_viagem(self):
        codigo = self.__tela_viagem.seleciona_viagem()
        viagem = self.pega_viagem_por_codigo(codigo)

        if viagem is None:
            self.__tela_viagem.mostra_mensagem("Viagem não encontrada.")
            return

        num_passagem = input("Número da passagem a cancelar: ")
        if viagem.cancelar_passagem(num_passagem):
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
            self.__viagem_dao.remove(viagem)
            self.__tela_viagem.mostra_mensagem("Viagem excluída com sucesso!")
        else:
            self.__tela_viagem.mostra_mensagem("Viagem não encontrada.")

    def retornar(self):
        self.__controlador_controladores.inicializa_sistema()

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

        sair = False
        while not sair:
            opcao = self.__tela_viagem.tela_opcoes()
            funcao = opcoes.get(opcao)
            if funcao:
                if opcao == 0:
                    sair = True
                funcao()
            else:
                self.__tela_viagem.mostra_mensagem("Opção inválida.")
