from view.tela_pagamento import TelaPagamento
from model.pagamento import Cartao, Pix, Cedula
from random import randint
from daos.pagamento_dao import PagamentoDAO
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException


class ControladorPagamento:
    def __init__(self, controlador_controladores):
        self.__pagamento_dao = PagamentoDAO()
        self.__tela_pagamento = TelaPagamento()
        self.__controlador_controladores = controlador_controladores

    def pega_pagamento_por_codigo(self, codigo):
        for pagamento in self.__pagamento_dao.get_all():
            if str(pagamento.codigo) == str(codigo):
                return pagamento
        return None

    def __monta_lista_dados(self):
        pagamentos = self.__pagamento_dao.get_all()
        lista = []
        for p in pagamentos:
            lista.append({
                "codigo": p.codigo,
                "forma": p.forma_pagamento,
                "valor": p.valor_total,
                "data": p.data,
                "status": "Pago" if p.pagou else "Pendente",
                "passageiro": p.passageiro.nome
            })
        return lista

    def incluir_pagamento(self):
        try:
            dados_pagamento = self.__tela_pagamento.pega_dados_pagamento()
            if not dados_pagamento:
                return

            forma_pagamento = dados_pagamento["forma_pagamento"]
            passageiro = self.__controlador_controladores.controlador_pessoa.pega_pessoa_por_cpf(
                dados_pagamento["cpf_passageiro"]
            )

            if not passageiro:
                raise ElementoNaoExisteException("Passageiro não encontrado.")

            valor_total = float(dados_pagamento["valor_total"])
            data = dados_pagamento["data"]
            pagou = dados_pagamento["pagou"]

            pagamento = None
            msg_sucesso = "Pagamento cadastrado com sucesso!"

            if forma_pagamento == "cartao":
                dados_cartao = self.__tela_pagamento.pega_dados_cartao()
                if not dados_cartao:
                    return
                pagamento = Cartao("cartao", pagou, data, valor_total, passageiro,
                                     dados_cartao["numero_cartao"], dados_cartao["validade"],
                                     dados_cartao["bandeira"], dados_cartao["nome_titular"])
                msg_sucesso = "💳 Pagamento via CARTÃO cadastrado com sucesso!"

            elif forma_pagamento == "pix":
                dados_pix = self.__tela_pagamento.pega_dados_pix()
                if not dados_pix:
                    return
                pagamento = Pix("pix", pagou, data, valor_total, passageiro,
                                 dados_pix["chave_pix"], dados_pix["banco"])
                
                msg_sucesso = f"⚡ Pagamento via PIX ({dados_pix['banco']}) realizado com sucesso."

            elif forma_pagamento == "cedulas":
                pagamento = Cedula("cedulas", pagou, data,
                                     valor_total, passageiro)
                msg_sucesso = "💵 Pagamento em CÉDULAS cadastrado com sucesso!"
            else:
                self.__tela_pagamento.mostra_mensagem("Forma de pagamento inválida.")
                return

            pagamento.codigo = randint(1, 10000)
            pagamento.processar_pagamento()
            self.__pagamento_dao.add(pagamento)
            
            self.__tela_pagamento.mostra_mensagem(msg_sucesso)

        except ElementoNaoExisteException as e:
            self.__tela_pagamento.mostra_mensagem(str(e))
        except ValueError:
            self.__tela_pagamento.mostra_mensagem("Erro: Valor inválido! Verifique se o 'Valor Total' contém apenas números.")

    def alterar_pagamento(self):
        try:
            lista_dados = self.__monta_lista_dados()
            if not lista_dados:
                self.__tela_pagamento.mostra_mensagem(
                    "Nenhum pagamento cadastrado.")
                return

            codigo = self.__tela_pagamento.seleciona_pagamento(lista_dados)
            if not codigo:
                return

            pagamento = self.pega_pagamento_por_codigo(codigo)
            if not pagamento:
                raise ElementoNaoExisteException("Pagamento não encontrado.")

            novos_dados = self.__tela_pagamento.pega_dados_pagamento(pagamento)
            if not novos_dados:
                return

            pagamento.valor_total = float(novos_dados["valor_total"])
            pagamento.data = novos_dados["data"]
            pagamento.pagou = novos_dados["pagou"]

            passageiro_novo = self.__controlador_controladores.controlador_pessoa.pega_pessoa_por_cpf(
                novos_dados["cpf_passageiro"])
            if passageiro_novo:
                pagamento.passageiro = passageiro_novo

            self.__pagamento_dao.update(pagamento)
            self.__tela_pagamento.mostra_mensagem(
                "Pagamento alterado com sucesso!")

        except ElementoNaoExisteException as e:
            self.__tela_pagamento.mostra_mensagem(str(e))
        except ValueError:
            self.__tela_pagamento.mostra_mensagem("Erro: Erro no valor numérico. Verifique se digitou o valor corretamente.")

    def listar_pagamentos(self):
        lista = self.__monta_lista_dados()
        self.__tela_pagamento.mostra_pagamentos(lista)

    def excluir_pagamento(self):
        try:
            lista_dados = self.__monta_lista_dados()
            if not lista_dados:
                self.__tela_pagamento.mostra_mensagem("Lista vazia.")
                return

            codigo = self.__tela_pagamento.seleciona_pagamento(lista_dados)
            if not codigo:
                return

            pagamento = self.pega_pagamento_por_codigo(codigo)
            if not pagamento:
                raise ElementoNaoExisteException("Pagamento não encontrado.")

            self.__pagamento_dao.remove(pagamento.codigo)
            self.__tela_pagamento.mostra_mensagem("Pagamento excluído!")

        except ElementoNaoExisteException as e:
            self.__tela_pagamento.mostra_mensagem(str(e))

    def retornar(self):
        return

    def abre_tela(self):
        opcoes = {
            1: self.incluir_pagamento,
            2: self.alterar_pagamento,
            3: self.listar_pagamentos,
            4: self.excluir_pagamento,
            0: self.retornar
        }
        while True:
            opcao = self.__tela_pagamento.tela_opcoes()
            if opcao == 0:
                break
            funcao = opcoes.get(opcao)
            if funcao:
                funcao()
            else:
                self.__tela_pagamento.mostra_mensagem("Opção inválida.")