import FreeSimpleGUI as sg

class TelaControladores:
    def tela_opcoes(self):
        sg.theme("DarkBlue3")

        layout = [
            [sg.Text("SISTEMA DE GERENCIAMENTO DE VIAGENS", font=("Helvetica", 16), justification="center")],
            [sg.HorizontalSeparator()],
            [sg.Button("1 - Empresa de Transporte", size=(30, 1))],
            [sg.Button("2 - Itinerário", size=(30, 1))],
            [sg.Button("3 - Meio de Transporte", size=(30, 1))],
            [sg.Button("4 - Passagem", size=(30, 1))],
            [sg.Button("5 - Pessoa", size=(30, 1))],
            [sg.Button("6 - Viagem", size=(30, 1))],
            [sg.Button("7 - Pagamento", size=(30, 1))],
            [sg.HorizontalSeparator()],
            [sg.Button("0 - Sair do Sistema", button_color=("white", "firebrick3"), size=(30, 1))]
        ]

        window = sg.Window("Menu Principal", layout, element_justification="center")

        while True:
            event, _ = window.read()

            if event in (sg.WINDOW_CLOSED, "0 - Sair do Sistema"):
                window.close()
                return 0

            for i in range(1, 8):
                if event.startswith(f"{i} -"):
                    window.close()
                    return i
