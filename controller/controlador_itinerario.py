from view.tela_itinerario import TelaItinerario
from model.itinerario import Itinerario
from daos.itinerario_dao import ItinerarioDAO

class ControladorItinerario:
    def __init__(self, controlador_controladores):
        self.__itinerario_dao = ItinerarioDAO()
        self.__tela_itinerario = TelaItinerario()
        self.__controlador_controladores = controlador_controladores

    @property
    def itinerarios(self):
        return self.__itinerario_dao.get_all()

    def pega_itinerario_por_codigo(self, codigo):
        # Aceita `codigo` como int ou str vindo da interface
        for itin in self.__itinerario_dao.get_all():
            try:
                # comparar como inteiro quando possível
                if int(itin.codigo_itinerario) == int(codigo):
                    return itin
            except Exception:
                # fallback para comparação de string
                if str(itin.codigo_itinerario) == str(codigo):
                    return itin
        return None

    def incluir_itinerario(self):
        dados = self.__tela_itinerario.pega_dados_itinerario()
        if not dados:
            self.__tela_itinerario.mostra_mensagem("Operação cancelada.")
            return

        if self.pega_itinerario_por_codigo(dados["codigo_itinerario"]):
            self.__tela_itinerario.mostra_mensagem("Itinerário já cadastrado!")
            return

        itinerario = Itinerario(
            codigo_itinerario=dados["codigo_itinerario"],
            origem=dados["origem"],
            destino=dados["destino"],
            data_inicio=dados["data_inicio"],
            data_fim=dados["data_fim"]
        )

        if not itinerario.validar_datas():
            self.__tela_itinerario.mostra_mensagem("Datas inválidas!")
            return

        self.__itinerario_dao.add(itinerario)
        self.__tela_itinerario.mostra_mensagem("✅ Itinerário cadastrado com sucesso!")

    def alterar_itinerario(self):
        # Mostrar todos os itinerários cadastrados para facilitar a escolha
        itinerarios = self.__itinerario_dao.get_all()
        if not itinerarios:
            self.__tela_itinerario.mostra_mensagem("Nenhum itinerário cadastrado.")
            return

        lista_itinerarios = []
        for itin in itinerarios:
            lista_itinerarios.append({
                "codigo_itinerario": itin.codigo_itinerario,
                "origem": itin.origem,
                "destino": itin.destino,
                "data_inicio": itin.data_inicio,
                "data_fim": itin.data_fim
            })

        codigo = self.__tela_itinerario.mostra_itinerario(lista_itinerarios)
        if not codigo:
            self.__tela_itinerario.mostra_mensagem("Operação cancelada.")
            return

        itinerario = self.pega_itinerario_por_codigo(codigo)
        if not itinerario:
            self.__tela_itinerario.mostra_mensagem("Itinerário não encontrado.")
            return

        dados = self.__tela_itinerario.pega_dados_itinerario(itinerario)
        if not dados:
            self.__tela_itinerario.mostra_mensagem("Operação cancelada.")
            return

        itinerario.origem = dados["origem"]
        itinerario.destino = dados["destino"]
        itinerario.data_inicio = dados["data_inicio"]
        itinerario.data_fim = dados["data_fim"]

        if not itinerario.validar_datas():
            self.__tela_itinerario.mostra_mensagem("Datas inválidas!")
            return

        self.__itinerario_dao.update(itinerario)
        self.__tela_itinerario.mostra_mensagem("✅ Itinerário alterado com sucesso!")

    def listar_itinerarios(self):
        itinerarios = self.__itinerario_dao.get_all()
        if not itinerarios:
            self.__tela_itinerario.mostra_mensagem("Nenhum itinerário cadastrado.")
            return

        # Construir lista de dicionários e mostrar todos de uma vez
        lista_itinerarios = []
        for itin in itinerarios:
            lista_itinerarios.append({
                "codigo_itinerario": itin.codigo_itinerario,
                "origem": itin.origem,
                "destino": itin.destino,
                "data_inicio": itin.data_inicio,
                "data_fim": itin.data_fim
            })

        self.__tela_itinerario.mostra_itinerario(lista_itinerarios)

    def excluir_itinerario(self):
        # Mostrar todos os itinerários cadastrados para facilitar a escolha
        itinerarios = self.__itinerario_dao.get_all()
        if not itinerarios:
            self.__tela_itinerario.mostra_mensagem("Nenhum itinerário cadastrado.")
            return

        lista_itinerarios = []
        for itin in itinerarios:
            lista_itinerarios.append({
                "codigo_itinerario": itin.codigo_itinerario,
                "origem": itin.origem,
                "destino": itin.destino,
                "data_inicio": itin.data_inicio,
                "data_fim": itin.data_fim
            })

        codigo = self.__tela_itinerario.mostra_itinerario(lista_itinerarios)
        if not codigo:
            self.__tela_itinerario.mostra_mensagem("Operação cancelada.")
            return

        itinerario = self.pega_itinerario_por_codigo(codigo)
        if itinerario:
            self.__itinerario_dao.remove(itinerario.codigo_itinerario)
            self.__tela_itinerario.mostra_mensagem("Itinerário removido com sucesso!")
        else:
            self.__tela_itinerario.mostra_mensagem("Itinerário não encontrado.")

    def adicionar_passagem(self, codigo_itinerario, passagem):
        itinerario = self.pega_itinerario_por_codigo(codigo_itinerario)
        if not itinerario:
            self.__tela_itinerario.mostra_mensagem("Itinerário não encontrado.")
            return

        itinerario.adicionar_passagem(passagem)
        self.__itinerario_dao.update(itinerario)
        self.__tela_itinerario.mostra_mensagem("✅ Passagem adicionada ao itinerário!")

    def retornar(self):
        self.__controlador_controladores.inicializa_sistema()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_itinerario,
            2: self.alterar_itinerario,
            3: self.listar_itinerarios,
            4: self.excluir_itinerario,
            0: self.retornar
        }

        while True:
            escolha = self.__tela_itinerario.tela_opcoes()
            funcao = opcoes.get(escolha)
            if funcao:
                funcao()
                if escolha == 0:
                    break
            else:
                self.__tela_itinerario.mostra_mensagem("Opção inválida.")
