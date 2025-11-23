import FreeSimpleGUI as sg

class TelaItinerario:
    def __init__(self):
        sg.theme("DarkBlue3")

    def tela_opcoes(self):
        layout = [
            [sg.Column(
                [
                    [sg.Text("🗺️ Menu Itinerário", font=("Segoe UI", 18, "bold"))],
                    [sg.HorizontalSeparator()],
                    [sg.Button("1 - Incluir Itinerário", size=(35, 1))],
                    [sg.Button("2 - Alterar Itinerário", size=(35, 1))],
                    [sg.Button("3 - Listar Itinerários", size=(35, 1))],
                    [sg.Button("4 - Excluir Itinerário", size=(35, 1))],
                    [sg.HorizontalSeparator()],
                    [sg.Button("0 - Voltar ao Menu Principal", button_color=("white", "red"), size=(35, 1))]
                ],
                element_justification="center",
                expand_x=True
            )]
        ]
        window = sg.Window("Menu Itinerário", layout, element_justification="center", size=(600, 500))
        
        event, _ = window.read()
        window.close()
        
        if event in (sg.WINDOW_CLOSED, "0 - Voltar ao Menu Principal"): return 0
        if event == "1 - Incluir Itinerário": return 1
        if event == "2 - Alterar Itinerário": return 2
        if event == "3 - Listar Itinerários": return 3
        if event == "4 - Excluir Itinerário": return 4
        return 0

    def pega_dados_itinerario(self, itinerario=None):
        # Valores padrão
        cod = itinerario.codigo_itinerario if itinerario else ""
        orig = itinerario.origem if itinerario else ""
        dest = itinerario.destino if itinerario else ""
        d_ini = itinerario.data_inicio if itinerario else ""
        d_fim = itinerario.data_fim if itinerario else ""
        
        layout = [
            [sg.Text("🗺️ Cadastro de Itinerário", font=("Segoe UI", 14, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("Código:", size=(15,1)), sg.Input(cod, key="codigo_itinerario", disabled=(itinerario is not None), size=(45, 1))],
            [sg.Text("Origem:", size=(15,1)), sg.Input(orig, key="origem", size=(45, 1))],
            [sg.Text("Destino:", size=(15,1)), sg.Input(dest, key="destino", size=(45, 1))],
            [sg.Text("Data Início(d/m/a)", size=(15,1)), sg.Input(d_ini, key="data_inicio", size=(45, 1))],
            [sg.Text("Data Fim(d/m/a)", size=(15,1)), sg.Input(d_fim, key="data_fim", size=(45, 1))],
            [sg.HorizontalSeparator()],
            [sg.Button("💾 Confirmar", key="confirmar", size=(20, 1)), sg.Button("↩️ Cancelar", key="cancelar", size=(20, 1))]
        ]
        window = sg.Window("Dados Itinerário", layout, element_justification="center")
        event, values = window.read()
        window.close()
        
        if event == "confirmar":
            return {
                "codigo_itinerario": values["codigo_itinerario"].strip(),
                "origem": values["origem"].strip(),
                "destino": values["destino"].strip(),
                "data_inicio": values["data_inicio"].strip(),
                "data_fim": values["data_fim"].strip()
            }
        return None

    # --- MÉTODO 1: APENAS LISTAR (Botão Voltar) ---
    def mostra_itinerarios(self, dados_itinerario):
        if not dados_itinerario:
            sg.popup("Nenhum itinerário encontrado.", title="Aviso")
            return
        
        headers = ["Código", "Origem", "Destino", "Início", "Fim"]
        rows = [[i['codigo_itinerario'], i['origem'], i['destino'], i['data_inicio'], i['data_fim']] for i in dados_itinerario]
        
        layout = [
            [sg.Text("📋 Lista de Itinerários", font=("Segoe UI", 14, "bold"))],
            [sg.Table(values=rows, headings=headers, max_col_width=50, auto_size_columns=True, 
                    expand_x=True, expand_y=True, justification='center')],
            [sg.Button("Voltar", size=(20, 1))] # Apenas voltar
        ]
        
        window = sg.Window("Itinerários", layout, size=(900, 400), element_justification="center")
        window.read()
        window.close()

    # --- MÉTODO 2: SELECIONAR (Botões Confirmar/Cancelar) ---
    def seleciona_itinerario(self, dados_itinerario):
        if not dados_itinerario: 
            sg.popup("Lista vazia.", title="Aviso")
            return None
        
        headers = ["Código", "Origem", "Destino", "Início", "Fim"]
        # Nota: Dependendo de quem chama, os nomes das chaves podem variar. 
        # O controlador está mandando 'codigo_itinerario' no CRUD de Itinerário
        # Mas 'codigo' no CRUD de Passagem. Vamos padronizar no controlador.
        # Aqui assumimos o padrão do CRUD Itinerário: 'codigo_itinerario'
        
        rows = []
        for i in dados_itinerario:
            # Tenta pegar 'codigo_itinerario', se não der tenta 'codigo' (fallback para compatibilidade)
            cod = i.get('codigo_itinerario', i.get('codigo', ''))
            orig = i.get('origem', '')
            dest = i.get('destino', '')
            ini = i.get('data_inicio', i.get('inicio', ''))
            fim = i.get('data_fim', '')
            rows.append([cod, orig, dest, ini, fim])
        
        layout = [
            [sg.Text("Selecione o Itinerário:", font=("Segoe UI", 14, "bold"))],
            [sg.Table(values=rows, headings=headers, max_col_width=50, auto_size_columns=True, key="tab", 
                    select_mode='browse', expand_x=True, expand_y=True, justification='center')],
            [sg.Button("Confirmar", size=(20, 1)), sg.Button("Cancelar", size=(20, 1))]
        ]
        window = sg.Window("Seleção", layout, size=(900, 400), element_justification="center")
        res = None
        while True:
            e, v = window.read()
            if e in (sg.WINDOW_CLOSED, "Cancelar"): break
            if e == "Confirmar":
                if v["tab"]:
                    res = rows[v["tab"][0]][0] # Retorna o Código (coluna 0)
                    break
                else:
                    sg.popup("Selecione uma linha.")
        window.close()
        return res

    def confirmar_cadastro_passagem(self):
        return sg.popup_yes_no("Itinerário criado! Deseja cadastrar passagens para ele agora?", title="Pergunta") == "Yes"

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Mensagem", font=("Segoe UI", 11))