import FreeSimpleGUI as sg

class TelaViagem:
    def __init__(self):
        pass

    def tela_opcoes(self):
        layout = [
            [sg.Text("Menu Viagem", font=("Helvetica", 15))],
            [sg.Button("Cadastrar Viagem", key=1)],
            [sg.Button("Listar Viagens", key=2)],
            [sg.Button("Excluir Viagem", key=3)],
            [sg.Button("Voltar", key=0)]
        ]

        window = sg.Window("Menu Viagem", layout)
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

    def pega_dados_viagem(self):
        layout = [
            [sg.Text("Código da Viagem:"), sg.InputText(key="codigo")],
            [sg.Text("Destino:"), sg.InputText(key="destino")],
            [sg.Text("Data:"), sg.InputText(key="data")],
            [sg.Text("Horário:"), sg.InputText(key="horario")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Cadastro de Viagem", layout)
        event, values = window.read()
        window.close()

        if event == "Confirmar":
            return {
                "codigo": values["codigo"],
                "destino": values["destino"],
                "data": values["data"],
                "horario": values["horario"]
            }
        return None

    def mostra_viagem(self, dados):
        sg.popup(
            f"Código: {dados['codigo']}\n"
            f"Destino: {dados['destino']}\n"
            f"Data: {dados['data']}\n"
            f"Horário: {dados['horario']}",
            title="Viagem"
        )

    def mostra_viagens(self, viagens):
        if not viagens:
            sg.popup("Nenhuma viagem cadastrada.")
            return
        texto = ""
        for v in viagens:
            texto += (
                f"Código: {v['codigo']}\n"
                f"Destino: {v['destino']}\n"
                f"Data: {v['data']}\n"
                f"Horário: {v['horario']}\n\n"
            )
        sg.popup_scrolled(texto, title="Viagens Cadastradas")

    def seleciona_viagem(self):
        layout = [
            [sg.Text("Digite o código da viagem:")],
            [sg.InputText(key="codigo")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Selecionar Viagem", layout)
        event, values = window.read()
        window.close()

        if event == "Confirmar":
            return values["codigo"]
        return None

    def mostra_mensagem(self, msg):
        sg.popup(msg)
