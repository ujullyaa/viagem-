import FreeSimpleGUI as sg

class TelaPessoa:
    def __init__(self):
        sg.theme("DarkBlue3")

    def tela_opcoes(self):
        layout = [
            [sg.Column(
                [
                    [sg.Text("👤 Menu Pessoa", font=("Segoe UI", 18, "bold"))],
                    [sg.HorizontalSeparator()],
                    [sg.Button("1 - Cadastrar Pessoa", size=(35, 1))],
                    [sg.Button("2 - Alterar Pessoa", size=(35, 1))],
                    [sg.Button("3 - Listar Pessoas", size=(35, 1))],
                    [sg.Button("4 - Excluir Pessoa", size=(35, 1))],
                    [sg.HorizontalSeparator()],
                    [sg.Button("0 - Voltar ao Menu Principal", button_color=("white", "red"), size=(35, 1))]
                ],
                element_justification="center",
                expand_x=True
            )]
        ]

        window = sg.Window("Menu Pessoa", layout, element_justification='center')
        result = window.read()
        window.close()

        event = result[0] if result else sg.WINDOW_CLOSED
        
        if event in (sg.WINDOW_CLOSED, "0 - Voltar ao Menu Principal"): return 0
        if event == "1 - Cadastrar Pessoa": return 1
        if event == "2 - Alterar Pessoa": return 2
        if event == "3 - Listar Pessoas": return 3
        if event == "4 - Excluir Pessoa": return 4
        return 0

    def pega_dados_pessoa(self, pessoa_existente=None):
        nome_val = pessoa_existente.nome if pessoa_existente else ""
        cpf_val = pessoa_existente.cpf if pessoa_existente else ""
        idade_val = pessoa_existente.idade if pessoa_existente else ""
        tel_val = pessoa_existente.telefone if pessoa_existente else ""

        layout = [
            [sg.Text("👤 Cadastro de Pessoa", font=("Segoe UI", 18, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("Nome:", size=(20, 1)), sg.InputText(key="nome", default_text=nome_val, size=(45, 1))],
            [sg.Text("Idade:", size=(20, 1)), sg.InputText(key="idade", default_text=idade_val, size=(45, 1))],
            [sg.Text("CPF:", size=(20, 1)), sg.InputText(key="cpf", default_text=cpf_val, disabled=(pessoa_existente is not None), size=(45, 1))],
            [sg.Text("Telefone:", size=(20, 1)), sg.InputText(key="telefone", default_text=tel_val, size=(45, 1))],
            [sg.HorizontalSeparator()],
            [sg.Button("💾 Confirmar", size=(20, 1)), sg.Button("↩️ Cancelar", size=(20, 1))]
        ]

        window = sg.Window("Dados da Pessoa", layout, element_justification="center")
        result = window.read()
        window.close()

        event = result[0] if result else sg.WINDOW_CLOSED
        values = result[1] if result else None

        if event == "💾 Confirmar":
            return {
                "nome": values["nome"],
                "idade": values["idade"],
                "cpf": values["cpf"],
                "telefone": values["telefone"]
            }
        return None

    def mostra_pessoas(self, dados_pessoas):
        if not dados_pessoas:
            sg.popup("Nenhuma pessoa cadastrada.", title="Aviso")
            return
        
        headers = ["CPF", "Nome", "Idade", "Telefone"]
        rows = [[p['cpf'], p['nome'], p['idade'], p['telefone']] for p in dados_pessoas]

        layout = [
            [sg.Text("📋 Lista de Pessoas", font=("Segoe UI", 14, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Table(values=rows, headings=headers, max_col_width=50, auto_size_columns=True, 
                    expand_x=True, expand_y=True, justification='center', key="tabela_pessoas")],
            [sg.HorizontalSeparator()],
            [sg.Button("Voltar", size=(20, 1))]
        ]

        window = sg.Window("Lista de Pessoas", layout, size=(800, 400), element_justification="center")
        window.read()
        window.close()

    def seleciona_pessoa_por_lista(self, dados_pessoas):
        if not dados_pessoas:
            sg.popup("Nenhuma pessoa cadastrada para selecionar.", title="Aviso")
            return None

        headers = ["CPF", "Nome", "Idade", "Telefone"]
        rows = [[p['cpf'], p['nome'], p['idade'], p['telefone']] for p in dados_pessoas]

        layout = [
            [sg.Text("Selecione a Pessoa na lista:", font=("Segoe UI", 14, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Table(values=rows, headings=headers, max_col_width=50, auto_size_columns=True,
                    expand_x=True, expand_y=True, justification='center',
                    key="tabela_pessoas", enable_events=True, select_mode='browse')],
            [sg.HorizontalSeparator()],
            [sg.Button("Confirmar", size=(20, 1)), sg.Button("Cancelar", size=(20, 1))]
        ]

        window = sg.Window("Selecionar Pessoa", layout, size=(800, 400), element_justification="center")
        
        cpf_selecionado = None
        
        while True:
            event, values = window.read()
            
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                break

            if event == "Confirmar":
                selected_rows = values.get("tabela_pessoas")
                if selected_rows:
                    index = selected_rows[0]
                    cpf_selecionado = rows[index][0]
                    break
                else:
                    sg.popup("Por favor, clique em uma pessoa da lista antes de confirmar.")

        window.close()
        return cpf_selecionado

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Mensagem", font=("Segoe UI", 11))