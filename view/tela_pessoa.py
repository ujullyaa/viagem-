import FreeSimpleGUI as sg

class TelaPessoa:
    def __init__(self):
        pass

    def tela_opcoes(self):
        layout = [
            [sg.Text("Menu Pessoa", font=("Helvetica", 15))],
            [sg.Button("Cadastrar Pessoa", key=1)],
            [sg.Button("Listar Pessoas", key=2)],
            [sg.Button("Excluir Pessoa", key=3)],
            [sg.Button("Voltar", key=0)]
        ]

        window = sg.Window("Menu Pessoa", layout)
        event, _ = window.read()
        window.close()

        if event in (sg.WINDOW_CLOSED, 0):
            return 0
        elif event == 1:
            return 1
        elif event == 2:
            return 2
        elif event == 3:
            return 3
        return 0

    def pega_dados_pessoa(self):
        layout = [
            [sg.Text("Nome:"), sg.InputText(key="nome")],
            [sg.Text("CPF:"), sg.InputText(key="cpf")],
            [sg.Text("Telefone:"), sg.InputText(key="telefone")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Cadastro de Pessoa", layout)
        event, values = window.read()
        window.close()

        if event == "Confirmar":
            return {
                "nome": values["nome"],
                "cpf": values["cpf"],
                "telefone": values["telefone"]
            }
        return None

    def mostra_pessoa(self, dados):
        sg.popup(
            f"Nome: {dados['nome']}\n"
            f"CPF: {dados['cpf']}\n"
            f"Telefone: {dados['telefone']}",
            title="Pessoa"
        )

    def mostra_pessoas(self, pessoas):
        if not pessoas:
            sg.popup("Nenhuma pessoa cadastrada.")
            return
        texto = ""
        for p in pessoas:
            texto += (
                f"Nome: {p['nome']}\n"
                f"CPF: {p['cpf']}\n"
                f"Telefone: {p['telefone']}\n\n"
            )
        sg.popup_scrolled(texto, title="Pessoas Cadastradas")

    def seleciona_pessoa(self):
        layout = [
            [sg.Text("Digite o CPF da pessoa:")],
            [sg.InputText(key="cpf")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Selecionar Pessoa", layout)
        event, values = window.read()
        window.close()

        if event == "Confirmar":
            return values["cpf"]
        return None

    def mostra_mensagem(self, msg):
        sg.popup(msg)
