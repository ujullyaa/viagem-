import FreeSimpleGUI as sg

class TelaItinerario:
    def __init__(self):
        pass

    def tela_opcoes(self):
        layout = [
            [sg.Text("Menu Itinerário", font=("Helvetica", 15))],
            [sg.Button("Cadastrar Itinerário", key=1)],
            [sg.Button("Listar Itinerários", key=2)],
            [sg.Button("Excluir Itinerário", key=3)],
            [sg.Button("Voltar", key=0)]
        ]

        window = sg.Window("Menu Itinerário", layout)
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

    def pega_dados_itinerario(self):
        layout = [
            [sg.Text("Código:"), sg.InputText(key="codigo")],
            [sg.Text("Origem:"), sg.InputText(key="origem")],
            [sg.Text("Destino:"), sg.InputText(key="destino")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Cadastro de Itinerário", layout)
        event, values = window.read()
        window.close()

        if event == "Confirmar":
            return {
                "codigo": values["codigo"],
                "origem": values["origem"],
                "destino": values["destino"]
            }
        return None

    def mostra_itinerario(self, dados):
        sg.popup(
            f"Código: {dados['codigo']}\n"
            f"Origem: {dados['origem']}\n"
            f"Destino: {dados['destino']}",
            title="Itinerário"
        )

    def mostra_itinerarios(self, itinerarios):
        if not itinerarios:
            sg.popup("Nenhum itinerário cadastrado.")
            return
        texto = ""
        for i in itinerarios:
            texto += (
                f"Código: {i['codigo']}\n"
                f"Origem: {i['origem']}\n"
                f"Destino: {i['destino']}\n\n"
            )
        sg.popup_scrolled(texto, title="Itinerários Cadastrados")

    def seleciona_itinerario(self):
        layout = [
            [sg.Text("Digite o código do itinerário:")],
            [sg.InputText(key="codigo")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Selecionar Itinerário", layout)
        event, values = window.read()
        window.close()

        if event == "Confirmar":
            return values["codigo"]
        return None

    def mostra_mensagem(self, msg):
        sg.popup(msg)
