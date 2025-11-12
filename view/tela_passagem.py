import FreeSimpleGUI as sg

class TelaPassagem:
    def __init__(self):
        pass

    def tela_opcoes(self):
        layout = [
            [sg.Text("Menu de Passagens", font=("Helvetica", 15))],
            [sg.Button("Incluir Passagem", key=1)],
            [sg.Button("Alterar Passagem", key=2)],
            [sg.Button("Listar Passagens", key=3)],
            [sg.Button("Excluir Passagem", key=4)],
            [sg.Button("Voltar ao Menu Principal", key=0)]
        ]

        window = sg.Window("Menu Passagens", layout)
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
        elif event == 4:
            return 4
        return 0

    def pega_dados_passagem(self):
        layout = [
            [sg.Text("Código da Passagem:"), sg.Input(key="codigo")],
            [sg.Text("Origem:"), sg.Input(key="origem")],
            [sg.Text("Destino:"), sg.Input(key="destino")],
            [sg.Text("Data da Viagem:"), sg.Input(key="data")],
            [sg.Text("Preço (R$):"), sg.Input(key="preco")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Cadastro de Passagem", layout)
        event, values = window.read()
        window.close()

        if event == "Confirmar":
            return {
                "codigo": values["codigo"],
                "origem": values["origem"],
                "destino": values["destino"],
                "data": values["data"],
                "preco": values["preco"]
            }
        return None

    def mostra_passagem(self, dados):
        sg.popup(
            f"Código: {dados['codigo']}\n"
            f"Origem: {dados['origem']}\n"
            f"Destino: {dados['destino']}\n"
            f"Data: {dados['data']}\n"
            f"Preço: R$ {dados['preco']}",
            title="Passagem"
        )

    def mostra_passagens(self, passagens):
        if not passagens:
            sg.popup("Nenhuma passagem cadastrada.")
            return
        texto = ""
        for p in passagens:
            texto += (
                f"Código: {p['codigo']}\n"
                f"Origem: {p['origem']}\n"
                f"Destino: {p['destino']}\n"
                f"Data: {p['data']}\n"
                f"Preço: R$ {p['preco']}\n\n"
            )
        sg.popup_scrolled(texto, title="Passagens Cadastradas")

    def seleciona_passagem(self):
        layout = [
            [sg.Text("Digite o código da passagem:")],
            [sg.Input(key="codigo")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Passagem", layout)
        event, values = window.read()
        window.close()

        if event == "Confirmar":
            return values["codigo"]
        return None

    def mostra_mensagem(self, msg):
        sg.popup(msg)
