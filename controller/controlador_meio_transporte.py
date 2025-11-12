from view.tela_meio_transporte import TelaMeioTransporte
from model.meio_transporte import MeioTransporte
from daos.meio_transporte_dao import MeioTransporteDAO

class ControladorMeioTransporte:
    def __init__(self, controlador_controladores, controlador_empresa_transporte):
        self.__meio_transporte_dao = MeioTransporteDAO()
        self.__tela_meio_transporte = TelaMeioTransporte()
        self.__controlador_controladores = controlador_controladores
        self.__controlador_empresa_transporte = controlador_empresa_transporte

    def pega_meio_por_tipo(self, tipo):
        tipo = tipo.strip().lower()
        for meio in self.__meio_transporte_dao.get_all():
            if meio.tipo.strip().lower() == tipo:
                return meio
        return None

    def incluir_meio_transporte(self):
        empresas = self.__controlador_empresa_transporte.empresas
        if not empresas:
            self.__tela_meio_transporte.mostra_mensagem(
                "Nenhuma empresa de transporte cadastrada! Cadastre uma primeiro."
            )
            return

        dados_meio_transporte = self.__tela_meio_transporte.pega_dados_meio_transporte()
        if not dados_meio_transporte:
            self.__tela_meio_transporte.mostra_mensagem("Dados inválidos.")
            return

        tipo = dados_meio_transporte["tipo"].strip().title()
        try:
            capacidade = int(dados_meio_transporte["capacidade"])
        except ValueError:
            self.__tela_meio_transporte.mostra_mensagem("Capacidade deve ser um número.")
            return

        self.__tela_meio_transporte.mostra_mensagem("Escolha a empresa responsável:")
        for i, empresa in enumerate(empresas, start=1):
            print(f"{i}. {empresa.nome_empresa} - CNPJ: {empresa.cnpj}")

        indice = input("Digite o número da empresa: ").strip()
        if not indice.isdigit() or int(indice) < 1 or int(indice) > len(empresas):
            self.__tela_meio_transporte.mostra_mensagem("Opção inválida.")
            return

        empresa_escolhida = empresas[int(indice) - 1]
        meio = MeioTransporte(tipo, capacidade, empresa_escolhida)

        self.__meio_transporte_dao.add(meio)
        self.__tela_meio_transporte.mostra_mensagem(
            f"Meio de transporte '{meio.tipo}' cadastrado com sucesso!"
        )

    def lista_meio_transporte(self):
        meios = self.__meio_transporte_dao.get_all()
        if not meios:
            self.__tela_meio_transporte.mostra_mensagem("Nenhum meio de transporte cadastrado.")
            return

        for meio in meios:
            self.__tela_meio_transporte.mostra_meio({
                "tipo": meio.tipo,
                "capacidade": meio.capacidade,
                "empresa": meio.empresa_transporte.nome_empresa
            })

    def excluir_meio_transporte(self):
        self.lista_meio_transporte()
        tipo_meio = self.__tela_meio_transporte.seleciona_meio_transporte()
        meio = self.pega_meio_por_tipo(tipo_meio)
        if meio:
            self.__meio_transporte_dao.remove(meio.tipo)
            self.__tela_meio_transporte.mostra_mensagem(
                f"Meio de transporte '{meio.tipo}' excluído com sucesso!"
            )
        else:
            self.__tela_meio_transporte.mostra_mensagem("Meio não encontrado.")

    def alterar_meio_transporte(self):
        tipo = self.__tela_meio_transporte.seleciona_meio_transporte()
        meio = self.pega_meio_por_tipo(tipo)
        if not meio:
            self.__tela_meio_transporte.mostra_mensagem("Meio não encontrado.")
            return

        novos_dados = self.__tela_meio_transporte.pega_dados_meio_transporte()
        if novos_dados:
            meio.tipo = novos_dados["tipo"].strip().title()
            try:
                meio.capacidade = int(novos_dados["capacidade"])
            except ValueError:
                self.__tela_meio_transporte.mostra_mensagem("Capacidade inválida.")
                return
            self.__meio_transporte_dao.update(meio)
            self.__tela_meio_transporte.mostra_mensagem("Meio atualizado com sucesso!")
        else:
            self.__tela_meio_transporte.mostra_mensagem("Alteração cancelada.")

    def retornar(self):
        self.__controlador_controladores.inicializa_sistema()

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
            if funcao:
                if opcao == 0:
                    sair = True
                funcao()
            else:
                self.__tela_meio_transporte.mostra_mensagem("Opção inválida.")
