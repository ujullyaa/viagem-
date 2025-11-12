import FreeSimpleGUI as sg

class TelaViagem:
    def __init__(self):
        sg.theme("DarkBlue14")

    def tela_opcoes(self):
        layout = [
            [sg.Text("===== MENU VIAGENS =====", font=("Arial", 14, "bold"))],
            [sg.Button("1 - Incluir Viagem")],
            [sg.Button("2 - Listar Viagens")],
            [sg.Button("3 - Reservar Viagem")],
            [sg.Button("4 - Cancelar Viagem")],
            [sg.Button("5 - Atualizar Viagem")],
            [sg.Button("6 - Excluir Viagem")],
            [sg.Button("0 - Retornar")]
        ]

        janela = sg.Window("Menu Viagens", layout)
        evento, _ = janela.read()
        janela.close()

        if evento in (sg.WIN_CLOSED, "0 - Retornar"):
            return 0
        elif evento == "1 - Incluir Viagem":
            return 1
        elif evento == "2 - Listar Viagens":
            return 2
        elif evento == "3 - Reservar Viagem":
            return 3
        elif evento == "4 - Cancelar Viagem":
            return 4
        elif evento == "5 - Atualizar Viagem":
            return 5
        elif evento == "6 - Excluir Viagem":
            return 6
        return -1

    def pega_dados_viagem(self):
        layout = [
            [sg.Text("Cadastro de Viagem", font=("Arial", 14, "bold"))],
            [sg.Text("Código da Viagem:", size=(20, 1)), sg.Input(key="codigo")],
            [sg.Text("Data de Partida (DD/MM/AAAA):", size=(20, 1)), sg.Input(key="data_partida")],
            [sg.Text("Data de Chegada (DD/MM/AAAA):", size=(20, 1)), sg.Input(key="data_chegada")],
            [sg.Text("Itinerário:", size=(20, 1)), sg.Input(key="itinerario")],
            [sg.Text("Meio de Transporte:", size=(20, 1)), sg.Input(key="meio_transporte")],
            [sg.Text("Empresa de Transporte:", size=(20, 1)), sg.Input(key="empresa_transporte")],
            [sg.Text("Pagamento:", size=(20, 1)), sg.Input(key="pagamento")],
            [sg.Text("CPF do Responsável:", size=(20, 1)), sg.Input(key="pessoa")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        janela = sg.Window("Nova Viagem", layout)
        evento, valores = janela.read()
        janela.close()

        if evento == "Confirmar":
            try:
                codigo = int(valores["codigo"])
            except ValueError:
                sg.popup_error("❌ Código inválido! Deve ser um número.")
                return None

            return {
                "codigo": codigo,
                "data_partida": valores["data_partida"],
                "data_chegada": valores["data_chegada"],
                "itinerario": valores["itinerario"],
                "meio_transporte": valores["meio_transporte"],
                "empresa_transporte": valores["empresa_transporte"],
                "pagamento": valores["pagamento"],
                "pessoa": valores["pessoa"]
            }
        return None

    def mostra_viagem(self, dados_viagem: dict):
        texto = (
            f"Código: {dados_viagem['codigo']}\n"
            f"Data Partida: {dados_viagem['data_partida']}\n"
            f"Data Chegada: {dados_viagem['data_chegada']}\n"
            f"Itinerário: {dados_viagem['itinerario']}\n"
            f"Meio de Transporte: {dados_viagem['meio_transporte']}\n"
            f"Empresa de Transporte: {dados_viagem['empresa_transporte']}\n"
            f"Pagamento: {dados_viagem['pagamento']}\n"
            f"Pessoa: {dados_viagem['pessoa']}"
        )
        sg.popup_scrolled(texto, title="📋 Dados da Viagem", font=("Arial", 11))

    def seleciona_viagem(self):
        layout = [
            [sg.Text("Digite o código da viagem:")],
            [sg.Input(key="codigo")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        janela = sg.Window("Selecionar Viagem", layout)
        evento, valores = janela.read()
        janela.close()

        if evento == "Confirmar":
            try:
                return int(valores["codigo"])
            except ValueError:
                sg.popup_error("❌ Código inválido! Deve ser um número.")
                return None
        return None

    def mostra_mensagem(self, msg: str):
        sg.popup(msg, title="Mensagem", font=("Arial", 11))
