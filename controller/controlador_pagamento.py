from view.tela_pagamento import TelaPagamento
from model.pagamento import Cartao, pix, Cedula
from random import randint
from daos.pagamento_dao import PagamentoDAO

class ControladorPagamento:
    def __init__(self, controlador_controladores):
        self.__pagamento_dao = PagamentoDAO()
        self.__tela_pagamento = TelaPagamento()
        self.__controlador_controladores = controlador_controladores

    def pega_pagamento_por_codigo(self, codigo: int):
        for pagamento in self.__pagamento_dao.get_all:
            if pagamento.codigo == codigo:
                return pagamento
        return None

    def incluir_pagamento(self):
        dados_pagamento = self.__tela_pagamento.pega_dados_pagamento()
        forma_pagamento = dados_pagamento["forma_pagamento"]

        # 🔹 Buscar passageiro pelo CPF
        passageiro = self.__controlador_controladores.controlador_pessoa.pega_pessoa_por_cpf(
            dados_pagamento["cpf_passageiro"]
        )

        if not passageiro:
            self.__tela_pagamento.mostra_mensagem("Passageiro não encontrado.")
            return

        valor_total = float(dados_pagamento["valor_total"])
        data = dados_pagamento["data"]
        pagou = dados_pagamento["pagou"]

        if forma_pagamento == "cartao":
            dados_cartao = self.__tela_pagamento.pega_dados_cartao()
            pagamento = Cartao(
                forma_pagamento="cartao",
                pagou=pagou,
                data=data,
                valor_total=valor_total,
                passageiro=passageiro,
                numero_cartao=dados_cartao["numero_cartao"],
                validade=dados_cartao["validade"],
                bandeira=dados_cartao["bandeira"],
                titular=dados_cartao["nome_titular"]  # 🔹 corrigido
            )

        elif forma_pagamento == "pix":
            dados_pix = self.__tela_pagamento.pega_dados_pix()
            pagamento = pix(
                forma_pagamento="pix",
                pagou=pagou,
                data=data,
                valor_total=valor_total,
                passageiro=passageiro,
                chave_pix=dados_pix["chave_pix"],
                banco=dados_pix["banco"]
            )

        elif forma_pagamento == "cedulas":
            pagamento = Cedula(
                forma_pagamento="cedulas",
                pagou=pagou,
                data=data,
                valor_total=valor_total,
                passageiro=passageiro
            )
        else:
            self.__tela_pagamento.mostra_mensagem(
                "Forma de pagamento inválida.")
            return

        pagamento.codigo = randint(1, 10000)
        pagamento.processar_pagamento()
        self.__pagamento_dao.add(pagamento)
        self.__tela_pagamento.mostra_mensagem(
            "Pagamento cadastrado com sucesso!")

    def listar_pagamentos(self):
        if not self.__pagamento_dao.get_all:
            self.__tela_pagamento.mostra_mensagem(
                "Nenhum pagamento cadastrado.")
            return

        for pagamento in self.__pagamento_dao.get_all:
            self.__tela_pagamento.mostra_pagamento({
                "codigo": pagamento.codigo,
                "forma_pagamento": pagamento.forma_pagamento,
                "valor_total": pagamento.valor_total,
                "data": pagamento.data,
                "pagou": pagamento.pagou,
                "passageiro": pagamento.passageiro.nome
            })

    def excluir_pagamento(self):
        self.listar_pagamentos()
        codigo = self.__tela_pagamento.seleciona_pagamento()
        pagamento = self.pega_pagamento_por_codigo(codigo)

        if pagamento:
            self.__pagamento_dao.remove(pagamento)
            self.__tela_pagamento.mostra_mensagem(
                "Pagamento excluído com sucesso!")
        else:
            self.__tela_pagamento.mostra_mensagem("Pagamento não encontrado.")

    def retornar(self):
        self.__controlador_controladores.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_pagamento,
            2: self.listar_pagamentos,
            3: self.excluir_pagamento,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_pagamento.tela_opcoes()
            funcao_escolhida = opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_pagamento.mostra_mensagem("Opção inválida.")
