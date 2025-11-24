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
        
        # --- CORREÇÃO PYLANCE ---
        # Lemos para uma variável 'resultado' primeiro
        resultado = window.read()
        window.close()

        # Se resultado for None (janela fechada com erro), definimos valores padrão
        if resultado is None:
            event = sg.WINDOW_CLOSED
        else:
            # Se deu certo, pegamos o evento (índice 0 da tupla)
            event = resultado[0]
        
        if event in (sg.WINDOW_CLOSED, "0 - Voltar ao Menu Principal"): return 0
        if event == "1 - Cadastrar Pessoa": return 1
        if event == "2 - Alterar Pessoa": return 2
        if event == "3 - Listar Pessoas": return 3
        if event == "4 - Excluir Pessoa": return 4
        return 0

    def pega_dados_pessoa(self, pessoa_existente=None):
        # Valores Padrão
        nome_val = pessoa_existente.nome if pessoa_existente else ""
        cpf_val = pessoa_existente.cpf if pessoa_existente else ""
        idade_val = pessoa_existente.idade if pessoa_existente else ""
        ddd_val = ""
        num_val = ""

        if pessoa_existente:
            tel_completo = str(pessoa_existente.telefone)
            tel_limpo = ''.join(filter(str.isdigit, tel_completo))
            if len(tel_limpo) >= 2:
                ddd_val = tel_limpo[:2]
                num_val = tel_limpo[2:]
            else:
                num_val = tel_limpo

        layout = [
            [sg.Text("👤 Cadastro de Pessoa", font=("Segoe UI", 18, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("Nome:", size=(15, 1)), sg.InputText(key="nome", default_text=nome_val, size=(40, 1))],
            [sg.Text("Idade:", size=(15, 1)), sg.InputText(key="idade", default_text=idade_val, size=(40, 1))],
            [sg.Text("CPF:", size=(15, 1)), sg.InputText(key="cpf", default_text=cpf_val, disabled=(pessoa_existente is not None), size=(40, 1))],
            
            # Campos de Telefone
            [
                sg.Text("Telefone:", size=(15, 1)), 
                sg.Text("DDD", size=(4,1), justification='right'), 
                sg.InputText(key="ddd", default_text=ddd_val, size=(5, 1)), 
                sg.Text("Número", size=(6,1), justification='right'), 
                sg.InputText(key="numero", default_text=num_val, size=(22, 1))
            ],
            [sg.Text("Ex: 48 e 99999-9999", font=("Segoe UI", 8), text_color="gray", pad=((140,0),(0,0)))],

            [sg.HorizontalSeparator()],
            [sg.Button("💾 Confirmar", size=(20, 1)), sg.Button("↩️ Cancelar", size=(20, 1))]
        ]

        window = sg.Window("Dados da Pessoa", layout, element_justification="center")
        
        # Lê a janela e guarda em 'resultado'
        resultado = window.read()
        window.close()

        # --- A CORREÇÃO ESTÁ AQUI EMBAIXO ---
        # Antes estava escrito 'result is None', agora corrigi para 'resultado is None'
        if resultado is None:
            event = sg.WINDOW_CLOSED
            values = None
        else:
            event, values = resultado # Desempacota a variável correta

        # Só processa se clicou em Confirmar E values existe
        if event == "💾 Confirmar" and values is not None:
            ddd_limpo = ''.join(filter(str.isdigit, values['ddd']))
            numero_limpo = ''.join(filter(str.isdigit, values['numero']))
            
            if ddd_limpo and numero_limpo.startswith(ddd_limpo) and len(numero_limpo) >= 10:
                numero_limpo = numero_limpo[len(ddd_limpo):]

            telefone_completo = ddd_limpo + numero_limpo

            return {
                "nome": values["nome"],
                "idade": values["idade"],
                "cpf": values["cpf"],
                "telefone": telefone_completo
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
            # --- CORREÇÃO PYLANCE ---
            resultado = window.read()
            
            if resultado is None: # Se fechou a janela pelo X
                break
                
            event, values = resultado # Seguro agora

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