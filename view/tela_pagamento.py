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
                    # Botões com keys numéricas explícitas
                    [sg.Button("1 - Cadastrar Pagamento", key=1, size=(35, 1))],
                    [sg.Button("2 - Alterar Pagamento", key=2, size=(35, 1))],
                    [sg.Button("3 - Listar Pagamentos", key=3, size=(35, 1))],
                    [sg.Button("4 - Excluir Pagamento", key=4, size=(35, 1))],
                    [sg.HorizontalSeparator()],
                    [sg.Button("0 - Voltar ao Menu Principal", key=0, button_color=("white", "red"), size=(35, 1))]
                ],
                element_justification="center",
                expand_x=True
            )]
        ]
        
        window = sg.Window("Menu Pagamento", layout, element_justification="center")
        resultado = window.read()
        window.close()

        # Verifica se a janela foi fechada no "X"
        if resultado is None:
            return 0
        
        event, _ = resultado

        # Lógica simples e à prova de falhas
        if event in (sg.WINDOW_CLOSED, None, 0, '0'):
            return 0
        
        # Se for 1, 2, 3 ou 4, retorna o próprio evento
        if event in [1, 2, 3, 4]:
            return event
            
        return 0

    # --- SELEÇÃO DE FORMA DE PAGAMENTO ---
    def seleciona_forma_pagamento(self):
        layout = [
            [sg.Text("💸 Escolha a forma de pagamento:", font=("Segoe UI", 12, "bold"))],
            [sg.Combo(["Cartão", "Pix", "Dinheiro"], key="forma", size=(30, 1), readonly=True)],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Pagamento", layout, element_justification="center")
        resultado = window.read()
        window.close()
        
        if resultado is None: return None
        event, values = resultado
        
        if event == "Confirmar" and values["forma"]:
            mapa = {"Cartão": "cartao", "Pix": "pix", "Dinheiro": "cedulas"}
            return mapa.get(values["forma"])
        return None

    # --- CADASTRO DE DADOS GERAIS ---
    def pega_dados_pagamento(self, pagamento=None):
        val_cpf = pagamento.passageiro.cpf if pagamento else ""
        val_total = str(pagamento.valor_total) if pagamento else ""
        val_data = pagamento.data if pagamento else ""
        
        def_pagou = "Sim" if (pagamento and pagamento.pagou) else "Não"
        def_forma = pagamento.forma_pagamento if pagamento else ""

        label_size = (15, 1)
        input_size = (40, 1)

        layout = [
            [sg.Text("💰 Dados do Pagamento", font=("Segoe UI", 14, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("CPF Passageiro:", size=label_size, justification='right'), sg.Input(default_text=val_cpf, key="cpf_passageiro", size=input_size)],
            [sg.Text("Valor Total (R$):", size=label_size, justification='right'), sg.Input(default_text=val_total, key="valor_total", size=input_size)],
            [sg.Text("Data (dd/mm/aaaa):", size=label_size, justification='right'), sg.Input(default_text=val_data, key="data", size=input_size)],
            [sg.Text("Status:", size=label_size, justification='right'), sg.Combo(["Sim", "Não"], default_value=def_pagou, key="pagou", readonly=True, size=(38,1))],
            [sg.Text("Forma:", size=label_size, justification='right'), sg.Combo(["cartao", "pix", "cedulas"], default_value=def_forma, key="forma_pagamento", readonly=True, size=(38,1))],
            [sg.HorizontalSeparator()],
            [sg.Button("Confirmar", size=(20,1)), sg.Button("Cancelar", size=(20,1))]
        ]

        window = sg.Window("Dados Pagamento", layout, element_justification="center")
        resultado = window.read()
        window.close()

        if resultado is None: return None
        event, values = resultado

        if event == "Confirmar" and values is not None:
            return {
                "cpf_passageiro": values["cpf_passageiro"].strip(),
                "valor_total": values["valor_total"].strip(),
                "data": values["data"].strip(),
                "pagou": values["pagou"] == "Sim",
                "forma_pagamento": values["forma_pagamento"]
            }
        return None

    def pega_dados_cartao(self):
        label_size = (15, 1)
        input_size = (40, 1)
        layout = [
            [sg.Text("💳 Detalhes do Cartão", font=("Segoe UI", 14, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("Número:", size=label_size, justification='right'), sg.Input(key="numero_cartao", size=input_size)],
            [sg.Text("Validade:", size=label_size, justification='right'), sg.Input(key="validade", size=input_size)],
            [sg.Text("Bandeira:", size=label_size, justification='right'), sg.Input(key="bandeira", size=input_size)],
            [sg.Text("Titular:", size=label_size, justification='right'), sg.Input(key="nome_titular", size=input_size)],
            [sg.HorizontalSeparator()],
            [sg.Button("Confirmar", size=(20,1)), sg.Button("Cancelar", size=(20,1))]
        ]
        window = sg.Window("Cartão", layout, element_justification="center")
        resultado = window.read()
        window.close()
        if resultado is None: return None
        return resultado[1] if resultado[0] == "Confirmar" else None

    def pega_dados_pix(self):
        label_size = (15, 1)
        input_size = (40, 1)
        layout = [
            [sg.Text("💠 Detalhes do PIX", font=("Segoe UI", 14, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("Chave:", size=label_size, justification='right'), sg.Input(key="chave_pix", size=input_size)],
            [sg.Text("Banco:", size=label_size, justification='right'), sg.Input(key="banco", size=input_size)],
            [sg.HorizontalSeparator()],
            [sg.Button("Confirmar", size=(20,1)), sg.Button("Cancelar", size=(20,1))]
        ]
        window = sg.Window("Pix", layout, element_justification="center")
        resultado = window.read()
        window.close()
        if resultado is None: return None
        return resultado[1] if resultado[0] == "Confirmar" else None

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
            resultado = window.read()
            if resultado is None: break
            event, values = resultado
            if event in (sg.WINDOW_CLOSED, "Cancelar"): break
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