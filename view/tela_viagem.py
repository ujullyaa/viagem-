import FreeSimpleGUI as sg

class TelaViagem:
    def __init__(self):
        sg.theme("DarkBlue3")

    def tela_opcoes(self):
        layout = [
            [sg.Column(
                [
                    [sg.Text("✈️ Menu Viagem", font=("Segoe UI", 18, "bold"))],
                    [sg.HorizontalSeparator()],
                    [sg.Button("1 - Cadastrar Viagem", size=(35, 1))],
                    [sg.Button("2 - Listar Viagens", size=(35, 1))],
                    [sg.Button("3 - Reservar Viagem", size=(35, 1))],
                    [sg.Button("4 - Cancelar Viagem", size=(35, 1))],
                    [sg.Button("5 - Atualizar Status", size=(35, 1))],
                    [sg.Button("6 - Excluir Viagem", size=(35, 1))],
                    [sg.HorizontalSeparator()],
                    [sg.Button("0 - Voltar ao Menu Principal", button_color=("white", "red"), size=(35, 1))]
                ],
                element_justification="center",
                expand_x=True
            )]
        ]

        window = sg.Window("Menu Viagem", layout, element_justification="center", size=(600, 600))
        event, _ = window.read()
        window.close()

        if event in (sg.WINDOW_CLOSED, "0 - Voltar ao Menu Principal"): return 0
        # Mapeamento simples de string para int
        opcoes = {
            "1 - Cadastrar Viagem": 1, "2 - Listar Viagens": 2, "3 - Reservar Viagem": 3,
            "4 - Cancelar Viagem": 4, "5 - Atualizar Status": 5, "6 - Excluir Viagem": 6
        }
        return opcoes.get(event, 0)

    def pega_dados_viagem(self):
        layout = [
            [sg.Text("✈️ Cadastro de Viagem", font=("Segoe UI", 14, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("Código:", size=(15,1)), sg.Input(key="codigo", size=(45,1))],
            [sg.Text("CPF Pessoa:", size=(15,1)), sg.Input(key="pessoa", size=(45,1))],
            [sg.Text("Partida:", size=(15,1)), sg.Input(key="data_partida", size=(45,1))],
            [sg.Text("Chegada:", size=(15,1)), sg.Input(key="data_chegada", size=(45,1))],
            # Adicione mais campos se necessário (meio, empresa, etc)
            # Para simplificar a UI, assumimos que o controlador trata o resto ou pedimos aqui
            [sg.HorizontalSeparator()],
            [sg.Button("💾 Confirmar", key="confirmar", size=(20,1)), sg.Button("↩️ Cancelar", key="cancelar", size=(20,1))]
        ]

        window = sg.Window("Dados Viagem", layout, element_justification="center")
        event, values = window.read()
        window.close()

        if event == "confirmar":
            return {
                "codigo": values["codigo"],
                "pessoa": values["pessoa"],
                "data_partida": values["data_partida"],
                "data_chegada": values["data_chegada"],
                # Os campos complexos (objetos) idealmente são selecionados via ID ou listas separadas
                # Aqui retornamos o básico para o controlador buscar
                "itinerario": None, "meio_transporte": None, "empresa_transporte": None, "pagamento": None
            }
        return None

    def mostra_viagens(self, viagens_lista):
        # viagens_lista deve ser lista de dicts: [{'codigo':..., 'destino':...}]
        if not viagens_lista:
            sg.popup("Nenhuma viagem cadastrada.", title="Aviso")
            return

        headers = ["Código", "Destino", "Data"]
        rows = [[v['codigo'], v['destino'], v['data']] for v in viagens_lista]

        layout = [
            [sg.Text("📋 Viagens Cadastradas", font=("Segoe UI", 14, "bold"))],
            [sg.Table(values=rows, headings=headers, max_col_width=50, auto_size_columns=True,
                    justification='center', key="tab", expand_x=True, expand_y=True)],
            [sg.Button("Voltar", size=(20,1))]
        ]
        window = sg.Window("Lista", layout, size=(800, 400), element_justification="center")
        window.read()
        window.close()

    def seleciona_viagem(self):
        layout = [
            [sg.Text("Digite o código da viagem:", font=("Segoe UI", 12))],
            [sg.Input(key="codigo", size=(45,1))],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Seleção", layout, element_justification="center")
        event, values = window.read()
        window.close()

        if event == "Confirmar":
            return values["codigo"]
        return None

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Mensagem", font=("Segoe UI", 11))