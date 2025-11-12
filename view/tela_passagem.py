import FreeSimpleGUI as sg

class TelaPassagem:
    def __init__(self):
        sg.theme("DarkBlue14")

    def tela_opcoes(self):
        layout = [
            [sg.Text("===== MENU PASSAGENS =====", font=("Arial", 14, "bold"))],
            [sg.Button("1 - Incluir Passagem")],
            [sg.Button("2 - Alterar Passagem")],
            [sg.Button("3 - Listar Passagens")],
            [sg.Button("4 - Excluir Passagem")],
            [sg.Button("0 - Retornar ao menu anterior")]
        ]

        janela = sg.Window("Menu Passagens", layout)
        evento, _ = janela.read()
        janela.close()

        if evento in (sg.WIN_CLOSED, "0 - Retornar ao menu anterior"):
            return 0
        elif evento == "1 - Incluir Passagem":
            return 1
        elif evento == "2 - Alterar Passagem":
            return 2
        elif evento == "3 - Listar Passagens":
            return 3
        elif evento == "4 - Excluir Passagem":
            return 4
        return -1

    def pega_dados_passagem(self):
        layout = [
            [sg.Text("Cadastro de Passagem", font=("Arial", 14, "bold"))],
            [sg.Text("Número da Passagem:", size=(22, 1)), sg.Input(key="numero")],
            [sg.Text("Assento:", size=(22, 1)), sg.Input(key="assento")],
            [sg.Text("Data da Viagem (DD/MM/AAAA):", size=(22, 1)), sg.Input(key="data_viagem")],
            [sg.Text("Valor da Passagem (R$):", size=(22, 1)), sg.Input(key="valor")],
            [sg.Text("Nome do Passageiro:", size=(22, 1)), sg.Input(key="pessoa")],
            [sg.Text("Forma de Pagamento:", size=(22, 1)),
             sg.Combo(["Cartão", "Dinheiro", "Pix"], key="pagamento", readonly=True)],
            [sg.Text("Meio de Transporte:", size=(22, 1)),
             sg.Combo(["Ônibus", "Avião", "Navio"], key="meio_transporte", readonly=True)],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        janela = sg.Window("Nova Passagem", layout)
        evento, valores = janela.read()
        janela.close()

        if evento == "Confirmar":
            try:
                numero = int(valores["numero"])
                valor = float(valores["valor"])
            except ValueError:
                sg.popup_error("❌ Número ou valor inválido!")
                return None

            return {
                "numero": numero,
                "assento": valores["assento"],
                "data_viagem": valores["data_viagem"],
                "valor": valor,
                "pessoa": valores["pessoa"],
                "pagamento": valores["pagamento"],
                "meio_transporte": valores["meio_transporte"]
            }

        return None

    def mostra_passagem(self, dados_passagem):
        texto = (
            f"Número: {dados_passagem['numero']}\n"
            f"Assento: {dados_passagem['assento']}\n"
            f"Data da Viagem: {dados_passagem['data_viagem']}\n"
            f"Valor: R$ {dados_passagem['valor']:.2f}\n"
            f"Passageiro: {dados_passagem['pessoa']}\n"
            f"Pagamento: {dados_passagem['pagamento']}\n"
            f"Meio de Transporte: {dados_passagem['meio_transporte']}"
        )
        sg.popup_scrolled(texto, title="🧾 Detalhes da Passagem", font=("Arial", 11))

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Mensagem", font=("Arial", 11))

    def seleciona_passagem(self):
        layout = [
            [sg.Text("Digite o número da passagem:")],
            [sg.Input(key="numero")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        janela = sg.Window("Selecionar Passagem", layout)
        evento, valores = janela.read()
        janela.close()

        if evento == "Confirmar":
            try:
                return int(valores["numero"])
            except ValueError:
                sg.popup_error("❌ O número deve ser um valor inteiro!")
        return None
