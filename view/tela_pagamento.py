import FreeSimpleGUI as sg

class TelaPagamento:
    def __init__(self):
        pass

    def tela_opcoes(self):
        layout = [
            [sg.Text("Menu Pagamento", font=("Helvetica", 15))],
            [sg.Button("Cadastrar Pagamento", key=1)],
            [sg.Button("Listar Pagamentos", key=2)],
            [sg.Button("Excluir Pagamento", key=3)],
            [sg.Button("Voltar", key=0)]
        ]

        window = sg.Window("Menu Pagamento", layout)
        event, _ = window.read()
        window.close()
        return event if event in (0, 1, 2, 3) else 0

    def pega_dados_pagamento(self):
        layout = [
            [sg.Text("CPF do Passageiro:"), sg.Input(key="cpf_passageiro")],
            [sg.Text("Valor Total (R$):"), sg.Input(key="valor_total")],
            [sg.Text("Data (DD/MM/AAAA):"), sg.Input(key="data")],
            [sg.Text("Pagou?"), sg.Combo(["Sim", "Não"], key="pagou", readonly=True)],

            [sg.Text("Forma de Pagamento:")],
            [sg.Combo(["cartao", "pix", "cedulas"], key="forma_pagamento", readonly=True)],

            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Cadastro de Pagamento", layout)
        event, values = window.read()
        window.close()

        if event == "Confirmar":
            return {
                "cpf_passageiro": values["cpf_passageiro"],
                "valor_total": values["valor_total"],
                "data": values["data"],
                "pagou": values["pagou"] == "Sim",
                "forma_pagamento": values["forma_pagamento"]
            }
        return None

    def pega_dados_cartao(self):
        layout = [
            [sg.Text("Número do Cartão:"), sg.Input(key="numero_cartao")],
            [sg.Text("Validade:"), sg.Input(key="validade")],
            [sg.Text("Bandeira:"), sg.Input(key="bandeira")],
            [sg.Text("Nome do Titular:"), sg.Input(key="nome_titular")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Dados do Cartão", layout)
        event, values = window.read()
        window.close()

        return values if event == "Confirmar" else None

    def pega_dados_pix(self):
        layout = [
            [sg.Text("Chave Pix:"), sg.Input(key="chave_pix")],
            [sg.Text("Banco:"), sg.Input(key="banco")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Dados Pix", layout)
        event, values = window.read()
        window.close()

        return values if event == "Confirmar" else None

    def mostra_pagamento(self, dados):
        sg.popup(
            f"Código: {dados['codigo']}\n"
            f"Forma: {dados['forma_pagamento']}\n"
            f"Valor: R$ {dados['valor_total']}\n"
            f"Data: {dados['data']}\n"
            f"Pagou: {dados['pagou']}\n"
            f"Passageiro: {dados['passageiro']}",
            title="Pagamento"
        )

    def seleciona_pagamento(self):
        layout = [
            [sg.Text("Digite o código do pagamento:")],
            [sg.Input(key="codigo")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Pagamento", layout)
        event, values = window.read()
        window.close()

        return int(values["codigo"]) if event == "Confirmar" else None

    def mostra_mensagem(self, msg):
        sg.popup(msg)
