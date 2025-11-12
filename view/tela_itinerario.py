import FreeSimpleGUI as sg

class TelaItinerario:
    def __init__(self):
        sg.theme("DarkBlue14")

    def tela_opcoes(self):
        layout = [
            [sg.Text("===== MENU ITINERÁRIOS =====", font=("Arial", 14, "bold"))],
            [sg.Button("1 - Incluir Itinerário")],
            [sg.Button("2 - Alterar Itinerário")],
            [sg.Button("3 - Listar Itinerários")],
            [sg.Button("4 - Excluir Itinerário")],
            [sg.Button("0 - Retornar ao menu anterior")],
        ]

        janela = sg.Window("Menu Itinerários", layout)
        evento, _ = janela.read()
        janela.close()

        if evento in (None, "0 - Retornar ao menu anterior"):
            return 0
        elif evento == "1 - Incluir Itinerário":
            return 1
        elif evento == "2 - Alterar Itinerário":
            return 2
        elif evento == "3 - Listar Itinerários":
            return 3
        elif evento == "4 - Excluir Itinerário":
            return 4
        else:
            return -1

    def pega_dados_itinerario(self):
        layout = [
            [sg.Text("Cadastro de Itinerário", font=("Arial", 14, "bold"))],
            [sg.Text("Código do Itinerário:", size=(20, 1)), sg.Input(key="codigo_itinerario")],
            [sg.Text("Origem:", size=(20, 1)), sg.Input(key="origem")],
            [sg.Text("Destino:", size=(20, 1)), sg.Input(key="destino")],
            [sg.Text("Data de Início (dd/mm/aaaa):", size=(20, 1)), sg.Input(key="data_inicio")],
            [sg.Text("Data de Fim (dd/mm/aaaa):", size=(20, 1)), sg.Input(key="data_fim")],
            [sg.Frame("Adicionar Passagens", [
                [sg.Button("➕ Adicionar Passagem"), sg.Button("✅ Confirmar"), sg.Button("❌ Cancelar")],
                [sg.Listbox(values=[], size=(45, 5), key="passagens", enable_events=True)]
            ])]
        ]

        janela = sg.Window("Cadastro de Itinerário", layout)

        passagens = []
        while True:
            evento, valores = janela.read()

            if evento in (sg.WIN_CLOSED, "❌ Cancelar"):
                janela.close()
                return None

            elif evento == "➕ Adicionar Passagem":
                nova_passagem = self.pega_dados_passagem()
                if nova_passagem:
                    passagens.append(nova_passagem)
                    janela["passagens"].update(values=[f"Código {p['codigo_passagem']} - {p['nome_passageiro']}" for p in passagens])

            elif evento == "✅ Confirmar":
                try:
                    codigo = int(valores["codigo_itinerario"])
                except ValueError:
                    sg.popup_error("O código deve ser numérico!")
                    continue

                janela.close()
                return {
                    "codigo_itinerario": codigo,
                    "origem": valores["origem"],
                    "destino": valores["destino"],
                    "data_inicio": valores["data_inicio"],
                    "data_fim": valores["data_fim"],
                    "passagem": passagens
                }

    def pega_dados_passagem(self):
        layout = [
            [sg.Text("Cadastro de Passagem", font=("Arial", 13, "bold"))],
            [sg.Text("Código da Passagem:"), sg.Input(key="codigo_passagem")],
            [sg.Text("Nome do Passageiro:"), sg.Input(key="nome_passageiro")],
            [sg.Text("Data da Passagem (dd/mm/aaaa):"), sg.Input(key="data_passagem")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        janela = sg.Window("Adicionar Passagem", layout)
        evento, valores = janela.read()
        janela.close()

        if evento == "Confirmar":
            try:
                codigo = int(valores["codigo_passagem"])
            except ValueError:
                sg.popup_error("O código da passagem deve ser numérico!")
                return None

            return {
                "codigo_passagem": codigo,
                "nome_passageiro": valores["nome_passageiro"],
                "data_passagem": valores["data_passagem"]
            }

        return None

    def seleciona_itinerario(self):
        layout = [
            [sg.Text("Digite o código do Itinerário:")],
            [sg.Input(key="codigo")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        janela = sg.Window("Selecionar Itinerário", layout)
        evento, valores = janela.read()
        janela.close()

        if evento == "Confirmar":
            try:
                return int(valores["codigo"])
            except ValueError:
                sg.popup_error("O código deve ser numérico!")
        return None

    def mostra_itinerario(self, dados_itinerario: dict):
        texto_passagens = "\n".join(
            [f"- Código: {p['codigo_passagem']}, Passageiro: {p['nome_passageiro']}, Data: {p['data_passagem']}"
             for p in dados_itinerario.get("passagem", [])]
        ) or "Nenhuma passagem cadastrada."

        sg.popup_scrolled(
            f"🧾 Itinerário\n\n"
            f"Código: {dados_itinerario['codigo_itinerario']}\n"
            f"Origem: {dados_itinerario['origem']}\n"
            f"Destino: {dados_itinerario['destino']}\n"
            f"Data de Início: {dados_itinerario['data_inicio']}\n"
            f"Data de Fim: {dados_itinerario['data_fim']}\n\n"
            f"Passagens:\n{texto_passagens}",
            title="Detalhes do Itinerário",
            font=("Arial", 11)
        )

    def mostra_mensagem(self, msg: str):
        sg.popup(msg, title="Mensagem")
