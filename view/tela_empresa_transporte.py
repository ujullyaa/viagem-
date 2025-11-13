# view/tela_empresa_transporte.py
import FreeSimpleGUI as sg

class TelaEmpresaTransporte:
    def tela_opcoes(self):
        layout = [
            [sg.Text("🏢  Menu Empresa de Transporte", font=("Segoe UI", 16, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Button("1 - Cadastrar Empresa")],
            [sg.Button("2 - Alterar Empresa")],
            [sg.Button("3 - Listar Empresas")],
            [sg.Button("4 - Excluir Empresa")],
            [sg.Button("0 - Voltar ao Menu Principal", button_color=("white", "red"))],
        ]
        window = sg.Window("Menu Empresa de Transporte", layout)
        result = window.read()
        window.close()
        
        event = result[0] if result else sg.WINDOW_CLOSED
        _ = result[1] if result else None

        if event in (sg.WINDOW_CLOSED, "0 - Voltar ao Menu Principal"):
            return 0
        elif event == "1 - Cadastrar Empresa":
            return 1
        elif event == "2 - Alterar Empresa":
            return 2
        elif event == "3 - Listar Empresas":
            return 3
        elif event == "4 - Excluir Empresa":
            return 4
        return -1

    def pega_dados_empresa(self, empresa=None):
        """Se receber empresa, preenche os campos para alteração."""
        layout = [
            [sg.Text("🏢 Cadastro de Empresa", font=("Segoe UI", 16, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("Nome da Empresa:", size=(18,1)), sg.Input(default_text=(empresa.nome_empresa if empresa else ""), key="nome_empresa")],
            [sg.Text("CNPJ:", size=(18,1)), sg.Input(default_text=(empresa.cnpj if empresa else ""), key="cnpj")],
            [sg.Text("Telefone:", size=(18,1)), sg.Input(default_text=(empresa.telefone if empresa else ""), key="telefone")],
            [sg.HorizontalSeparator()],
            [sg.Button("💾 Confirmar", key="confirmar"), sg.Button("↩️ Cancelar", key="cancelar")]
        ]
        window = sg.Window("Cadastro de Empresa", layout)
        result = window.read()
        window.close()
        
        event = result[0] if result else sg.WINDOW_CLOSED
        values = result[1] if result else None

        if event == "confirmar" and values:
            return {
                "nome_empresa": values.get("nome_empresa", "").strip(),
                "cnpj": values.get("cnpj", "").strip(),
                "telefone": values.get("telefone", "").strip(),
            }
        return None

    def mostra_empresa(self, empresas):
        """Mostra uma ou várias empresas."""
        if not empresas:
            sg.popup("Nenhuma empresa cadastrada.", title="Empresas", font=("Segoe UI", 11))
            return
        
        # Se receber um dicionário, converte para lista
        if isinstance(empresas, dict):
            empresas = [empresas]
        
        texto = "\n\n".join([
            f"🏢 Nome: {e.get('nome_empresa','')}\n📞 Telefone: {e.get('telefone','')}\n🧾 CNPJ: {e.get('cnpj','')}"
            for e in empresas
        ])
        sg.popup_scrolled(texto, title="Empresas Cadastradas", font=("Segoe UI", 11))

    def seleciona_empresa_lista(self, empresas):
        """Mostra uma lista de empresas para selecionar pelo CNPJ."""
        if not empresas:
            sg.popup("Nenhuma empresa cadastrada.", title="Selecionar Empresa")
            return None
        lista = [f"{e.nome_empresa} - {e.cnpj}" for e in empresas]
        layout = [
            [sg.Text("Selecione a empresa:")],
            [sg.Listbox(values=lista, size=(40, 10), key="empresa")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Selecionar Empresa", layout)
        result = window.read()
        window.close()
        
        event = result[0] if result else sg.WINDOW_CLOSED
        values = result[1] if result else None

        if event == "Confirmar" and values and values.get("empresa"):
            return values["empresa"][0].split(" - ")[1]  # retorna apenas o CNPJ
        return None

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Mensagem", font=("Segoe UI", 11))
