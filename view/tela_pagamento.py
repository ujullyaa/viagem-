import FreeSimpleGUI as sg

class TelaPagamento:
    def __init__(self):
        sg.theme("DarkBlue3")

    def tela_opcoes(self):
        layout = [
            [sg.Column(
                [
                    [sg.Text("💰 Menu Pagamentos", font=("Segoe UI", 18, "bold"))],
                    [sg.HorizontalSeparator()],
                    [sg.Button("1 - Cadastrar Pagamento", size=(35, 1))],
                    [sg.Button("2 - Alterar Pagamento", size=(35, 1))],
                    [sg.Button("3 - Listar Pagamentos", size=(35, 1))],
                    [sg.Button("4 - Excluir Pagamento", size=(35, 1))],
                    [sg.HorizontalSeparator()],
                    [sg.Button("0 - Voltar ao Menu Principal", button_color=("white", "red"), size=(35, 1))]
                ],
                element_justification="center",
                expand_x=True
            )]
        ]
        
        window = sg.Window("Menu Pagamento", layout, element_justification="center")
        
        event, _ = window.read()
        window.close()

        if event in (sg.WINDOW_CLOSED, "0 - Voltar ao Menu Principal"): return 0
        
        opcoes = {
            "1 - Cadastrar Pagamento": 1,
            "2 - Alterar Pagamento": 2,
            "3 - Listar Pagamentos": 3,
            "4 - Excluir Pagamento": 4
        }
        return opcoes.get(event, 0)

    def pega_dados_pagamento(self, pagamento=None):
        # Valores padrão
        val_cpf = pagamento.passageiro.cpf if pagamento else ""
        val_total = str(pagamento.valor_total) if pagamento else ""
        val_data = pagamento.data if pagamento else ""
        
        def_pagou = "Sim" if (pagamento and pagamento.pagou) else "Não"
        if not pagamento: def_pagou = ""

        def_forma = pagamento.forma_pagamento if pagamento else ""

        layout = [
            [sg.Text("💰 Dados do Pagamento", font=("Segoe UI", 14, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("CPF Passageiro:", size=(15,1)), sg.Input(default_text=val_cpf, key="cpf_passageiro", size=(45,1))],
            [sg.Text("Valor Total:", size=(15,1)), sg.Input(default_text=val_total, key="valor_total", size=(45,1))],
            [sg.Text("Data:", size=(15,1)), sg.Input(default_text=val_data, key="data", size=(45,1))],
            [sg.Text("Status:", size=(15,1)), sg.Combo(["Sim", "Não"], default_value=def_pagou, key="pagou", readonly=True, size=(43,1))],
            [sg.Text("Forma:", size=(15,1)), sg.Combo(["cartao", "pix", "cedulas"], default_value=def_forma, key="forma_pagamento", readonly=True, size=(43,1))],
            [sg.HorizontalSeparator()],
            [sg.Button("Confirmar", size=(20,1)), sg.Button("Cancelar", size=(20,1))]
        ]

        window = sg.Window("Dados Pagamento", layout, element_justification="center")
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
            [sg.Text("💳 Detalhes do Cartão", font=("Segoe UI", 14, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("Número:", size=(15,1)), sg.Input(key="numero_cartao", size=(45,1))],
            [sg.Text("Validade:", size=(15,1)), sg.Input(key="validade", size=(45,1))],
            [sg.Text("Bandeira:", size=(15,1)), sg.Input(key="bandeira", size=(45,1))],
            [sg.Text("Titular:", size=(15,1)), sg.Input(key="nome_titular", size=(45,1))],
            [sg.HorizontalSeparator()],
            [sg.Button("Confirmar", size=(20,1)), sg.Button("Cancelar", size=(20,1))]
        ]
        window = sg.Window("Cartão", layout, element_justification="center")
        event, values = window.read()
        window.close()
        return values if event == "Confirmar" else None

    def pega_dados_pix(self):
        layout = [
            [sg.Text("💠 Detalhes do PIX", font=("Segoe UI", 14, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("Chave:", size=(15,1)), sg.Input(key="chave_pix", size=(45,1))],
            [sg.Text("Banco:", size=(15,1)), sg.Input(key="banco", size=(45,1))],
            [sg.HorizontalSeparator()],
            [sg.Button("Confirmar", size=(20,1)), sg.Button("Cancelar", size=(20,1))]
        ]
        window = sg.Window("Pix", layout, element_justification="center")
        event, values = window.read()
        window.close()
        return values if event == "Confirmar" else None

    def mostra_pagamentos(self, lista_dados):
        if not lista_dados:
            sg.popup("Nenhum pagamento para mostrar.", title="Aviso")
            return

        headers = ["Código", "Forma", "Valor", "Data", "Status", "Passageiro"]
        rows = [[d['codigo'], d['forma'], d['valor'], d['data'], d['status'], d['passageiro']] for d in lista_dados]

        layout = [
            [sg.Text("📋 Lista de Pagamentos", font=("Segoe UI", 14, "bold"))],
            [sg.Table(values=rows, headings=headers, max_col_width=50, auto_size_columns=True,
                    justification='center', expand_x=True, expand_y=True)],
            [sg.Button("Voltar", size=(20,1))]
        ]

        window = sg.Window("Lista Pagamentos", layout, size=(900, 400), element_justification="center")
        window.read()
        window.close()

    def seleciona_pagamento(self, lista_dados):
        if not lista_dados:
            sg.popup("Lista vazia.", title="Aviso")
            return None

        headers = ["Código", "Forma", "Valor", "Data", "Status", "Passageiro"]
        rows = [[d['codigo'], d['forma'], d['valor'], d['data'], d['status'], d['passageiro']] for d in lista_dados]

        layout = [
            [sg.Text("Selecione o Pagamento:", font=("Segoe UI", 14, "bold"))],
            [sg.Table(values=rows, headings=headers, max_col_width=50, auto_size_columns=True,
                    justification='center', key="tab", select_mode='browse', enable_events=True,
                    expand_x=True, expand_y=True)],
            [sg.Button("Confirmar", size=(20,1)), sg.Button("Cancelar", size=(20,1))]
        ]
        window = sg.Window("Seleção Pagamento", layout, size=(900, 400), element_justification="center")
        
        codigo_selecionado = None
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                break
            if event == "Confirmar":
                if values["tab"]:
                    idx = values["tab"][0]
                    codigo_selecionado = rows[idx][0]
                    break
                else:
                    sg.popup("Selecione uma linha!", title="Aviso")
        
        window.close()
        return codigo_selecionado

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Mensagem", font=("Segoe UI", 11))