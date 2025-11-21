import FreeSimpleGUI as sg

class TelaItinerario:

    def tela_opcoes(self):
        layout = [
            [sg.Column(
                [
                    [sg.Text("🗺️  Menu Itinerário", font=("Segoe UI", 18, "bold"))],
                    [sg.HorizontalSeparator()],
                    [sg.Button("1 - Incluir Itinerário", size=(35, 1))],
                    [sg.Button("2 - Alterar Itinerário", size=(35, 1))],
                    [sg.Button("3 - Listar Itinerários", size=(35, 1))],
                    [sg.Button("4 - Excluir Itinerário", size=(35, 1))],
                    [sg.HorizontalSeparator()],
                    [sg.Button("0 - Voltar ao Menu Principal", button_color=("white", "red"), size=(35, 1))]
                ],
                element_justification="center"
            )]
        ]
        window = sg.Window("Menu Itinerário", layout, element_justification="center")
        result = window.read()
        window.close()
        
        event = result[0] if result else sg.WINDOW_CLOSED
        
        if event in (sg.WINDOW_CLOSED, "0 - Voltar ao Menu Principal"): return 0
        if event == "1 - Incluir Itinerário": return 1
        if event == "2 - Alterar Itinerário": return 2
        if event == "3 - Listar Itinerários": return 3
        if event == "4 - Excluir Itinerário": return 4
        return -1

    def pega_dados_itinerario(self, itinerario=None):
        codigo_default = itinerario.codigo_itinerario if itinerario else ""
        origem_default = itinerario.origem if itinerario else ""
        destino_default = itinerario.destino if itinerario else ""
        data_inicio_default = itinerario.data_inicio if itinerario else ""
        data_fim_default = itinerario.data_fim if itinerario else ""
        
        layout = [
            [sg.Text("🗺️ Cadastro de Itinerário", font=("Segoe UI", 18, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("Código do Itinerário:", size=(20,1)), sg.Input(default_text=codigo_default, key="codigo_itinerario", disabled=itinerario is not None, size=(45, 1))],
            [sg.Text("Origem:", size=(20,1)), sg.Input(default_text=origem_default, key="origem", size=(45, 1))],
            [sg.Text("Destino:", size=(20,1)), sg.Input(default_text=destino_default, key="destino", size=(45, 1))],
            [sg.Text("Data Início (DD/MM/AAAA):", size=(20,1)), sg.Input(default_text=data_inicio_default, key="data_inicio", size=(45, 1))],
            [sg.Text("Data Fim (DD/MM/AAAA):", size=(20,1)), sg.Input(default_text=data_fim_default, key="data_fim", size=(45, 1))],
            [sg.HorizontalSeparator()],
            [sg.Button("💾 Confirmar", key="confirmar", size=(20, 1)), sg.Button("↩️ Cancelar", key="cancelar", size=(20, 1))]
        ]
        window = sg.Window("Cadastro/Alteração de Itinerário", layout, element_justification="center")
        result = window.read()
        window.close()
        
        event = result[0] if result else sg.WINDOW_CLOSED
        values = result[1] if result else None

        if values is None or event in (sg.WINDOW_CLOSED, "cancelar"):
            return None
            
        if event == "confirmar":
            return {
                "codigo_itinerario": values.get("codigo_itinerario", "").strip(),
                "origem": values.get("origem", "").strip(),
                "destino": values.get("destino", "").strip(),
                "data_inicio": values.get("data_inicio", "").strip(),
                "data_fim": values.get("data_fim", "").strip()
            }
        return None

    def mostra_itinerario(self, dados_itinerario):
        if isinstance(dados_itinerario, list):
            if not dados_itinerario:
                sg.popup("Nenhum itinerário encontrado.", title="📋 Lista de Itinerários")
                return
            
            headers = ["Código", "Origem", "Destino", "Data Início", "Data Fim"]
            rows = []
            for itinerario in dados_itinerario:
                rows.append([
                    itinerario.get('codigo_itinerario', ''),
                    itinerario.get('origem', ''),
                    itinerario.get('destino', ''),
                    itinerario.get('data_inicio', ''),
                    itinerario.get('data_fim', '')
                ])
            
            layout = [
                [sg.Text("📋 Lista de Itinerários", font=("Segoe UI", 14, "bold"))],
                [sg.HorizontalSeparator()],
                [sg.Table(values=rows, headings=headers, max_col_width=50, auto_size_columns=True, 
                          expand_x=True, expand_y=True, justification='center',
                          key="tabela_itinerarios", enable_events=True, select_mode='browse')],
                [sg.Button("Confirmar", key="confirmar", size=(20, 1)), sg.Button("Cancelar", key="cancelar", size=(20, 1))]
            ]
            window = sg.Window("Lista de Itinerários", layout, size=(800, 400), element_justification="center")
            while True:
                result = window.read()
                event = result[0] if result else sg.WINDOW_CLOSED
                values = result[1] if result else None

                if event in (sg.WINDOW_CLOSED, "cancelar"):
                    window.close()
                    return None

                if event == "confirmar":
                    selected = values.get("tabela_itinerarios") if values else []
                    if selected:
                        idx = selected[0]
                        codigo = rows[idx][0]
                        window.close()
                        return codigo
                    else:
                        sg.popup("Selecione um itinerário antes de confirmar.", title="Aviso")
            window.close()
        else:
            texto = (
                f"🗺️ Código: {dados_itinerario.get('codigo_itinerario','')}\n"
                f"🏠 Origem: {dados_itinerario.get('origem','')}\n"
                f"🏁 Destino: {dados_itinerario.get('destino','')}\n"
                f"📅 Data Início: {dados_itinerario.get('data_inicio','')}\n"
                f"📅 Data Fim: {dados_itinerario.get('data_fim','')}\n"
                f"🎫 Passagens: {', '.join(dados_itinerario.get('passagens',[])) if dados_itinerario.get('passagens') else 'Nenhuma'}"
            )
            sg.popup_scrolled(texto, title="📋 Itinerário", font=("Segoe UI", 11))

    def seleciona_itinerario(self):
        layout = [
            [sg.Text("Digite o Código do Itinerário:", size=(25,1))],
            [sg.Input(key="codigo_itinerario")],
            [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]
        ]
        window = sg.Window("Selecionar Itinerário", layout)
        result = window.read()
        window.close()
        
        event = result[0] if result else sg.WINDOW_CLOSED
        values = result[1] if result else None

        if event == "confirmar":
            return values.get("codigo_itinerario", "").strip()
        return None

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Mensagem")

    # --- NOVO MÉTODO ---
    def confirmar_cadastro_passagem(self):
        # Popup simples do PySimpleGUI que retorna "Yes" ou "No"
        resposta = sg.popup_yes_no("Itinerário cadastrado!\nDeseja cadastrar uma passagem para este itinerário agora?", 
                                title="Cadastrar Passagem?", 
                                font=("Segoe UI", 11))
        return resposta == "Yes"