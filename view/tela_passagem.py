import FreeSimpleGUI as sg

class TelaPassagem:
    def __init__(self):
        sg.theme("DarkBlue3")

    def tela_opcoes(self):
        layout = [
            [sg.Column(
                [
                    [sg.Text("🎫 Menu de Passagens", font=("Segoe UI", 18, "bold"))],
                    [sg.HorizontalSeparator()],
                    [sg.Button("1 - Incluir Passagem", size=(35, 1))],
                    [sg.Button("2 - Alterar Passagem", size=(35, 1))],
                    [sg.Button("3 - Listar Passagens", size=(35, 1))],
                    [sg.Button("4 - Excluir Passagem", size=(35, 1))],
                    [sg.HorizontalSeparator()],
                    [sg.Button("0 - Voltar ao Menu Principal", button_color=("white", "red"), size=(35, 1))]
                ],
                element_justification="center",
                expand_x=True
            )]
        ]
        window = sg.Window("Menu Passagens", layout, element_justification="center")
        resultado = window.read()
        window.close()

        if resultado is None:
            event = sg.WINDOW_CLOSED
        else:
            event = resultado[0]

        if event in (sg.WINDOW_CLOSED, "0 - Voltar ao Menu Principal"): return 0
        
        opcoes = {
            "1 - Incluir Passagem": 1,
            "2 - Alterar Passagem": 2,
            "3 - Listar Passagens": 3,
            "4 - Excluir Passagem": 4
        }
        return opcoes.get(event, 0)

    def pega_dados_passagem(self, passagem=None):
        val_num = passagem.numero if passagem else ""
        val_assento = passagem.assento if passagem else ""
        val_data = passagem.data_viagem if passagem else ""
        val_valor = passagem.valor if passagem else ""

        # --- CORREÇÃO VISUAL ---
        label_size = (20, 1)
        input_size = (40, 1)

        layout = [
            [sg.Text("🎫 Dados da Passagem", font=("Segoe UI", 14, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("Número:", size=label_size, justification='right'), sg.Input(val_num, key="numero", size=input_size, disabled=(passagem is not None))],
            [sg.Text("Assento:", size=label_size, justification='right'), sg.Input(val_assento, key="assento", size=input_size)],
            [sg.Text("Data (dd/mm/aaaa):", size=label_size, justification='right'), sg.Input(val_data, key="data_viagem", size=input_size)],
            [sg.Text("Valor (R$):", size=label_size, justification='right'), sg.Input(str(val_valor), key="valor", size=input_size)],
            [sg.HorizontalSeparator()],
            [sg.Button("💾 Confirmar", key="confirmar", size=(20,1)), sg.Button("↩️ Cancelar", key="cancelar", size=(20,1))]
        ]

        window = sg.Window("Dados Passagem", layout, element_justification="center")
        resultado = window.read()
        window.close()

        if resultado is None:
            event = sg.WINDOW_CLOSED
            values = None
        else:
            event, values = resultado

        if event == "confirmar" and values is not None:
            return {
                "numero": values.get("numero", "").strip(),
                "assento": values.get("assento", "").strip(),
                "data_viagem": values.get("data_viagem", "").strip(),
                "valor": values.get("valor", "").strip()
            }
        return None

    # --- SELEÇÃO DE VEÍCULO POR TABELA (Adicionado) ---
    def seleciona_meio_transporte(self, lista_meios):
        if not lista_meios:
            sg.popup("Nenhum veículo cadastrado.", title="Erro")
            return None

        headers = ["Tipo", "Capacidade", "Empresa"]
        rows = []
        mapa_objetos = {}

        for idx, m in enumerate(lista_meios):
            empresa = m.empresa_transporte.nome_empresa if hasattr(m, 'empresa_transporte') and m.empresa_transporte else "N/A"
            rows.append([m.tipo, m.capacidade, empresa])
            mapa_objetos[idx] = m

        layout = [
            [sg.Text("🚌 Selecione o Veículo:", font=("Segoe UI", 14, "bold"))],
            [sg.Table(values=rows, headings=headers, max_col_width=50, auto_size_columns=True,
                        justification='center', key="tab", select_mode='browse', 
                        expand_x=True, expand_y=True)],
            [sg.Button("Confirmar", size=(20,1)), sg.Button("Cancelar", size=(20,1))]
        ]
        
        window = sg.Window("Seleção Transporte", layout, size=(700, 400), element_justification="center")
        obj_selecionado = None
        
        while True:
            resultado = window.read()
            if resultado is None: break
            event, values = resultado
            if event in (sg.WINDOW_CLOSED, "Cancelar"): break
            
            if event == "Confirmar":
                if values["tab"]:
                    idx = values["tab"][0]
                    obj_selecionado = mapa_objetos[idx]
                    break
                else:
                    sg.popup("Selecione uma linha.", title="Aviso")
        window.close()
        return obj_selecionado

    # --- SELEÇÃO DE ITINERÁRIO POR TABELA (Adicionado) ---
    def seleciona_itinerario(self, dados):
        if not dados: 
            sg.popup("Nenhum itinerário disponível.", title="Aviso")
            return None
            
        headers=["Cod", "Origem", "Destino", "Inicio"]
        rows = [[d['codigo'], d['origem'], d['destino'], d['inicio']] for d in dados]
        layout=[
            [sg.Text("🗺️ Selecione o Itinerário:", font=("Segoe UI", 14, "bold"))],
            [sg.Table(values=rows, headings=headers, key="tab", select_mode='browse', 
                        justification='center', expand_x=True, expand_y=True)], 
            [sg.Button("Confirmar", size=(20,1)), sg.Button("Cancelar", size=(20,1))]
        ]
        window = sg.Window("Seleção Itinerário", layout, size=(700,400), element_justification="center")
        res = None
        while True:
            resultado = window.read()
            if resultado is None: break
            e,v = resultado
            if e in (sg.WINDOW_CLOSED, "Cancelar"): break
            if e == "Confirmar":
                if v["tab"]: 
                    res = rows[v["tab"][0]][0]
                    break
                else: 
                    sg.popup("Selecione um itinerário.")
        window.close()
        return res

    def seleciona_passagem_por_lista(self, dados_passagens):
        if not dados_passagens:
            sg.popup("Nenhuma passagem para selecionar.", title="Aviso")
            return None

        headers = ["Número", "Pessoa", "Data", "Assento", "Valor"]
        rows = [[p['numero'], p['pessoa'], p['data'], p['assento'], p['valor']] for p in dados_passagens]

        layout = [
            [sg.Text("Selecione a Passagem:", font=("Segoe UI", 14, "bold"))],
            [sg.Table(values=rows, headings=headers, max_col_width=50, auto_size_columns=True,
                        justification='center', key="tab", select_mode='browse', enable_events=True,
                        expand_x=True, expand_y=True)],
            [sg.Button("Confirmar", size=(20,1)), sg.Button("Cancelar", size=(20,1))]
        ]
        window = sg.Window("Seleção Passagem", layout, size=(900, 400), element_justification="center")
        
        numero_selecionado = None
        while True:
            resultado = window.read()
            if resultado is None: break
            event, values = resultado
            if event in (sg.WINDOW_CLOSED, "Cancelar"): break
            if event == "Confirmar":
                if values["tab"]:
                    idx = values["tab"][0]
                    numero_selecionado = rows[idx][0] 
                    break
                else:
                    sg.popup("Selecione uma linha!", title="Aviso")
        
        window.close()
        return numero_selecionado

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

    def confirma_pagamento_visual(self, val, nome):
        return sg.popup_yes_no(f"Iniciar processo de pagamento de R${val} para {nome}?", title="Pagamento") == "Yes"