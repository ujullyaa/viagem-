# controller/controlador_itinerario.py
from view.tela_itinerario import TelaItinerario
from model.itinerario import Itinerario
from daos.itinerario_dao import ItinerarioDAO

class ControladorItinerario:
    def __init__(self, controlador_controladores):
        self.__itinerario_dao = ItinerarioDAO()
        self.__tela_itinerario = TelaItinerario()
        self.__controlador_controladores = controlador_controladores  # referência para passagens, pessoas etc.

    def pega_itinerario_por_codigo(self, codigo_itinerario: int):
        for itinerario in self.__itinerario_dao.get_all():
            if itinerario.codigo_itinerario == codigo_itinerario:
                return itinerario
        return None

    def incluir_itinerario(self):
        dados = self.__tela_itinerario.pega_dados_itinerario()
        if not dados:
            self.__tela_itinerario.mostra_mensagem("❌ Dados inválidos.")
            return

        if self.pega_itinerario_por_codigo(dados["codigo_itinerario"]):
            self.__tela_itinerario.mostra_mensagem("⚠️ Já existe um itinerário com esse código.")
            return

        novo_itinerario = Itinerario(
            codigo_itinerario=dados["codigo_itinerario"],
            origem=dados["origem"],
            destino=dados["destino"],
            data_inicio=dados["data_inicio"],
            data_fim=dados["data_fim"]
        )

        if not novo_itinerario.validar_datas():
            self.__tela_itinerario.mostra_mensagem("⚠️ Data inicial não pode ser posterior à data final.")
            return

        self.__itinerario_dao.add(novo_itinerario)
        self.__tela_itinerario.mostra_mensagem("✅ Itinerário cadastrado com sucesso!")

    def listar_itinerarios(self):
        itinerarios = self.__itinerario_dao.get_all()
        if not itinerarios:
            self.__tela_itinerario.mostra_mensagem("📭 Nenhum itinerário cadastrado.")
            return

        for it in itinerarios:
            self.__tela_itinerario.mostra_itinerario({
                "codigo_itinerario": it.codigo_itinerario,
                "origem": it.origem,
                "destino": it.destino,
                "data_inicio": it.data_inicio,
                "data_fim": it.data_fim,
                "qtd_passagens": len(it.passagem)
            })

    def abre_tela(self):
        opcoes = {
            1: self.incluir_itinerario,
            2: self.listar_itinerarios,
            0: self.__controlador_controladores.inicializa_sistema
        }

        while True:
            escolha = self.__tela_itinerario.tela_opcoes()
            funcao = opcoes.get(escolha)
            if funcao:
                funcao()
            else:
                self.__tela_itinerario.mostra_mensagem("❌ Opção inválida!")
            if escolha == 0:
                break
