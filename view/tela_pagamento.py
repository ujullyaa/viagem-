import FreeSimpleGUI as sg

class TelaPagamento:
    def __init__(self):
        sg.theme("DarkBlue14")

    def tela_opcoes(self):
        layout = [
            [sg.Text("===== PAGAMENTO =====", font=("Arial", 14, "bold"))],
            [sg.Button("1 - Incluir Pagamento")],
            [sg.Button("2 - Listar Pagamentos")],
            [sg.Button("3 - Excluir Pagamento")],
            [sg.Button("0 - Retornar ao Menu Principal")]
        ]
        janela = sg.Window("Menu Pagamento", layout)
        evento, _ = janela.read()
        janela.close()

        if evento in (sg.WIN_CLOSED, "0 - Retornar ao Menu Principal"):
            return 0
        elif evento == "1 - Incluir Pagamento":
            return 1
        elif evento == "2 - Listar Pagamentos":
            return 2
        elif evento == "3 - Excluir Pagamento":
            return 3
        else:
            return -1

    def escolhe_tipo_pagamento(self):
        layout = [
            [sg.Text("Escolha a forma de pagamento:", font=("Arial", 12, "bold"))],
            [sg.Radio("Cartão", "FORMA", key="cartao")],
            [sg.Radio("Pix", "FORMA", key="pix")],
            [sg.Radio("Cédulas", "FORMA", key="cedulas")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        janela = sg.Window("Forma de Pagamento", layout)
        evento, valores = janela.read()
        janela.close()

        if evento == "Confirmar":
            if valores["cartao"]:
                return "cartao"
            elif valores["pix"]:
                return "pix"
            elif valores["cedulas"]:
                return "cedulas"
        return None

    def pega_dados_pagamento(self):
        layout = [
            [sg.Text("Novo Pagamento", font=("Arial", 14, "bold"))],
            [sg.Text("CPF do Passageiro:", size=(18, 1)), sg.Input(key="cpf_passageiro")],
            [sg.Text("Valor Total:", size=(18, 1)), sg.Input(key="valor_total")],
            [sg.Text("Data (DD/MM/AAAA):", size=(18, 1)), sg.Input(key="data")],
            [sg.Checkbox("Pagamento Efetuado", key="pagou")],
            [sg.Button("Escolher Forma de Pagamento"), sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        janela = sg.Window("Cadastro de Pagamento", layout)
        forma_pagamento = None

        while True:
            evento, valores = janela.read()
            if evento in (sg.WIN_CLOSED, "Cancelar"):
                janela.close()
                return None
            elif evento == "Escolher Forma de Pagamento":
                forma_pagamento = self.escolhe_tipo_pagamento()
                if forma_pagamento:
                    sg.popup(f"Forma escolhida: {forma_pagamento.upper()}")
            elif evento == "Confirmar":
                if not forma_pagamento:
                    sg.popup_error("Escolha a forma de pagamento antes de confirmar!")
                    continue

                try:
                    valor_total = float(valores["valor_total"])
                except ValueError:
                    sg.popup_error("Valor inválido. Use apenas números.")
                    continue

                janela.close()
                return {
                    "cpf_passageiro": valores["cpf_passageiro"],
                    "valor_total": valor_total,
                    "data": valores["data"],
                    "pagou": valores["pagou"],
                    "forma_pagamento": forma_pagamento
                }

    def pega_dados_cartao(self):
        layout = [
            [sg.Text("Dados do Cartão", font=("Arial", 13, "bold"))],
            [sg.Text("Número do Cartão:"), sg.Input(key="numero_cartao")],
            [sg.Text("Nome do Titular:"), sg.Input(key="nome_titular")],
            [sg.Text("Validade (MM/AA):"), sg.Input(key="validade")],
            [sg.Text("Bandeira:"), sg.Input(key="bandeira")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        janela = sg.Window("Cartão de Crédito", layout)
        evento, valores = janela.read()
        janela.close()

        if evento == "Confirmar":
            return valores
        return None

    def pega_dados_pix(self):
        layout = [
            [sg.Text("Dados PIX", font=("Arial", 13, "bold"))],
            [sg.Text("Chave Pix:"), sg.Input(key="chave_pix")],
            [sg.Text("Banco:"), sg.Input(key="banco")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        janela = sg.Window("Pagamento via PIX", layout)
        evento, valores = janela.read()
        janela.close()

        if evento == "Confirmar":
            return valores
        return None

    def mostra_pagamento(self, dados_pagamento: dict):
        texto = (
            f"Código: {dados_pagamento.get('codigo', '(não informado)')}\n"
            f"Passageiro: {dados_pagamento.get('passageiro', '(não informado)')}\n"
            f"Forma de Pagamento: {dados_pagamento['forma_pagamento']}\n"
            f"Valor Total: R$ {dados_pagamento['valor_total']:.2f}\n"
            f"Data: {dados_pagamento['data']}\n"
            f"Efetuado: {'Sim' if dados_pagamento['pagou'] else 'Não'}"
        )
        sg.popup_scrolled(texto, title="Dados do Pagamento", font=("Arial", 11))

    def mostra_mensagem(self, msg: str):
        sg.popup(msg, title="Mensagem")

    def seleciona_pagamento(self):
        layout = [
            [sg.Text("Digite o código do pagamento:")],
            [sg.Input(key="codigo")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        janela = sg.Window("Selecionar Pagamento", layout)
        evento, valores = janela.read()
        janela.close()

        if evento == "Confirmar":
            try:
                return int(valores["codigo"])
            except ValueError:
                sg.popup_error("O código deve ser um número!")
        return None
