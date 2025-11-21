import FreeSimpleGUI as sg

class TelaPassagem:
    def tela_opcoes(self):
        layout = [
            [sg.Text("🎫  Menu de Passagens", font=("Segoe UI", 18, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Button("1 - Incluir Passagem", size=(30, 1))],
            [sg.Button("2 - Alterar Passagem", size=(30, 1))],
            [sg.Button("3 - Listar Passagens", size=(30, 1))],
            [sg.Button("4 - Excluir Passagem", size=(30, 1))],
            [sg.HorizontalSeparator()],
            [sg.Button("0 - Voltar ao Menu Principal", button_color=("white", "red"), size=(30, 1))]
        ]

        window = sg.Window("Menu Passagens", layout, element_justification="center")
        event, _ = window.read()
        window.close()

        if event in (sg.WINDOW_CLOSED, "0 - Voltar ao Menu Principal"): return 0
        if event == "1 - Incluir Passagem": return 1
        if event == "2 - Alterar Passagem": return 2
        if event == "3 - Listar Passagens": return 3
        if event == "4 - Excluir Passagem": return 4
        return -1

    def pega_dados_passagem(self):
        layout = [
            [sg.Text("🎫  Cadastro de Passagem", font=("Segoe UI", 18, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("Número da Passagem:", size=(20, 1)), sg.Input(key="numero", size=(40, 1))],
            [sg.Text("Assento:", size=(20, 1)), sg.Input(key="assento", size=(40, 1))],
            [sg.Text("Data da Viagem:", size=(20, 1)), sg.Input(key="data_viagem", size=(40, 1))],
            [sg.Text("Valor (R$):", size=(20, 1)), sg.Input(key="valor", size=(40, 1))],
            [sg.HorizontalSeparator()],
            [sg.Button("💾  Confirmar", key="confirmar"), sg.Button("↩️  Cancelar", key="cancelar")]
        ]

        window = sg.Window("Cadastro de Passagem", layout, element_justification="center")
        event, values = window.read()
        window.close()

        if event == "confirmar":
            return {
                "numero": values.get("numero", "").strip(),
                "assento": values.get("assento", "").strip(),
                "data_viagem": values.get("data_viagem", "").strip(),
                "valor": values.get("valor", "").strip()
            }
        return None

    def mostra_passagem(self, dados):
        texto = (
            f"🎫 Número: {dados.get('numero', '')}\n"
            f"💺 Assento: {dados.get('assento', '')}\n"
            f"📅 Data: {dados.get('data_viagem', '')}\n"
            f"💰 Valor: {dados.get('valor', '')}\n"
            f"🧑 Pessoa: {dados.get('pessoa', '')}\n"
            f"🚌 Transporte: {dados.get('meio_transporte', '')}\n"
            f"💲 Status Pagamento: {dados.get('status_pagamento', 'N/A')}"
        )
        sg.popup_scrolled(texto, title="📋 Detalhes da Passagem", font=("Segoe UI", 11), size=(40, 12))

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Mensagem", font=("Segoe UI", 11))

    def seleciona_passagem(self):
        layout = [
            [sg.Text("Digite o número da passagem:", font=("Segoe UI", 12))],
            [sg.Input(key="numero", size=(40, 1))],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Selecionar Passagem", layout, element_justification="center")
        event, values = window.read()
        window.close()

        if event == "Confirmar":
            return values.get("numero", "").strip()
        return None

    def seleciona_meio_transporte(self):
        layout = [
            [sg.Text("Digite o TIPO do meio de transporte (ex: Onibus, Carro):", font=("Segoe UI", 12))],
            [sg.Input(key="tipo", size=(40, 1))],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Selecionar Transporte", layout, element_justification="center")
        event, values = window.read()
        window.close()

        if event == "Confirmar":
            return values.get("tipo", "").strip()
        return None

    # --- AQUI ESTÁ A MUDANÇA PRINCIPAL: TABELA EM VEZ DE INPUT ---
    def seleciona_itinerario(self, dados_itinerarios):
        if not dados_itinerarios:
            sg.popup("Nenhum itinerário cadastrado para selecionar.", title="Aviso")
            return None

        headers = ["Código", "Origem", "Destino", "Data Início"]
        rows = [[i['codigo'], i['origem'], i['destino'], i['inicio']] for i in dados_itinerarios]

        layout = [
            [sg.Text("Selecione o Itinerário:", font=("Segoe UI", 14, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Table(values=rows, headings=headers, max_col_width=50, auto_size_columns=True,
                      expand_x=True, expand_y=True, justification='center',
                      key="tabela_itinerarios", enable_events=True, select_mode='browse')],
            [sg.HorizontalSeparator()],
            [sg.Button("Confirmar", size=(20, 1)), sg.Button("Cancelar", size=(20, 1))]
        ]

        window = sg.Window("Selecionar Itinerário", layout, size=(800, 400), element_justification="center")
        
        codigo_selecionado = None
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                break
            
            if event == "Confirmar":
                selected_rows = values.get("tabela_itinerarios")
                if selected_rows:
                    index = selected_rows[0]
                    # O código é a coluna 0
                    codigo_selecionado = rows[index][0]
                    break
                else:
                    sg.popup("Selecione uma linha da tabela antes de confirmar.")

        window.close()
        return codigo_selecionado

    def confirma_pagamento_visual(self, valor, nome_pessoa):
        layout = [
            [sg.Text("💲 Verificação de Pagamento", font=("Segoe UI", 16, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text(f"Cliente: {nome_pessoa}", font=("Segoe UI", 12))],
            [sg.Text(f"Valor a pagar: R$ {valor}", font=("Segoe UI", 12))],
            [sg.Text("O pagamento foi realizado?", font=("Segoe UI", 12))],
            [sg.HorizontalSeparator()],
            [sg.Button("Sim (Pago)", key="sim", button_color="green", size=(15,1)), 
            sg.Button("Não (Pendente)", key="nao", button_color="red", size=(15,1))]
        ]
        window = sg.Window("Status Pagamento", layout, element_justification="center")
        event, _ = window.read()
        window.close()
        
        return event == "sim"