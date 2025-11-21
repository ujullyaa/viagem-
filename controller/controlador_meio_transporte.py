from view.tela_meio_transporte import TelaMeioTransporte
from model.meio_transporte import MeioTransporte
from daos.meio_transporte_dao import MeioTransporteDAO

class ControladorMeioTransporte:
    def __init__(self, controlador_controladores, controlador_empresa_transporte):
        self.__meio_transporte_dao = MeioTransporteDAO()
        self.__tela_meio_transporte = TelaMeioTransporte()
        self.__controlador_controladores = controlador_controladores
        self.__controlador_empresa_transporte = controlador_empresa_transporte

    # --- ESTE É O MÉTODO QUE FALTAVA E CAUSAVA O ERRO ---
    def pega_meio_por_tipo(self, tipo):
        if not tipo:
            return None
        
        # Normaliza a string para comparação (remove espaços e joga para minúsculo)
        tipo_buscado = str(tipo).strip().lower()

        for meio in self.__meio_transporte_dao.get_all():
            # Compara o tipo salvo no banco com o digitado
            if meio.tipo.lower() == tipo_buscado:
                return meio
        return None

    # -------------------------------------------------------------------------
    def incluir_meio_transporte(self):
        # Verifica se existem empresas antes de começar
        empresas = list(self.__controlador_empresa_transporte.empresas)
        if not empresas:
            self.__tela_meio_transporte.mostra_mensagem(
                "Nenhuma empresa cadastrada! Cadastre uma empresa antes de cadastrar o veículo."
            )
            return

        # Pede os dados completos (Tipo e Capacidade)
        dados = self.__tela_meio_transporte.pega_dados_meio_transporte()
        if not dados:
            return # Cancelado

        try:
            capacidade = int(dados["capacidade"])
        except (ValueError, KeyError):
            self.__tela_meio_transporte.mostra_mensagem("Capacidade deve ser um número inteiro.")
            return

        tipo = dados["tipo"]

        # Selecionar empresa
        empresa = self.__tela_meio_transporte.seleciona_empresa(empresas)
        if not empresa:
            self.__tela_meio_transporte.mostra_mensagem("Nenhuma empresa selecionada. Cadastro cancelado.")
            return

        # Cria e Salva
        meio = MeioTransporte(tipo, capacidade, empresa)
        
        self.__meio_transporte_dao.add(meio)

        self.__tela_meio_transporte.mostra_mensagem(
            f"Meio '{meio.tipo}' cadastrado com sucesso!"
        )

    # -------------------------------------------------------------------------
    def lista_meio_transporte(self):
        meios = list(self.__meio_transporte_dao.get_all())
        self.__tela_meio_transporte.lista_meios(meios)

    # -------------------------------------------------------------------------
    def excluir_meio_transporte(self):
        meios = list(self.__meio_transporte_dao.get_all())
        if not meios:
            self.__tela_meio_transporte.mostra_mensagem("Nenhum meio cadastrado.")
            return

        meio_selecionado = self.__tela_meio_transporte.seleciona_meio_transporte(meios)
        
        if not meio_selecionado:
            return

        self.__meio_transporte_dao.remove(meio_selecionado)
        self.__tela_meio_transporte.mostra_mensagem("Meio de transporte excluído com sucesso!")

    # -------------------------------------------------------------------------
    def alterar_meio_transporte(self):
        meios = list(self.__meio_transporte_dao.get_all())
        if not meios:
            self.__tela_meio_transporte.mostra_mensagem("Nenhum meio cadastrado.")
            return

        meio_selecionado = self.__tela_meio_transporte.seleciona_meio_transporte(meios)
        if not meio_selecionado:
            return

        novos_dados = self.__tela_meio_transporte.pega_dados_meio_transporte(meio_selecionado)
        if not novos_dados:
            return

        try:
            nova_capacidade = int(novos_dados["capacidade"])
        except ValueError:
            self.__tela_meio_transporte.mostra_mensagem("Capacidade inválida.")
            return

        meio_selecionado.tipo = novos_dados["tipo"]
        meio_selecionado.capacidade = nova_capacidade
        
        self.__meio_transporte_dao.update(meio_selecionado)
        
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

        while True:
            opcao = self.__tela_meio_transporte.tela_opcoes()
            funcao = opcoes.get(opcao)

            if opcao == 0:
                self.retornar()
                break
            
            if funcao:
                funcao()
            else:
                self.__tela_meio_transporte.mostra_mensagem("Opção inválida.")