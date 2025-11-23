import FreeSimpleGUI as sg

class TelaEmpresaTransporte:
    def __init__(self):
        sg.theme("DarkBlue3")

    def tela_opcoes(self):
        layout = [
            [sg.Column(
                [
                    [sg.Text("🏢 Menu Empresa", font=("Segoe UI", 18, "bold"))],
                    [sg.HorizontalSeparator()],
                    [sg.Button("1 - Incluir Empresa", size=(35, 1))],
                    [sg.Button("2 - Alterar Empresa", size=(35, 1))],
                    [sg.Button("3 - Listar Empresas", size=(35, 1))],
                    [sg.Button("4 - Excluir Empresa", size=(35, 1))],
                    [sg.HorizontalSeparator()],
                    [sg.Button("0 - Voltar ao Menu Principal", button_color=("white", "red"), size=(35, 1))]
                ],
                element_justification="center",
                expand_x=True
            )]
        ]

        window = sg.Window("Menu Empresa", layout, element_justification="center", size=(600, 500))
        event, _ = window.read()
        window.close()

        if event in (sg.WINDOW_CLOSED, "0 - Voltar ao Menu Principal"): return 0
        if event == "1 - Incluir Empresa": return 1
        if event == "2 - Alterar Empresa": return 2
        if event == "3 - Listar Empresas": return 3
        if event == "4 - Excluir Empresa": return 4
        return 0

    def pega_dados_empresa(self, empresa=None):
        nome = empresa.nome_empresa if empresa else ""
        cnpj = empresa.cnpj if empresa else ""
        tel = empresa.telefone if empresa else ""

        layout = [
            [sg.Text("🏢 Cadastro de Empresa", font=("Segoe UI", 14, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("Nome:", size=(15, 1)), sg.Input(nome, key="nome", size=(45, 1))],
            [sg.Text("CNPJ:", size=(15, 1)), sg.Input(cnpj, key="cnpj", disabled=(empresa is not None), size=(45, 1))],
            [sg.Text("Telefone:", size=(15, 1)), sg.Input(tel, key="telefone", size=(45, 1))],
            [sg.HorizontalSeparator()],
            [sg.Button("💾 Confirmar", key="confirmar", size=(20, 1)), sg.Button("↩️ Cancelar", key="cancelar", size=(20, 1))]
        ]

        window = sg.Window("Dados Empresa", layout, element_justification="center")
        event, values = window.read()
        window.close()

        if event == "confirmar":
            return {"nome": values["nome"], "cnpj": values["cnpj"], "telefone": values["telefone"]}
        return None

    # --- MÉTODO 1: APENAS LISTAR (CORRIGIDO O BOTÃO VOLTAR) ---
    def mostra_empresas(self, empresas):
        if not empresas:
            sg.popup("Nenhuma empresa encontrada.", title="Aviso")
            return

        headers = ["CNPJ", "Nome", "Telefone"]
        rows = [[e.cnpj, e.nome_empresa, e.telefone] for e in empresas]

        layout = [
            [sg.Text("📋 Lista de Empresas", font=("Segoe UI", 14, "bold"))],
            [sg.Table(values=rows, headings=headers, max_col_width=50, auto_size_columns=True,
                      justification='center', key="tabela", expand_x=True, expand_y=True)],
            [sg.Button("Voltar", size=(20, 1))] # Botão correto
        ]

        window = sg.Window("Lista", layout, size=(800, 400), element_justification="center")
        window.read() # Espera o clique
        window.close() # Fecha ao clicar em Voltar ou X

    # --- MÉTODO 2: SELECIONAR (PARA ALTERAR/EXCLUIR) ---
    def seleciona_empresa(self, empresas):
        if not empresas:
            sg.popup("Nenhuma empresa encontrada.", title="Aviso")
            return None

        headers = ["CNPJ", "Nome", "Telefone"]
        rows = [[e.cnpj, e.nome_empresa, e.telefone] for e in empresas]

        layout = [
            [sg.Text("Selecione a Empresa:", font=("Segoe UI", 14, "bold"))],
            [sg.Table(values=rows, headings=headers, max_col_width=50, auto_size_columns=True,
                      justification='center', key="tabela", enable_events=True, select_mode='browse', 
                      expand_x=True, expand_y=True)],
            [sg.Button("Confirmar", size=(20, 1)), sg.Button("Cancelar", size=(20, 1))]
        ]

        window = sg.Window("Seleção", layout, size=(800, 400), element_justification="center")
        
        selected_cnpj = None
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                break
            if event == "Confirmar":
                if values["tabela"]:
                    idx = values["tabela"][0]
                    selected_cnpj = rows[idx][0] # CNPJ é a primeira coluna
                    break
                else:
                    sg.popup("Selecione uma linha!", title="Aviso")
        
        window.close()
        return selected_cnpj

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Mensagem", font=("Segoe UI", 11))