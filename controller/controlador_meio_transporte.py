# controller/controlador_meio_transporte.py
from view.tela_meio_transporte import TelaMeioTransporte
from model.meio_transporte import MeioTransporte
from daos.meio_transporte_dao import MeioTransporteDAO

class ControladorMeioTransporte:
    def __init__(self, controlador_controladores, controlador_empresa_transporte):
        self.__meio_transporte_dao = MeioTransporteDAO()
        self.__tela_meio_transporte = TelaMeioTransporte()
        self.__controlador_controladores = controlador_controladores
        self.__controlador_empresa_transporte = controlador_empresa_transporte

    # -------------------------------------------------------------------------
    # PROTEÇÃO: garante que tipo nunca cause erro caso seja None
    # -------------------------------------------------------------------------
    def pega_meio_por_tipo(self, tipo):
        if not tipo:  # None, "", [], etc.
            return None

        tipo = str(tipo).strip().lower()

        for meio in self.__meio_transporte_dao.get_all():
            # compara com segurança (protege None)
            if getattr(meio, "tipo", "").strip().lower() == tipo:
                return meio
        return None

    # -------------------------------------------------------------------------
    def incluir_meio_transporte(self):
        empresas = list(self.__controlador_empresa_transporte.empresas)


        if not empresas:
            self.__tela_meio_transporte.mostra_mensagem(
                "Nenhuma empresa de transporte cadastrada! Cadastre uma primeiro."
            )
            return

        # -------- 1) Selecionar tipo (lista fixa: Onibus, Carro, Avião) --------
        tipo = self.__tela_meio_transporte.seleciona_meio_transporte()
        if not tipo:
            self.__tela_meio_transporte.mostra_mensagem("Cadastro cancelado.")
            return

        # -------- 2) Pegar capacidade --------
        dados = self.__tela_meio_transporte.pega_dados_meio_transporte()
        if not dados:
            self.__tela_meio_transporte.mostra_mensagem("Cadastro cancelado.")
            return

        try:
            capacidade = int(dados["capacidade"])
        except (ValueError, KeyError):
            self.__tela_meio_transporte.mostra_mensagem("Capacidade deve ser um número.")
            return

        # -------- 3) Selecionar empresa --------
        empresa = self.__tela_meio_transporte.seleciona_empresa(empresas)
        if not empresa:
            self.__tela_meio_transporte.mostra_mensagem("Nenhuma empresa selecionada.")
            return

        # Criar e salvar (tipo armazenado como string; DAO usa tipo como chave)
        meio = MeioTransporte(tipo.strip().title(), capacidade, empresa)
        self.__meio_transporte_dao.add(meio)

        self.__tela_meio_transporte.mostra_mensagem(
            f"Meio de transporte '{meio.tipo}' cadastrado com sucesso!"
        )

    # -------------------------------------------------------------------------
    def lista_meio_transporte(self):
        meios = list(self.__meio_transporte_dao.get_all())

        if not meios:
            self.__tela_meio_transporte.mostra_mensagem("Nenhum meio de transporte cadastrado.")
            return

        self.__tela_meio_transporte.lista_meios(meios)

    # -------------------------------------------------------------------------
    def excluir_meio_transporte(self):
        meios = list(self.__meio_transporte_dao.get_all())

        # seleciona_meio_transporte aceita opcionalmente a lista de meios (retorna o tipo selecionado)
        tipo = self.__tela_meio_transporte.seleciona_meio_transporte(meios)
        if not tipo:
            self.__tela_meio_transporte.mostra_mensagem("Nenhum meio selecionado.")
            return

        meio = self.pega_meio_por_tipo(tipo)
        if not meio:
            self.__tela_meio_transporte.mostra_mensagem("Meio não encontrado.")
            return

        # DAO usa 'tipo' como chave
        self.__meio_transporte_dao.remove(meio.tipo)

        self.__tela_meio_transporte.mostra_mensagem(
            f"Meio de transporte '{meio.tipo}' excluído com sucesso!"
        )

    # -------------------------------------------------------------------------
    def alterar_meio_transporte(self):
        meios = list(self.__meio_transporte_dao.get_all())

        tipo = self.__tela_meio_transporte.seleciona_meio_transporte(meios)
        if not tipo:
            self.__tela_meio_transporte.mostra_mensagem("Nenhum meio selecionado.")
            return

        meio = self.pega_meio_por_tipo(tipo)
        if not meio:
            self.__tela_meio_transporte.mostra_mensagem("Meio não encontrado.")
            return

        novos = self.__tela_meio_transporte.pega_dados_meio_transporte(meio)
        if not novos:
            self.__tela_meio_transporte.mostra_mensagem("Alteração cancelada.")
            return

        meio.tipo = novos["tipo"].strip().title()

        try:
            meio.capacidade = int(novos["capacidade"])
        except (ValueError, KeyError):
            self.__tela_meio_transporte.mostra_mensagem("Capacidade inválida.")
            return

        # mantém a mesma empresa a menos que a tela permita trocar (aqui não alteramos empresa)
        self.__meio_transporte_dao.update(meio)
        self.__tela_meio_transporte.mostra_mensagem("Meio atualizado com sucesso!")

    # -------------------------------------------------------------------------
    def retornar(self):
        self.__controlador_controladores.inicializa_sistema()

    # -------------------------------------------------------------------------
    def abre_tela(self):
        opcoes = {
            1: self.incluir_meio_transporte,
            2: self.alterar_meio_transporte,
            3: self.lista_meio_transporte,
            4: self.excluir_meio_transporte,
            0: self.retornar
        }

        sair = False
        while not sair:
            opcao = self.__tela_meio_transporte.tela_opcoes()
            funcao = opcoes.get(opcao)

            if opcao == 0:
                sair = True

            if funcao:
                funcao()
            else:
                self.__tela_meio_transporte.mostra_mensagem("Opção inválida.")
