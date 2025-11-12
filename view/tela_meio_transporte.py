import FreeSimpleGUI as sg

class TelaMeioTransporte:
    def __init__(self):
        sg.theme("DarkBlue14")

    def tela_opcoes(self):
        layout = [
            [sg.Text("-------- Meio de Transporte ----------", font=("Arial", 14, "bold"))],
            [sg.Button("1 - Incluir Meio de Transporte")],
            [sg.Button("2 - Alterar Meio de Transporte")],
            [sg.Button("3 - Listar Meios de Transporte")],
            [sg.Button("4 - Excluir Meio de Transporte")],
            [sg.Button("0 - Retornar ao Menu Principal")]
        ]

        janela = sg.Window("Menu - Meio de Transporte", layout)
        evento, _ = janela.read()
        janela.close()

        if evento in (sg.WIN_CLOSED, "0 - Retornar ao Menu Principal"):
            return 0
        elif evento == "1 - Incluir Meio de Transporte":
            return 1
        elif evento == "2 - Alterar Meio de Transporte":
            return 2
        elif evento == "3 - Listar Meios de Transporte":
            return 3
        elif evento == "4 - Excluir Meio de Transporte":
            return 4
        else:
            return -1

    def pega_dados_meio_transporte(self):
        layout = [
            [sg.Text("Cadastro de Meio de Transporte", font=("Arial", 14, "bold"))],
            [sg.Text("Tipo do meio de transporte:", size=(25, 1)), sg.Input(key="tipo")],
            [sg.Text("Capacidade:", size=(25, 1)), sg.Input(key="capacidade")],
            [sg.Text("Empresa responsável:", size=(25, 1)), sg.Input(key="empresa")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        janela = sg.Window("Cadastro - Meio de Transporte", layout)
        evento, valores = janela.read()
        janela.close()

        if evento == "Confirmar":
            try:
                capacidade = int(valores["capacidade"])
            except ValueError:
                sg.popup_error("A capacidade deve ser um número!")
                return None

            return {
                "tipo": valores["tipo"],
                "capacidade": capacidade,
                "empresa": valores["empresa"]
            }

        return None

    def mostra_meio(self, dados_meio_transporte):
        texto = (
            f"Tipo: {dados_meio_transporte['tipo']}\n"
            f"Capacidade: {dados_meio_transporte['capacidade']}\n"
            f"Empresa: {dados_meio_transporte['empresa']}"
        )
        sg.popup_scrolled(texto, title="Dados do Meio de Transporte", font=("Arial", 11))

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Mensagem")

    def seleciona_meio_transporte(self):
        layout = [
            [sg.Text("Digite o tipo do meio de transporte:")],
            [sg.Input(key="tipo")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        janela = sg.Window("Selecionar Meio de Transporte", layout)
        evento, valores = janela.read()
        janela.close()

        if evento == "Confirmar":
            return valores["tipo"]
        return None
