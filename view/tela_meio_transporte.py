# view/tela_meio_transporte.py
import FreeSimpleGUI as sg

class TelaMeioTransporte:
    def __init__(self):
        pass

    def tela_opcoes(self):
        layout = [
            [sg.Text("Menu Meio de Transporte", font=("Helvetica", 15))],
            [sg.Button("Cadastrar Meio de Transporte", key=1)],
            [sg.Button("Alterar Meio de Transporte", key=2)],
            [sg.Button("Listar Meios de Transporte", key=3)],
            [sg.Button("Excluir Meio de Transporte", key=4)],
            [sg.Button("Voltar", key=0)]
        ]

        window = sg.Window("Menu Meio de Transporte", layout)
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

    def pega_dados_meio_transporte(self):
        layout = [
            [sg.Text("Tipo:"), sg.InputText(key="tipo")],
            [sg.Text("Capacidade:"), sg.InputText(key="capacidade")],
            [sg.Text("Placa:"), sg.InputText(key="placa")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Cadastro de Meio de Transporte", layout)
        event, values = window.read()
        window.close()

        if event == "Confirmar":
            return {
                "tipo": values["tipo"],
                "capacidade": values["capacidade"],
                "placa": values["placa"]
            }
        return None

    def mostra_meio_transporte(self, dados):
        sg.popup(
            f"Tipo: {dados['tipo']}\n"
            f"Capacidade: {dados['capacidade']}\n"
            f"Placa: {dados['placa']}",
            title="Meio de Transporte"
        )

    def mostra_meios_transporte(self, meios):
        if not meios:
            sg.popup("Nenhum meio de transporte cadastrado.")
            return
        texto = ""
        for m in meios:
            texto += (
                f"Tipo: {m['tipo']}\n"
                f"Capacidade: {m['capacidade']}\n"
                f"Placa: {m['placa']}\n\n"
            )
        sg.popup_scrolled(texto, title="Meios de Transporte Cadastrados")

    def seleciona_meio_transporte(self):
        layout = [
            [sg.Text("Digite a placa do meio de transporte:")],
            [sg.InputText(key="placa")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Selecionar Meio de Transporte", layout)
        event, values = window.read()
        window.close()

        if event == "Confirmar":
            return values["placa"]
        return None

    def mostra_mensagem(self, msg):
        sg.popup(msg)
