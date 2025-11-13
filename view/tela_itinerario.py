import FreeSimpleGUI as sg

class TelaItinerario:

    def tela_opcoes(self):
        layout = [
            [sg.Text("🗺️  Menu Itinerário", font=("Segoe UI", 18, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Button("1 - Incluir Itinerário")],
            [sg.Button("2 - Alterar Itinerário")],
            [sg.Button("3 - Listar Itinerários")],
            [sg.Button("4 - Excluir Itinerário")],
            [sg.Button("0 - Voltar ao Menu Principal", button_color=("white", "red"))]
        ]
        window = sg.Window("Menu Itinerário", layout, element_justification="center")
        result = window.read()
        window.close()
        event = result[0] if result else sg.WINDOW_CLOSED
        _ = result[1] if result else None

        if event in (sg.WINDOW_CLOSED, "0 - Voltar ao Menu Principal"):
            return 0
        elif event == "1 - Incluir Itinerário":
            return 1
        elif event == "2 - Alterar Itinerário":
            return 2
        elif event == "3 - Listar Itinerários":
            return 3
        elif event == "4 - Excluir Itinerário":
            return 4
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
            [sg.Text("Código do Itinerário:", size=(18,1)), sg.Input(default_text=codigo_default, key="codigo_itinerario", disabled=itinerario is not None)],
            [sg.Text("Origem:", size=(18,1)), sg.Input(default_text=origem_default, key="origem")],
            [sg.Text("Destino:", size=(18,1)), sg.Input(default_text=destino_default, key="destino")],
            [sg.Text("Data de Início (DD/MM/AAAA):", size=(18,1)), sg.Input(default_text=data_inicio_default, key="data_inicio")],
            [sg.Text("Data de Fim (DD/MM/AAAA):", size=(18,1)), sg.Input(default_text=data_fim_default, key="data_fim")],
            [sg.HorizontalSeparator()],
            [sg.Button("💾 Confirmar", key="confirmar"), sg.Button("↩️ Cancelar", key="cancelar")]
        ]
        window = sg.Window("Cadastro/Alteração de Itinerário", layout)
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

        if values is None or event in (sg.WINDOW_CLOSED, "cancelar"):
            return None
            
        if event == "confirmar":
            return values.get("codigo_itinerario", "").strip()
        return None

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Mensagem")
