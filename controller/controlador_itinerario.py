from view.tela_itinerario import TelaItinerario
from model.itinerario import Itinerario
from daos.itinerario_dao import ItinerarioDAO
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException


class ControladorItinerario:
    def __init__(self, controlador_controladores):
        self.__itinerario_dao = ItinerarioDAO()
        self.__tela_itinerario = TelaItinerario()
        self.__controlador_controladores = controlador_controladores

    @property
    def itinerarios(self):
        return self.__itinerario_dao.get_all()

    def atualizar_itinerario(self, itinerario):
        self.__itinerario_dao.update(itinerario)

    def pega_itinerario_por_codigo(self, codigo):
        for itin in self.__itinerario_dao.get_all():
            if str(itin.codigo_itinerario) == str(codigo):
                return itin
        return None

    def incluir_itinerario(self):
        dados = self.__tela_itinerario.pega_dados_itinerario()
        if not dados:
            return

        try:
            if self.pega_itinerario_por_codigo(dados["codigo_itinerario"]):
                raise ElementoRepetidoException(
                    f"Itinerário com código {dados['codigo_itinerario']} já existe.")

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

            if self.__tela_itinerario.confirmar_cadastro_passagem():
                self.__controlador_controladores.controlador_passagem.incluir_passagem(
                    itinerario_fixo=itinerario)
            else:
                self.__tela_itinerario.mostra_mensagem(
                    "Itinerário cadastrado!")

        except ElementoRepetidoException as e:
            self.__tela_itinerario.mostra_mensagem(str(e))

    def alterar_itinerario(self):
        try:
            itinerarios = self.__itinerario_dao.get_all()
            if not itinerarios:
                self.__tela_itinerario.mostra_mensagem("Nenhum cadastrado.")
                return

            lista_itinerarios = []
            for i in itinerarios:
                lista_itinerarios.append({
                    "codigo_itinerario": i.codigo_itinerario,
                    "origem": i.origem,
                    "destino": i.destino,
                    "data_inicio": i.data_inicio,
                    "data_fim": i.data_fim
                })

            codigo = self.__tela_itinerario.seleciona_itinerario(
                lista_itinerarios)
            if not codigo:
                return

            itinerario = self.pega_itinerario_por_codigo(codigo)

            if not itinerario:
                raise ElementoNaoExisteException(
                    "Itinerário não encontrado para alteração.")

            dados = self.__tela_itinerario.pega_dados_itinerario(itinerario)
            if not dados:
                return

            itinerario.origem = dados["origem"]
            itinerario.destino = dados["destino"]
            itinerario.data_inicio = dados["data_inicio"]
            itinerario.data_fim = dados["data_fim"]

            if not itinerario.validar_datas():
                self.__tela_itinerario.mostra_mensagem("Datas inválidas!")
                return

            self.__itinerario_dao.update(itinerario)
            self.__tela_itinerario.mostra_mensagem("Atualizado com sucesso!")

        except ElementoNaoExisteException as e:
            self.__tela_itinerario.mostra_mensagem(str(e))

    def excluir_itinerario(self):
        try:
            itinerarios = self.__itinerario_dao.get_all()
            if not itinerarios:
                self.__tela_itinerario.mostra_mensagem("Vazio.")
                return

            lista_itinerarios = []
            for i in itinerarios:
                lista_itinerarios.append({
                    "codigo_itinerario": i.codigo_itinerario,
                    "origem": i.origem,
                    "destino": i.destino,
                    "data_inicio": i.data_inicio,
                    "data_fim": i.data_fim
                })

            codigo = self.__tela_itinerario.seleciona_itinerario(
                lista_itinerarios)
            if not codigo:
                return

            itinerario = self.pega_itinerario_por_codigo(codigo)

            if not itinerario:
                raise ElementoNaoExisteException("Itinerário não existe.")

            self.__itinerario_dao.remove(itinerario.codigo_itinerario)
            self.__tela_itinerario.mostra_mensagem("Removido!")

        except ElementoNaoExisteException as e:
            self.__tela_itinerario.mostra_mensagem(str(e))

    def listar_itinerarios(self):
        itins = self.__itinerario_dao.get_all()
        if not itins:
            self.__tela_itinerario.mostra_mensagem(
                "Nenhum itinerário cadastrado.")
            return

        lista = []
        for i in itins:
            lista.append({
                "codigo_itinerario": i.codigo_itinerario,
                "origem": i.origem,
                "destino": i.destino,
                "data_inicio": i.data_inicio,
                "data_fim": i.data_fim
            })
        self.__tela_itinerario.mostra_itinerarios(lista)

    def retornar(self):
        return

    def abre_tela(self):
        opcoes = {
            1: self.incluir_itinerario,
            2: self.alterar_itinerario,
            3: self.listar_itinerarios,
            4: self.excluir_itinerario,
            0: self.retornar
        }
        while True:
            opcao = self.__tela_itinerario.tela_opcoes()
            if opcao == 0:
                break
            funcao = opcoes.get(opcao)
            if funcao:
                funcao()
            else:
                self.__tela_itinerario.mostra_mensagem("Opção inválida.")
