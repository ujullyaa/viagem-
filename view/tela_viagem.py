import FreeSimpleGUI as sg


class TelaViagem:
    def __init__(self):
        sg.theme('DarkBlue3')

    def tela_opcoes(self):

        layout = [
            [sg.Text('Sistema de Gerenciamento de Viagens',
                    font='Arial 18', justification='center')],
            [sg.HSeparator()],
            [sg.Button('1 - Cadastrar Viagem', key=1, size=(30, 2))],
            [sg.Button('2 - Listar Viagens', key=2, size=(30, 2))],
            [sg.Button('3 - Reservar Viagem', key=3, size=(30, 2))],
            [sg.Button('4 - Cancelar Passagem', key=4, size=(30, 2))],
            [sg.Button('5 - Atualizar Status', key=5, size=(30, 2))],
            [sg.Button('6 - Alterar Viagem', key=6, size=(30, 2))],
            [sg.Button('7 - Excluir Viagem', key=7, size=(30, 2))],
            [sg.Button('0 - Voltar ao Menu Principal', key='-VOLTAR-',
                        size=(30, 2), button_color=('white', 'firebrick3'))]
        ]

        window = sg.Window('Menu Viagens', layout, finalize=True, element_justification='center')
        event, values = window.read()
        window.close()

        if event == '-VOLTAR-':
            return 0

        return event

    def pega_dados_viagem(self):

        layout = [
            [sg.Text('Código da Viagem:', size=(20, 1)),
            sg.Input(key='codigo')],
            [sg.Text('CPF do Passageiro:', size=(20, 1)), sg.Input(key='cpf')],
            [sg.Text('Data Partida (dd/mm/aaaa):', size=(20, 1)),
            sg.Input(key='data_partida')],
            [sg.Text('Data Chegada (dd/mm/aaaa):', size=(20, 1)),
            sg.Input(key='data_chegada')],
            [sg.Button('Confirmar', key='confirmar'),
            sg.Button('Cancelar', key='-CANCELAR-')]
        ]

        window = sg.Window('Cadastrar Viagem', layout)
        event, values = window.read()
        window.close()

        if event != 'confirmar':
            return None

        return {
            'codigo': values['codigo'], 'cpf': values['cpf'],
            'data_partida': values['data_partida'], 'data_chegada': values['data_chegada']
        }

    def mostra_viagens(self, lista):
        texto = '\n'.join(
            [f"Código: {v.get('codigo', 'N/A')} | Partida: {v.get('data', 'N/A')} | Status: {v.get('status', 'N/A')} | Passagens: {v.get('passagens', 0)}" for v in lista])

        sg.popup_scrolled(
            texto if texto else 'Nenhuma viagem cadastrada.', title='Lista de Viagens', size=(50, 10))

    def seleciona_viagem(self):

        layout = [
            [sg.Text('Digite o código da viagem:')],
            [sg.Input(key='codigo')],
            [sg.Button('OK'), sg.Button('Cancelar', key='-CANCELAR-')]
        ]

        window = sg.Window('Selecionar Viagem', layout)
        event, values = window.read()
        window.close()

        if event != 'OK':
            return None

        return values['codigo']

    def pega_novo_status(self):
        layout = [
            [sg.Text('Selecione o novo status:')],
            [sg.Combo(['Pendente', 'Confirmada', 'Em Curso', 'Concluída', 'Cancelada'],
                    default_value='Pendente', key='status')],
            [sg.Button('Confirmar'), sg.Button('Cancelar', key='-CANCELAR-')]
        ]
        window = sg.Window('Atualizar Status', layout)
        event, values = window.read()
        window.close()

        if event == 'Confirmar':
            return values['status']
        return None

    def seleciona_passagem(self, lista_passagens: list):
        if not lista_passagens:
            self.mostra_mensagem(
                "Não há passagens disponíveis para selecionar.")
            return None

        codigos = [p['codigo'] for p in lista_passagens]

        layout = [
            [sg.Text('Selecione o código da passagem para cancelar:')],
            [sg.Combo(codigos, key='cod_passagem')],
            [sg.Button('OK'), sg.Button('Cancelar', key='-CANCELAR-')]
        ]

        window = sg.Window('Cancelar Passagem', layout)
        event, values = window.read()
        window.close()

        if event == 'OK':
            return values['cod_passagem']
        return None

    def pega_dados_alteracao(self, dados_atuais):
        layout = [
            [sg.Text('Alterar Dados da Viagem', font='Arial 14')],

            [sg.Text('Data Partida:'), sg.Input(
                default_text=dados_atuais.get('data_partida', ''), key='data_partida')],
            [sg.Text('Data Chegada:'), sg.Input(
                default_text=dados_atuais.get('data_chegada', ''), key='data_chegada')],
            [sg.Text('Status Atual:'), sg.Input(
                default_text=dados_atuais.get('status', ''), key='status')],
            [sg.Text('CPF do Passageiro:'), sg.Input(
                default_text=dados_atuais.get('cpf', ''), key='cpf')],

            [sg.Button('Salvar', key='salvar'), sg.Button(
                'Cancelar', key='-CANCELAR-')]
        ]

        window = sg.Window('Alterar Viagem', layout)
        event, values = window.read()
        window.close()

        if event != 'salvar':
            return None

        return values

    def mostra_mensagem(self, msg):
        sg.popup(msg)
