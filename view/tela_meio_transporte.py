# view/tela_meio_transporte.py
import FreeSimpleGUI as sg

class TelaMeioTransporte:
    def __init__(self):
        sg.theme("LightGray1")
        # tipos fixos conforme solicitado (observação: 'Onibus' sem acento se preferir)
        self._tipos_fixos = ["Onibus", "Carro", "Avião"]

    def tela_opcoes(self):
        layout = [
            [sg.Text("🚍 Menu Meio de Transporte", font=("Segoe UI", 18, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Button("1 - Incluir Meio de Transporte", size=(30,1))],
            [sg.Button("2 - Alterar Meio de Transporte", size=(30,1))],
            [sg.Button("3 - Listar Meios de Transporte", size=(30,1))],
            [sg.Button("4 - Excluir Meio de Transporte", size=(30,1))],
            [sg.HorizontalSeparator()],
            [sg.Button("0 - Retornar", size=(30,1))],
        ]
        window = sg.Window("Meios de Transporte", layout, element_justification="center")
        event, values = window.read()
        window.close()

        if event is None:
            return 0
        if event.startswith("1"):
            return 1
        if event.startswith("2"):
            return 2
        if event.startswith("3"):
            return 3
        if event.startswith("4"):
            return 4
        if event.startswith("0"):
            return 0
        # fallback
        return 0

    def mostra_mensagem(self, msg):
        sg.popup(msg)

    # -------------------------------------------------
    # seleciona_meio_transporte: se receber 'meios' (iterável)
    # exibe uma lista dos tipos já cadastrados para seleção (usar em alterar/excluir)
    # se não receber 'meios', exibe combo com os TIPOS FIXOS (Onibus, Carro, Avião)
    # -------------------------------------------------
    def seleciona_meio_transporte(self, meios=None):
        if meios:
            # constroi lista de strings amigáveis a partir dos objetos meios
            opcoes = []
            for m in meios:
                tipo = getattr(m, "tipo", None)
                capacidade = getattr(m, "capacidade", "")
                empresa = getattr(m, "empresa", "")
                # tenta obter nome da empresa se possível
                nome_empresa = getattr(empresa, "nome", str(empresa)) if empresa is not None else ""
                opcoes.append(f"{tipo} — Capacidade: {capacidade} — Empresa: {nome_empresa}")

            layout = [
                [sg.Text("Selecione o meio de transporte:", font=("Segoe UI", 12))],
                [sg.Combo(opcoes, size=(60, 1), key="-MEIO-")],
                [sg.Button("OK"), sg.Button("Cancelar")]
            ]
            window = sg.Window("Selecionar Meio", layout, element_justification="center")
            event, values = window.read()
            window.close()

            if event != "OK":
                return None

            selecionado = values.get("-MEIO-")
            if not selecionado:
                return None

            # extrai o tipo da string montada (antes do ' — ')
            tipo = selecionado.split("—")[0].strip()
            return tipo

        else:
            # mostra lista fixa de tipos (inclusão)
            layout = [
                [sg.Text("Selecione o tipo do meio de transporte:", font=("Segoe UI", 12))],
                [sg.Combo(self._tipos_fixos, size=(40, 1), key="-TIPO-")],
                [sg.Button("OK"), sg.Button("Cancelar")]
            ]
            window = sg.Window("Tipo do Meio", layout, element_justification="center")
            event, values = window.read()
            window.close()

            if event != "OK":
                return None

            tipo = values.get("-TIPO-")
            return tipo

    # -------------------------------------------------
    # pega_dados_meio_transporte: pede capacidade e (opcional) altera tipo
    # se for passada uma instância 'meio', pré-preenche valores e permite
    # alterar tipo e capacidade
    # -------------------------------------------------
    def pega_dados_meio_transporte(self, meio=None):
        tipo_inicial = getattr(meio, "tipo", "")
        capacidade_inicial = getattr(meio, "capacidade", "")

        # para consistência visual, tipo também é um Combo com os fixos
        layout = [
            [sg.Text("Tipo:", size=(12,1)), sg.Combo(self._tipos_fixos, default_value=tipo_inicial, size=(40,1), key="-TIPO-")],
            [sg.Text("Capacidade:", size=(12,1)), sg.Input(str(capacidade_inicial), size=(40,1), key="-CAP-")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Dados do Meio de Transporte", layout, element_justification="left")
        event, values = window.read()
        window.close()

        if event != "OK":
            return None

        tipo = values.get("-TIPO-")
        capacidade = values.get("-CAP-")
        if tipo is None or capacidade is None:
            return None

        return {"tipo": tipo, "capacidade": capacidade}

    # -------------------------------------------------
    # seleciona_empresa: recebe lista de objetos empresa e retorna a empresa selecionada
    # -------------------------------------------------
    def seleciona_empresa(self, empresas):
        # tenta extrair nome, se houver atributo 'nome'
        opcoes = []
        for e in empresas:
            nome = getattr(e, "nome", None)
            if nome:
                opcoes.append(nome)
            else:
                opcoes.append(str(e))

        layout = [
            [sg.Text("Selecione a empresa responsável:", font=("Segoe UI", 12))],
            [sg.Combo(opcoes, size=(60,1), key="-EMP-")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Selecionar Empresa", layout, element_justification="center")
        event, values = window.read()
        window.close()

        if event != "OK":
            return None

        selecionado = values.get("-EMP-")
        if not selecionado:
            return None

        # retorna o objeto empresa correspondente
        for e in empresas:
            nome = getattr(e, "nome", None)
            if nome == selecionado or str(e) == selecionado:
                return e

        return None

    # -------------------------------------------------
    def lista_meios(self, meios):
        # constrói uma string grande para exibir a lista completa
        linhas = []
        for m in meios:
            tipo = getattr(m, "tipo", "")
            capacidade = getattr(m, "capacidade", "")
            empresa = getattr(m, "empresa", "")
            nome_empresa = getattr(empresa, "nome", str(empresa)) if empresa is not None else ""
            linhas.append(f"Tipo: {tipo} | Capacidade: {capacidade} | Empresa: {nome_empresa}")

        texto = "\n".join(linhas) if linhas else "Nenhum meio cadastrado."
        sg.popup_scrolled(texto, title="Meios de Transporte", size=(80,20))
