# view/tela_passagem.py
import FreeSimpleGUI as sg

class TelaPassagem:
    def tela_opcoes(self):
        layout = [
            [sg.Text("🎫  Menu de Passagens", font=("Segoe UI", 18, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Button("1 - Incluir Passagem")],
            [sg.Button("2 - Alterar Passagem")],
            [sg.Button("3 - Listar Passagens")],
            [sg.Button("4 - Excluir Passagem")],
            [sg.Button("0 - Voltar ao Menu Principal", button_color=("white", "red"))]
        ]

        window = sg.Window("Menu Passagens", layout)
        event, _ = window.read()
        window.close()

        if event in (sg.WINDOW_CLOSED, "0 - Voltar ao Menu Principal"):
            return 0
        elif event == "1 - Incluir Passagem":
            return 1
        elif event == "2 - Alterar Passagem":
            return 2
        elif event == "3 - Listar Passagens":
            return 3
        elif event == "4 - Excluir Passagem":
            return 4
        return -1

    def pega_dados_passagem(self):
        layout = [
            [sg.Text("🎫  Cadastro de Passagem", font=("Segoe UI", 18, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("Número da Passagem:"), sg.Input(key="numero")],
            [sg.Text("Assento:"), sg.Input(key="assento")],
            [sg.Text("Data da Viagem (dd/mm/aaaa):"), sg.Input(key="data_viagem")],
            [sg.Text("Valor (R$):"), sg.Input(key="valor")],
            [sg.Text("Código da Pessoa:"), sg.Input(key="pessoa")],
            [sg.Text("Código do Meio de Transporte:"), sg.Input(key="meio_transporte")],
            [sg.HorizontalSeparator()],
            [
                sg.Button("💾  Confirmar", key="confirmar", button_color=("white", "green")),
                sg.Button("↩️  Cancelar", key="cancelar", button_color=("white", "gray"))
            ]
        ]

        window = sg.Window("Cadastro de Passagem", layout)
        event, values = window.read()
        window.close()

        if event == "confirmar":
            return {
                "numero": values.get("numero", "").strip(),
                "assento": values.get("assento", "").strip(),
                "data_viagem": values.get("data_viagem", "").strip(),
                "valor": values.get("valor", "").strip(),
                "pessoa": values.get("pessoa", "").strip(),
                "meio_transporte": values.get("meio_transporte", "").strip()
            }
        return None

    def mostra_passagem(self, dados):
        texto = (
            f"🎫 Número: {dados.get('numero', '')}\n"
            f"💺 Assento: {dados.get('assento', '')}\n"
            f"📅 Data da Viagem: {dados.get('data_viagem', '')}\n"
            f"💰 Valor: {dados.get('valor', '')}\n"
            f"🧑 Pessoa: {dados.get('pessoa', '')}\n"
            f"🚌 Meio de Transporte: {dados.get('meio_transporte', '')}"
        )
        sg.popup_scrolled(texto, title="📋 Passagem", font=("Segoe UI", 11))

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Mensagem", font=("Segoe UI", 11))

    def seleciona_passagem(self):
        layout = [
            [sg.Text("Digite o número da passagem:")],
            [sg.Input(key="numero")],
            [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]
        ]
        window = sg.Window("Selecionar Passagem", layout)
        event, values = window.read()
        window.close()

        if event == "confirmar":
            return values.get("numero", "").strip()
        return None
