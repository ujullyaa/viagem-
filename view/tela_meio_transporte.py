import FreeSimpleGUI as sg

class TelaMeioTransporte:
    def __init__(self):
        sg.theme("LightGray1")
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
        if event.startswith("1"): return 1
        if event.startswith("2"): return 2
        if event.startswith("3"): return 3
        if event.startswith("4"): return 4
        if event.startswith("0"): return 0
        return 0

    def mostra_mensagem(self, msg):
        sg.popup(msg)

    # -------------------------------------------------
    # Seleciona um meio da lista (para alterar ou excluir)
    # -------------------------------------------------
    def seleciona_meio_transporte(self, meios=None):
        # Se receber a lista de meios, mostra o combo para escolher qual alterar/excluir
        if meios is not None:
            opcoes = []
            mapa_meios = {} # Para mapear a string de volta ao objeto

            for m in meios:
                tipo = getattr(m, "tipo", "Sem Tipo")
                capacidade = getattr(m, "capacidade", "?")
                empresa = getattr(m, "empresa_transporte", None)
                
                # CORREÇÃO: Usar nome_empresa
                nome_empresa = getattr(empresa, "nome_empresa", str(empresa)) if empresa else "Sem Empresa"
                
                # ID visual único para o usuário distinguir (usando memória ou contador se preferir, aqui string simples)
                texto_opcao = f"{tipo} | Cap: {capacidade} | Emp: {nome_empresa}"
                opcoes.append(texto_opcao)
                mapa_meios[texto_opcao] = m

            layout = [
                [sg.Text("Selecione o meio de transporte:", font=("Segoe UI", 12))],
                [sg.Combo(opcoes, size=(60, 1), key="-MEIO-", readonly=True)],
                [sg.Button("OK"), sg.Button("Cancelar")]
            ]
            window = sg.Window("Selecionar Meio", layout, element_justification="center")
            event, values = window.read()
            window.close()

            if event != "OK":
                return None
            
            selecionado_str = values.get("-MEIO-")
            return mapa_meios.get(selecionado_str) # Retorna o OBJETO real, não string

        else:
            return None

    # -------------------------------------------------
    # Pega dados (inclui seleção do tipo fixo)
    # -------------------------------------------------
    def pega_dados_meio_transporte(self, meio=None):
        tipo_inicial = getattr(meio, "tipo", "")
        capacidade_inicial = getattr(meio, "capacidade", "")

        layout = [
            [sg.Text("Dados do Meio de Transporte", font=("Segoe UI", 14, "bold"))],
            [sg.Text("Tipo:", size=(12,1)), sg.Combo(self._tipos_fixos, default_value=tipo_inicial, size=(40,1), key="-TIPO-", readonly=True)],
            [sg.Text("Capacidade:", size=(12,1)), sg.Input(str(capacidade_inicial), size=(40,1), key="-CAP-")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Cadastro Meio de Transporte", layout, element_justification="left")
        event, values = window.read()
        window.close()

        if event != "OK":
            return None

        tipo = values.get("-TIPO-")
        capacidade = values.get("-CAP-")
        
        if not tipo or not capacidade:
            return None

        return {"tipo": tipo, "capacidade": capacidade}

    # -------------------------------------------------
    # Seleciona empresa (CORRIGIDO O ATRIBUTO NOME)
    # -------------------------------------------------
    def seleciona_empresa(self, empresas):
        opcoes = []
        mapa_empresas = {}

        for e in empresas:
            # CORREÇÃO: atributo correto é nome_empresa
            nome = getattr(e, "nome_empresa", None)
            cnpj = getattr(e, "cnpj", "")
            
            if nome:
                texto = f"{nome} (CNPJ: {cnpj})"
            else:
                texto = str(e)
            
            opcoes.append(texto)
            mapa_empresas[texto] = e

        layout = [
            [sg.Text("Selecione a empresa responsável:", font=("Segoe UI", 12))],
            [sg.Combo(opcoes, size=(60,1), key="-EMP-", readonly=True)],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Selecionar Empresa", layout, element_justification="center")
        event, values = window.read()
        window.close()

        if event != "OK":
            return None

        selecionado = values.get("-EMP-")
        return mapa_empresas.get(selecionado)

    # -------------------------------------------------
    # Listagem simples
    # -------------------------------------------------
    def lista_meios(self, meios):
        linhas = []
        for m in meios:
            tipo = getattr(m, "tipo", "")
            capacidade = getattr(m, "capacidade", "")
            empresa = getattr(m, "empresa_transporte", None)
            nome_empresa = getattr(empresa, "nome_empresa", "N/A") if empresa else "N/A"
            
            linhas.append(f"Tipo: {tipo} | Capacidade: {capacidade} | Empresa: {nome_empresa}")

        texto = "\n".join(linhas) if linhas else "Nenhum meio cadastrado."
        sg.popup_scrolled(texto, title="Meios de Transporte", size=(80,20))