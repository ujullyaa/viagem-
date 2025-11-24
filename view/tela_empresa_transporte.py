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

        window = sg.Window("Menu Empresa", layout, element_justification="center")
        resultado = window.read()
        window.close()
        
        if resultado is None:
            event = sg.WINDOW_CLOSED
        else:
            event = resultado[0]

        if event in (sg.WINDOW_CLOSED, "0 - Voltar ao Menu Principal"): return 0
        if event == "1 - Incluir Empresa": return 1
        if event == "2 - Alterar Empresa": return 2
        if event == "3 - Listar Empresas": return 3
        if event == "4 - Excluir Empresa": return 4
        return 0

    def pega_dados_empresa(self, empresa=None):
        # Valores Padrão
        nome_val = empresa.nome_empresa if empresa else ""
        cnpj_val = empresa.cnpj if empresa else ""
        ddd_val = ""
        num_val = ""

        # Lógica para preencher DDD e Número se for edição
        if empresa:
            tel_completo = str(empresa.telefone)
            tel_limpo = ''.join(filter(str.isdigit, tel_completo))
            if len(tel_limpo) >= 2:
                ddd_val = tel_limpo[:2]
                num_val = tel_limpo[2:]
            else:
                num_val = tel_limpo

        layout = [
            [sg.Text("🏢 Cadastro de Empresa", font=("Segoe UI", 14, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("Nome:", size=(15, 1)), sg.Input(nome_val, key="nome", size=(45, 1))],
            [sg.Text("CNPJ:", size=(15, 1)), sg.Input(cnpj_val, key="cnpj", disabled=(empresa is not None), size=(45, 1))],
            
            # --- Layout dividido para Telefone ---
            [
                sg.Text("Telefone:", size=(15, 1)), 
                sg.Text("DDD", size=(4,1), justification='right'), 
                sg.InputText(key="ddd", default_text=ddd_val, size=(5, 1)), 
                sg.Text("Número", size=(6,1), justification='right'), 
                sg.InputText(key="numero", default_text=num_val, size=(22, 1))
            ],
            [sg.Text("Ex: 48 e 3333-4444", font=("Segoe UI", 8), text_color="gray", pad=((140,0),(0,0)))],
            
            [sg.HorizontalSeparator()],
            [sg.Button("💾 Confirmar", key="confirmar", size=(20, 1)), sg.Button("↩️ Cancelar", key="cancelar", size=(20, 1))]
        ]

        window = sg.Window("Dados Empresa", layout, element_justification="center")
        resultado = window.read()
        window.close()

        if resultado is None:
            event = sg.WINDOW_CLOSED
            values = None
        else:
            event, values = resultado

        if event == "confirmar" and values is not None:
            # --- Lógica de Limpeza do Telefone ---
            ddd_limpo = ''.join(filter(str.isdigit, values['ddd']))
            numero_limpo = ''.join(filter(str.isdigit, values['numero']))
            
            # Verifica se o usuário repetiu o DDD no campo número
            if ddd_limpo and numero_limpo.startswith(ddd_limpo) and len(numero_limpo) >= 10:
                numero_limpo = numero_limpo[len(ddd_limpo):]

            telefone_completo = ddd_limpo + numero_limpo

            return {
                "nome": values["nome"], 
                "cnpj": values["cnpj"], 
                "telefone": telefone_completo
            }
        return None

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
            [sg.Button("Voltar", size=(20, 1))] 
        ]

        window = sg.Window("Lista", layout, size=(800, 400), element_justification="center")
        window.read() 
        window.close() 

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
            resultado = window.read()
            if resultado is None:
                break
            
            event, values = resultado
            
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                break
            
            if event == "Confirmar":
                if values["tabela"]:
                    idx = values["tabela"][0]
                    selected_cnpj = rows[idx][0] 
                    break
                else:
                    sg.popup("Selecione uma linha!", title="Aviso")
        
        window.close()
        return selected_cnpj

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Mensagem", font=("Segoe UI", 11))