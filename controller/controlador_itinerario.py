from view.tela_itinerario import TelaItinerario
from model.itinerario import Itinerario


class ControladorItinerario:
    def __init__(self, controlador_controladores):
        self.__itinerarios = []
        self.__tela_itinerario = TelaItinerario()
        self.__controlador_controladores = controlador_controladores

    def pega_itinerario_por_codigo_itinerario(self, codigo_itinerario: int):
        for itinerario in self.__itinerarios:
            if itinerario.codigo_itinerario == codigo_itinerario:
                return itinerario
        return None

    def incluir_itinerario(self):
        dados_itinerario = self.__tela_itinerario.pega_dados_itinerario()
        if not dados_itinerario:
            self.__tela_itinerario.mostra_mensagem(" Dados inválidos. Tente novamente.")
            return

        itinerario = Itinerario(
            dados_itinerario["codigo_itinerario"],
            dados_itinerario["origem"],
            dados_itinerario["destino"],
            dados_itinerario["data_inicio"],
            dados_itinerario["data_fim"],
            dados_itinerario.get("passagem", [])
        )
        self.__itinerarios.append(itinerario)
        self.__tela_itinerario.mostra_mensagem(" Itinerário cadastrado com sucesso!")

    def listar_itinerarios(self):
        if not self.__itinerarios:
            self.__tela_itinerario.mostra_mensagem(" Nenhum itinerário cadastrado.")
            return

        for itinerario in self.__itinerarios:
            self.__tela_itinerario.mostra_itinerario({
                "codigo_itinerario": itinerario.codigo_itinerario,
                "origem": itinerario.origem,
                "destino": itinerario.destino,
                "data_inicio": itinerario.data_inicio,
                "data_fim": itinerario.data_fim,
                "passagem": itinerario.passagem
            })

    def excluir_itinerario(self):
        self.listar_itinerarios()
        codigo_itinerario = self.__tela_itinerario.seleciona_itinerario()

        itinerario = self.pega_itinerario_por_codigo_itinerario(codigo_itinerario)

        if itinerario:
            self.__itinerarios.remove(itinerario)
            self.__tela_itinerario.mostra_mensagem(" Itinerário removido com sucesso!")
        else:
            self.__tela_itinerario.mostra_mensagem(" Atenção: Itinerário não existente.")

    def alterar_itinerario(self):
        codigo_itinerario = self.__tela_itinerario.seleciona_itinerario()
        itinerario = self.pega_itinerario_por_codigo_itinerario(codigo_itinerario)

        if itinerario:
            novos_dados = self.__tela_itinerario.pega_dados_itinerario()
            if not novos_dados:
                self.__tela_itinerario.mostra_mensagem(" Dados inválidos.")
                return

            itinerario.codigo_itinerario = novos_dados["codigo_itinerario"]
            itinerario.origem = novos_dados["origem"]
            itinerario.destino = novos_dados["destino"]
            itinerario.data_inicio = novos_dados["data_inicio"]
            itinerario.data_fim = novos_dados["data_fim"]
            itinerario.passagem = novos_dados.get("passagem", [])
            self.__tela_itinerario.mostra_mensagem(" Itinerário atualizado com sucesso!")
        else:
            self.__tela_itinerario.mostra_mensagem(" Itinerário não encontrado.")

    def retornar(self):
        self.__controlador_controladores.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_itinerario,
            2: self.alterar_itinerario,
            3: self.listar_itinerarios,
            4: self.excluir_itinerario,
            0: self.retornar
        }

        continua = True

        while continua:
            opcao = self.__tela_itinerario.tela_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao)

            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_itinerario.mostra_mensagem(" Opção inválida!")

            if opcao == 0:
                continua = False
