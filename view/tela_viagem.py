import FreeSimpleGUI as sg

class TelaViagem:
    def __init__(self):
        sg.theme('DarkBlue3')

    def tela_opcoes(self):
        layout = [
            [sg.Column(
                [
                    [sg.Text('🚍 Menu de Viagens', font=("Segoe UI", 18, "bold"))],
                    [sg.HorizontalSeparator()],
                    [sg.Button('1 - Cadastrar Viagem', size=(35, 1))],
                    [sg.Button('2 - Listar Viagens', size=(35, 1))],
                    [sg.Button('3 - Atualizar Status', size=(35, 1))],
                    [sg.Button('4 - Alterar Viagem', size=(35, 1))],
                    [sg.Button('5 - Excluir Viagem', size=(35, 1))],
                    [sg.HorizontalSeparator()],
                    [sg.Button('0 - Voltar ao Menu Principal', button_color=('white', 'red'), size=(35, 1))]
                ],
                element_justification="center",
                expand_x=True
            )]
        ]

        window = sg.Window('Gestão de Viagens', layout, element_justification='center')
        
        # --- CORREÇÃO DE LEITURA SEGURA ---
        resultado = window.read()
        window.close()

        if resultado is None: # Se a janela foi destruída
            return 0
        
        event, _ = resultado # Desempacota apenas se não for None

        if event in (sg.WINDOW_CLOSED, '0 - Voltar ao Menu Principal'): 
            return 0
        
        opcoes = {
            '1 - Cadastrar Viagem': 1,
            '2 - Listar Viagens': 2,
            '3 - Atualizar Status': 3, 
            '4 - Alterar Viagem': 4, 
            '5 - Excluir Viagem': 5
        }
        return opcoes.get(event, 0)

    def pega_dados_viagem(self, viagem=None):
        cod = viagem.codigo if viagem else ""
        d_partida = viagem.data_partida if viagem else ""
        d_chegada = viagem.data_chegada if viagem else ""
        
        cpf = ""
        if viagem and viagem.passageiro:
            cpf = viagem.passageiro.cpf

        layout = [
            [sg.Text('✈️ Dados da Viagem', font=("Segoe UI", 14, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text('Código:', size=(20, 1)), sg.Input(default_text=cod, key='codigo', disabled=(viagem is not None), size=(40,1))],
            [sg.Text('CPF do Passageiro:', size=(20, 1)), sg.Input(default_text=cpf, key='cpf', size=(40,1))],
            [sg.Text('Data Partida (dd/mm/aaaa):', size=(20, 1)), sg.Input(default_text=d_partida, key='data_partida', size=(40,1))],
            [sg.Text('Data Chegada (dd/mm/aaaa):', size=(20, 1)), sg.Input(default_text=d_chegada, key='data_chegada', size=(40,1))],
            [sg.HorizontalSeparator()],
            [sg.Button('Confirmar', size=(20,1)), sg.Button('Cancelar', size=(20,1))]
        ]

        window = sg.Window('Cadastro de Viagem', layout, element_justification="center")
        resultado = window.read()
        window.close()

        if resultado is None: return None
        event, values = resultado

        if event == 'Confirmar':
            return {
                'codigo': values['codigo'], 
                'cpf': values['cpf'],
                'data_partida': values['data_partida'], 
                'data_chegada': values['data_chegada']
            }
        return None

    def seleciona_itinerario(self, lista_itinerarios):
        if not lista_itinerarios:
            sg.popup("Nenhum itinerário disponível.")
            return None
            
        headers = ["Código", "Origem", "Destino"]
        rows = [[i.codigo_itinerario, i.origem, i.destino] for i in lista_itinerarios]
        
        layout = [
            [sg.Text("Selecione o Itinerário:", font=("Arial", 12))],
            [sg.Table(values=rows, headings=headers, key='tab', select_mode='browse', 
                        justification='center', expand_x=True, expand_y=True)], 
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Seleção Itinerário", layout, size=(600,400))
        codigo_selecionado = None
        
        while True:
            # --- CORREÇÃO ---
            resultado = window.read()
            if resultado is None: break
            event, values = resultado
            
            if event in (sg.WIN_CLOSED, "Cancelar"): break
            if event == "Confirmar":
                if values['tab']:
                    idx = values['tab'][0]
                    codigo_selecionado = rows[idx][0]
                    break
        window.close()
        return codigo_selecionado

    def seleciona_meio_transporte(self, lista_meios):
        if not lista_meios:
            sg.popup("Nenhum veículo disponível.")
            return None
            
        mapa_objetos = {}
        rows = []
        
        for idx, m in enumerate(lista_meios):
            empresa_nome = m.empresa_transporte.nome_empresa if hasattr(m, 'empresa_transporte') and m.empresa_transporte else "N/A"
            rows.append([m.tipo, m.capacidade, empresa_nome])
            mapa_objetos[idx] = m
        
        headers = ["Tipo", "Capacidade", "Empresa"]
        
        layout = [
            [sg.Text("Selecione o Veículo:", font=("Arial", 12))],
            [sg.Table(values=rows, headings=headers, key='tab', select_mode='browse', 
                        justification='center', expand_x=True, expand_y=True)], 
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Seleção Veículo", layout, size=(600,400))
        
        objeto_selecionado = None
        
        while True:
            # --- CORREÇÃO ---
            resultado = window.read()
            if resultado is None: break
            event, values = resultado

            if event in (sg.WIN_CLOSED, "Cancelar"): break
            
            if event == "Confirmar":
                if values['tab']:
                    idx_tabela = values['tab'][0]
                    objeto_selecionado = mapa_objetos[idx_tabela]
                    break
                else:
                    sg.popup("Selecione uma linha.")
                    
        window.close()
        return objeto_selecionado

    def mostra_viagens(self, lista):
        texto = ""
        for v in lista:
            texto += f"Cód: {v['codigo']} | Partida: {v['data']} | Status: {v['status']} | Veículo: {v['veiculo']}\n"
            
        sg.popup_scrolled(texto if texto else 'Nenhuma viagem cadastrada.', title='Lista de Viagens', size=(80, 10))

    def seleciona_viagem(self, lista_dados=None):
        if lista_dados:
            headers = ["Cód", "Partida", "Status", "Veículo"]
            rows = [[v['codigo'], v['data'], v['status'], v['veiculo']] for v in lista_dados]
            
            layout = [
                [sg.Text("Selecione a Viagem:", font=("Arial", 12))],
                [sg.Table(values=rows, headings=headers, key='tab', select_mode='browse', 
                        justification='center', expand_x=True, expand_y=True)], 
                [sg.Button("Confirmar"), sg.Button("Cancelar")]
            ]
            window = sg.Window("Seleção Viagem", layout, size=(700,400))
            cod_selecionado = None
            while True:

                resultado = window.read()
                if resultado is None: break
                e, v = resultado

                if e in (sg.WIN_CLOSED, "Cancelar"): break
                if e == "Confirmar":
                    if v['tab']:
                        idx = v['tab'][0]
                        cod_selecionado = rows[idx][0]
                        break
            window.close()
            return cod_selecionado
        else:

            layout = [[sg.Text('Digite o código:')], [sg.Input(key='codigo')], [sg.Button('OK'), sg.Button('Cancelar')]]
            window = sg.Window('Selecionar', layout)
            

            resultado = window.read()
            window.close()
            
            if resultado is None: return None
            e, v = resultado
            
            if e == 'OK': return v['codigo']
            return None

    def pega_novo_status(self):
        layout = [
            [sg.Text('Selecione o novo status:')],
            [sg.Combo(['Pendente', 'Confirmada', 'Em Curso', 'Concluída', 'Cancelada'], default_value='Pendente', key='status')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Atualizar Status', layout)
        

        resultado = window.read()
        window.close()
        
        if resultado is None: return None
        event, values = resultado

        if event == 'Confirmar': return values['status']
        return None

    def pega_dados_alteracao(self, dados_atuais):
        layout = [
            [sg.Text('Alterar Dados da Viagem', font=("Segoe UI", 14, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text('Data Partida:', size=(20,1)), sg.Input(default_text=dados_atuais.get('data_partida', ''), key='data_partida', size=(40,1))],
            [sg.Text('Data Chegada:', size=(20,1)), sg.Input(default_text=dados_atuais.get('data_chegada', ''), key='data_chegada', size=(40,1))],
            [sg.Text('Status Atual:', size=(20,1)), sg.Input(default_text=dados_atuais.get('status', ''), key='status', disabled=True, text_color='gray', size=(40,1))],
            [sg.Text(' (Use "Atualizar Status" para mudar)', font=("Arial", 8), text_color='gray')],
            [sg.Text('CPF do Passageiro:', size=(20,1)), sg.Input(default_text=dados_atuais.get('cpf', ''), key='cpf', size=(40,1))],
            [sg.HorizontalSeparator()],
            [sg.Button('Salvar', key='salvar', size=(20,1)), sg.Button('Cancelar', size=(20,1))]
        ]
        window = sg.Window('Alterar Viagem', layout, element_justification="center")
        

        resultado = window.read()
        window.close()

        if resultado is None: return None
        event, values = resultado

        if event != 'salvar': return None
        return values

    def mostra_mensagem(self, msg):
        sg.popup(msg)