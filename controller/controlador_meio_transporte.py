from view.tela_meio_transporte import TelaMeioTransporte
from model.meio_transporte import MeioTransporte
from daos.meio_transporte_dao import MeioTransporteDAO
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException


class ControladorMeioTransporte:
    def __init__(self, controlador_controladores, controlador_empresa_transporte):
        self.__meio_transporte_dao = MeioTransporteDAO()
        self.__tela_meio_transporte = TelaMeioTransporte()
        self.__controlador_controladores = controlador_controladores
        self.__controlador_empresa_transporte = controlador_empresa_transporte

    def pega_meio_por_tipo(self, tipo):
        if not tipo:
            return None
        target = str(tipo).strip().lower()
        for m in self.__meio_transporte_dao.get_all():
            if m.tipo.lower() == target:
                return m
        return None

    def incluir_meio_transporte(self):
        empresas = list(self.__controlador_empresa_transporte.empresas)
        if not empresas:
            self.__tela_meio_transporte.mostra_mensagem(
                "Sem empresas cadastradas.")
            return

        dados = self.__tela_meio_transporte.pega_dados_meio_transporte()
        if not dados:
            return

        try:
            if not dados["capacidade"] or int(dados["capacidade"]) <= 0:
                raise ValueError(
                    "A capacidade deve ser um número maior que zero.")

            empresa = self.__tela_meio_transporte.seleciona_empresa(empresas)
            if not empresa:
                return

            meio = MeioTransporte(dados["tipo"], int(
                dados["capacidade"]), empresa)
            self.__meio_transporte_dao.add(meio)
            self.__tela_meio_transporte.mostra_mensagem("Sucesso!")

        except ValueError as e:
            self.__tela_meio_transporte.mostra_mensagem(
                f"Erro de Validação: {e}")
        except Exception as e:
            self.__tela_meio_transporte.mostra_mensagem(str(e))

    def alterar_meio_transporte(self):
        try:
            meios = list(self.__meio_transporte_dao.get_all())
            if not meios:
                self.__tela_meio_transporte.mostra_mensagem("Vazio.")
                return

            meio_selecionado = self.__tela_meio_transporte.seleciona_meio_transporte(
                meios)
            if not meio_selecionado:
                return

            novos_dados = self.__tela_meio_transporte.pega_dados_meio_transporte(
                meio_selecionado)
            if not novos_dados:
                return

            if not novos_dados["capacidade"] or int(novos_dados["capacidade"]) <= 0:
                raise ValueError(
                    "A capacidade deve ser um número maior que zero.")

            meio_selecionado.tipo = novos_dados["tipo"]
            meio_selecionado.capacidade = int(novos_dados["capacidade"])

            self.__meio_transporte_dao.update(meio_selecionado)
            self.__tela_meio_transporte.mostra_mensagem("Atualizado!")

        except ValueError as e:
            self.__tela_meio_transporte.mostra_mensagem(f"Erro: {e}")
        except Exception as e:
            self.__tela_meio_transporte.mostra_mensagem(str(e))

    def excluir_meio_transporte(self):
        try:
            meios = list(self.__meio_transporte_dao.get_all())
            if not meios:
                return

            meio_selecionado = self.__tela_meio_transporte.seleciona_meio_transporte(
                meios)

            if not meio_selecionado:
                if meio_selecionado not in self.__meio_transporte_dao.get_all():
                    pass
                return

            self.__meio_transporte_dao.remove(meio_selecionado)
            self.__tela_meio_transporte.mostra_mensagem("Excluído!")

        except ElementoNaoExisteException as e:
            self.__tela_meio_transporte.mostra_mensagem(str(e))

    def excluir_veiculos_da_empresa(self, empresa_alvo):

        veiculos = self.__meio_transporte_dao.get_all()
        removidos = 0
        for veiculo in veiculos:
            if veiculo.empresa_transporte and veiculo.empresa_transporte.cnpj == empresa_alvo.cnpj:
                self.__meio_transporte_dao.remove(veiculo)
                removidos += 1

        if removidos > 0:
            print(
                f"Alerta: {removidos} veículos da empresa {empresa_alvo.nome_empresa} foram removidos automaticamente.")

    def lista_meio_transporte(self):
        self.__tela_meio_transporte.lista_meios(
            self.__meio_transporte_dao.get_all())

    def retornar(self):
        return

    def abre_tela(self):
        opcoes = {
            1: self.incluir_meio_transporte,
            2: self.alterar_meio_transporte,
            3: self.lista_meio_transporte,
            4: self.excluir_meio_transporte,
            0: self.retornar
        }
        while True:
            op = self.__tela_meio_transporte.tela_opcoes()
            func = opcoes.get(op)
            if op == 0:
                func()
                break
            elif func:
                func()
