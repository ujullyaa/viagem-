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
        event, _ = window.read()
        window.close()

        if event in (sg.WINDOW_CLOSED, "0 - Voltar ao Menu Principal"): return 0
        if event == "1 - Incluir Passagem": return 1
        if event == "2 - Alterar Passagem": return 2
        if event == "3 - Listar Passagens": return 3
        if event == "4 - Excluir Passagem": return 4
        return -1

    def pega_dados_passagem(self, passagem=None):
        # Valores padrão para alteração
        val_num = passagem.numero if passagem else ""
        val_assento = passagem.assento if passagem else ""
        val_data = passagem.data_viagem if passagem else ""
        val_valor = passagem.valor if passagem else ""

        layout = [
            [sg.Text("🎫 Dados da Passagem", font=("Segoe UI", 14, "bold"))],
            [sg.HorizontalSeparator()],
            # Número desabilitado se for edição (chave primária)
            [sg.Text("Número:", size=(15,1)), sg.Input(val_num, key="numero", size=(45,1), disabled=(passagem is not None))],
            [sg.Text("Assento:", size=(15,1)), sg.Input(val_assento, key="assento", size=(45,1))],
            [sg.Text("Data:", size=(15,1)), sg.Input(val_data, key="data_viagem", size=(45,1))],
            [sg.Text("Valor:", size=(15,1)), sg.Input(str(val_valor), key="valor", size=(45,1))],
            [sg.HorizontalSeparator()],
            [sg.Button("💾 Confirmar", key="confirmar", size=(20,1)), sg.Button("↩️ Cancelar", key="cancelar", size=(20,1))]
        ]

        window = sg.Window("Dados Passagem", layout, element_justification="center")
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

    # --- MÉTODOS DE SELEÇÃO VISUAL ---

    def seleciona_passagem_por_lista(self, dados_passagens):
        """
        Exibe uma tabela com as passagens e retorna o NÚMERO da passagem selecionada.
        """
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
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                break
            if event == "Confirmar":
                if values["tab"]:
                    idx = values["tab"][0]
                    numero_selecionado = rows[idx][0] # Número é a primeira coluna
                    break
                else:
                    sg.popup("Selecione uma linha!", title="Aviso")
        
        window.close()
        return numero_selecionado

    def seleciona_meio_transporte(self):
        layout = [[sg.Text("Tipo Transporte (ex: Onibus):", font=("Segoe UI", 12))], [sg.Input(key="tipo", size=(45,1))], [sg.Button("Confirmar"), sg.Button("Cancelar")]]
        w = sg.Window("Sel", layout, element_justification="center")
        e, v = w.read()
        w.close()
        return v["tipo"] if e=="Confirmar" else None

    def seleciona_itinerario(self, dados):
        if not dados: return None
        headers=["Cod", "Origem", "Destino", "Inicio"]
        rows = [[d['codigo'], d['origem'], d['destino'], d['inicio']] for d in dados]
        layout=[
            [sg.Text("Selecione Itinerário", font=("Segoe UI", 14, "bold"))],
            [sg.Table(values=rows, headings=headers, key="tab", select_mode='browse', expand_x=True, expand_y=True)], 
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        w = sg.Window("Itinerarios", layout, size=(600,400), element_justification="center")
        res = None
        while True:
            e,v = w.read()
            if e in (sg.WINDOW_CLOSED, "Cancelar"): break
            if e == "Confirmar":
                if v["tab"]: res=rows[v["tab"][0]][0]; break
        w.close()
        return res

    def confirma_pagamento_visual(self, val, nome):
        return sg.popup_yes_no(f"Cliente {nome} pagou R${val}?", title="Pagamento") == "Yes"