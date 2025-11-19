from model.pessoa import Pessoa
from view.tela_pessoa import TelaPessoa
from daos.pessoa_dao import PessoaDAO

class ControladorPessoa:
    def __init__(self, controlador_controladores):
        self.__pessoa_dao = PessoaDAO()
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_controladores = controlador_controladores

    # --- Validações ---
    def __validar_cpf(self, cpf):
        cpf = ''.join(filter(str.isdigit, str(cpf)))
        if len(cpf) != 11 or cpf == cpf[0] * 11: return False
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = (soma * 10) % 11
        if resto == 10: resto = 0
        if resto != int(cpf[9]): return False
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = (soma * 10) % 11
        if resto == 10: resto = 0
        if resto != int(cpf[10]): return False
        return True

    def __validar_idade(self, idade):
        try:
            idade_int = int(idade)
            if idade_int >= 18: return True, idade_int
            else: return False, "A pessoa deve ser maior de idade (>= 18)."
        except ValueError: return False, "A idade deve ser um número inteiro."

    def __validar_telefone(self, telefone):
        tel_limpo = ''.join(filter(str.isdigit, str(telefone)))
        return 10 <= len(tel_limpo) <= 11

    # --- Auxiliar para formatar dados para a tabela ---
    def __monta_lista_dados(self):
        pessoas = self.__pessoa_dao.get_all()
        dados_pessoas = []
        for p in pessoas:
            dados_pessoas.append({
                "nome": p.nome, 
                "idade": p.idade, 
                "cpf": p.cpf, 
                "telefone": p.telefone
            })
        return dados_pessoas

    # --- Métodos Principais ---

    def pega_pessoa_por_cpf(self, cpf):
        for pessoa in self.__pessoa_dao.get_all():
            if pessoa.cpf == cpf:
                return pessoa
        return None

    def incluir_pessoa(self):
        dados = self.__tela_pessoa.pega_dados_pessoa()
        if not dados: return

        cpf_limpo = ''.join(filter(str.isdigit, dados["cpf"]))
        if not self.__validar_cpf(cpf_limpo):
            self.__tela_pessoa.mostra_mensagem("Erro: CPF inválido.")
            return

        if self.pega_pessoa_por_cpf(cpf_limpo):
            self.__tela_pessoa.mostra_mensagem("Erro: CPF já cadastrado.")
            return

        valido_idade, res_idade = self.__validar_idade(dados["idade"])
        if not valido_idade:
            self.__tela_pessoa.mostra_mensagem(f"Erro: {res_idade}")
            return
        
        if not self.__validar_telefone(dados["telefone"]):
            self.__tela_pessoa.mostra_mensagem("Erro: Telefone inválido.")
            return

        pessoa = Pessoa(dados["nome"], res_idade, cpf_limpo, dados["telefone"])
        self.__pessoa_dao.add(pessoa)
        self.__tela_pessoa.mostra_mensagem("Pessoa cadastrada com sucesso!")

    def alterar_pessoa(self):
        # 1. Pega todos os dados
        dados_pessoas = self.__monta_lista_dados()
        
        # 2. Chama a nova tela de seleção por tabela
        cpf_selecionado = self.__tela_pessoa.seleciona_pessoa_por_lista(dados_pessoas)
        
        # Se o usuário fechou ou cancelou a janela de seleção
        if not cpf_selecionado:
            return

        # 3. Busca o objeto
        pessoa = self.pega_pessoa_por_cpf(cpf_selecionado)

        if pessoa:
            # 4. Abre tela de edição com dados pré-preenchidos
            novos_dados = self.__tela_pessoa.pega_dados_pessoa(pessoa_existente=pessoa)
            if not novos_dados: return

            # Validações
            valido_idade, res_idade = self.__validar_idade(novos_dados["idade"])
            if not valido_idade:
                self.__tela_pessoa.mostra_mensagem(f"Erro: {res_idade}")
                return

            if not self.__validar_telefone(novos_dados["telefone"]):
                self.__tela_pessoa.mostra_mensagem("Erro: Telefone inválido.")
                return

            # Atualiza
            pessoa.nome = novos_dados["nome"]
            pessoa.idade = res_idade
            pessoa.telefone = novos_dados["telefone"]

            self.__pessoa_dao.update(pessoa)
            self.__tela_pessoa.mostra_mensagem("Pessoa alterada com sucesso!")
        else:
            self.__tela_pessoa.mostra_mensagem("Erro: Pessoa não encontrada no sistema.")

    def listar_pessoas(self):
        dados_pessoas = self.__monta_lista_dados()
        self.__tela_pessoa.mostra_pessoas(dados_pessoas)

    def excluir_pessoa(self):
        # Também atualizei para usar a tabela! É muito mais fácil excluir clicando na lista.
        dados_pessoas = self.__monta_lista_dados()
        cpf_selecionado = self.__tela_pessoa.seleciona_pessoa_por_lista(dados_pessoas)
        
        if not cpf_selecionado:
            return

        pessoa = self.pega_pessoa_por_cpf(cpf_selecionado)
        if pessoa:
            self.__pessoa_dao.remove(pessoa.cpf)
            self.__tela_pessoa.mostra_mensagem("Pessoa excluída com sucesso!")
        else:
            self.__tela_pessoa.mostra_mensagem("Pessoa não encontrada.")

    def retornar(self):
        self.__controlador_controladores.inicializa_sistema()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_pessoa,
            2: self.alterar_pessoa,
            3: self.listar_pessoas,
            4: self.excluir_pessoa,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_pessoa.tela_opcoes()
            funcao = lista_opcoes.get(opcao)
            
            if opcao == 0:
                funcao()
                break
            elif funcao:
                funcao()
            else:
                self.__tela_pessoa.mostra_mensagem("Opção inválida.")