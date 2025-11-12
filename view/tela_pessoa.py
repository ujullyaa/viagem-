import FreeSimpleGUI as sg

class TelaPessoa:
    def __init__(self):
        sg.theme("DarkBlue14")

    def tela_opcoes(self):
        layout = [
            [sg.Text("===== MENU PESSOAS =====", font=("Arial", 14, "bold"))],
            [sg.Button("1 - Incluir Pessoa")],
            [sg.Button("2 - Alterar Pessoa")],
            [sg.Button("3 - Listar Pessoas")],
            [sg.Button("4 - Excluir Pessoa")],
            [sg.Button("0 - Retornar")]
        ]

        janela = sg.Window("Menu Pessoas", layout)
        evento, _ = janela.read()
        janela.close()

        if evento in (sg.WIN_CLOSED, "0 - Retornar"):
            return 0
        elif evento == "1 - Incluir Pessoa":
            return 1
        elif evento == "2 - Alterar Pessoa":
            return 2
        elif evento == "3 - Listar Pessoas":
            return 3
        elif evento == "4 - Excluir Pessoa":
            return 4
        return -1

    def pega_dados_pessoa(self):
        layout = [
            [sg.Text("Cadastro de Pessoa", font=("Arial", 14, "bold"))],
            [sg.Text("Nome:", size=(15, 1)), sg.Input(key="nome")],
            [sg.Text("Idade:", size=(15, 1)), sg.Input(key="idade")],
            [sg.Text("CPF:", size=(15, 1)), sg.Input(key="cpf")],
            [sg.Text("Telefone:", size=(15, 1)), sg.Input(key="telefone")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        janela = sg.Window("Nova Pessoa", layout)
        evento, valores = janela.read()
        janela.close()

        if evento == "Confirmar":
            try:
                idade = int(valores["idade"])
            except ValueError:
                sg.popup_error("❌ Idade inválida. Deve ser um número.")
                return None

            return {
                "nome": valores["nome"],
                "idade": idade,
                "cpf": valores["cpf"],
                "telefone": valores["telefone"]
            }

        return None

    def seleciona_pessoa(self):
        layout = [
            [sg.Text("Digite o CPF da pessoa:")],
            [sg.Input(key="cpf")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        janela = sg.Window("Selecionar Pessoa", layout)
        evento, valores = janela.read()
        janela.close()

        if evento == "Confirmar":
            return valores["cpf"]
        return None

    def mostra_pessoa(self, dados_pessoa: dict):
        texto = (
            f"Nome: {dados_pessoa['nome']}\n"
            f"Idade: {dados_pessoa['idade']}\n"
            f"CPF: {dados_pessoa['cpf']}\n"
            f"Telefone: {dados_pessoa['telefone']}"
        )
        sg.popup_scrolled(texto, title="📋 Dados da Pessoa", font=("Arial", 11))

    def mostra_mensagem(self, msg: str):
        sg.popup(msg, title="Mensagem", font=("Arial", 11))
