from model.pessoa import Pessoa
from view.tela_pessoa import TelaPessoa
from daos.pessoa_dao import PessoaDAO
# --- IMPORTS DAS EXCEPTIONS ---
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException

class ControladorPessoa:
    def __init__(self, controlador_controladores):
        self.__pessoa_dao = PessoaDAO()
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_controladores = controlador_controladores

    # --- Validadores ---
    def __validar_cpf(self, cpf):
        cpf = ''.join(filter(str.isdigit, str(cpf)))
        if len(cpf) != 11: return False
        return True
    
    def __validar_telefone(self, telefone):
        tel = ''.join(filter(str.isdigit, str(telefone)))
        return 10 <= len(tel) <= 11

    # --- CORREÇÃO AQUI: VALIDAÇÃO DE IDADE >= 18 ---
    def __validar_idade(self, idade):
        try:
            i = int(idade)
            if i < 18:
                # Retorna False e a mensagem específica solicitada
                return False, "Pessoa menor de idade. Cadastro não permitido."
            return True, i
        except ValueError:
            return False, "A idade deve ser um número inteiro válido."

    # --- Helpers ---
    def pega_pessoa_por_cpf(self, cpf):
        for p in self.__pessoa_dao.get_all():
            if p.cpf == cpf: return p
        return None
    
    def __monta_lista_dados(self):
        return [{"nome": p.nome, "idade": p.idade, "cpf": p.cpf, "telefone": p.telefone} for p in self.__pessoa_dao.get_all()]

    # --- MÉTODOS PRINCIPAIS ---

    def incluir_pessoa(self):
        dados = self.__tela_pessoa.pega_dados_pessoa()
        if not dados: return

        try:
            cpf_limpo = ''.join(filter(str.isdigit, dados["cpf"]))
            
            # EXCEPTION: Elemento Repetido
            if self.pega_pessoa_por_cpf(cpf_limpo):
                raise ElementoRepetidoException(f"Já existe uma pessoa com o CPF {cpf_limpo}")

            if not self.__validar_cpf(cpf_limpo):
                self.__tela_pessoa.mostra_mensagem("CPF inválido.")
                return

            # Valida Idade (Agora barra menores de 18)
            valido_idade, res_idade = self.__validar_idade(dados["idade"])
            if not valido_idade:
                self.__tela_pessoa.mostra_mensagem(f"Erro: {res_idade}")
                return

            # Valida Telefone
            if not self.__validar_telefone(dados["telefone"]):
                self.__tela_pessoa.mostra_mensagem("Telefone inválido.")
                return

            pessoa = Pessoa(dados["nome"], res_idade, cpf_limpo, dados["telefone"])
            self.__pessoa_dao.add(pessoa)
            self.__tela_pessoa.mostra_mensagem("Pessoa cadastrada com sucesso!")

        except ElementoRepetidoException as e:
            self.__tela_pessoa.mostra_mensagem(str(e))

    def alterar_pessoa(self):
        try:
            dados_pessoas = self.__monta_lista_dados()
            cpf_selecionado = self.__tela_pessoa.seleciona_pessoa_por_lista(dados_pessoas)
            if not cpf_selecionado: return

            pessoa = self.pega_pessoa_por_cpf(cpf_selecionado)
            
            # EXCEPTION: Elemento Não Existe
            if not pessoa:
                raise ElementoNaoExisteException("Pessoa não encontrada no sistema.")

            novos_dados = self.__tela_pessoa.pega_dados_pessoa(pessoa_existente=pessoa)
            if not novos_dados: return

            # Valida Idade na alteração também
            valido_idade, res_idade = self.__validar_idade(novos_dados["idade"])
            if not valido_idade:
                self.__tela_pessoa.mostra_mensagem(f"Erro: {res_idade}")
                return
            
            if not self.__validar_telefone(novos_dados["telefone"]):
                self.__tela_pessoa.mostra_mensagem("Telefone inválido.")
                return

            pessoa.nome = novos_dados["nome"]
            pessoa.idade = res_idade
            pessoa.telefone = novos_dados["telefone"]

            self.__pessoa_dao.update(pessoa)
            self.__tela_pessoa.mostra_mensagem("Pessoa alterada com sucesso!")

        except ElementoNaoExisteException as e:
            self.__tela_pessoa.mostra_mensagem(str(e))

    def excluir_pessoa(self):
        try:
            dados_pessoas = self.__monta_lista_dados()
            cpf_selecionado = self.__tela_pessoa.seleciona_pessoa_por_lista(dados_pessoas)
            if not cpf_selecionado: return

            pessoa = self.pega_pessoa_por_cpf(cpf_selecionado)
            
            # EXCEPTION: Elemento Não Existe
            if not pessoa:
                raise ElementoNaoExisteException("Pessoa não encontrada para exclusão.")

            self.__pessoa_dao.remove(pessoa.cpf)
            self.__tela_pessoa.mostra_mensagem("Pessoa excluída com sucesso!")

        except ElementoNaoExisteException as e:
            self.__tela_pessoa.mostra_mensagem(str(e))

    def listar_pessoas(self):
        dados_pessoas = self.__monta_lista_dados()
        self.__tela_pessoa.mostra_pessoas(dados_pessoas)

    def escolher_pessoa_externo(self):
        dados = self.__monta_lista_dados()
        cpf = self.__tela_pessoa.seleciona_pessoa_por_lista(dados)
        if not cpf: return None
        return self.pega_pessoa_por_cpf(cpf)

    def retornar(self):
        # Apenas return vazio para encerrar o loop e voltar ao menu anterior
        return

    def abre_tela(self):
        opcoes = {
            1: self.incluir_pessoa, 
            2: self.alterar_pessoa, 
            3: self.listar_pessoas, 
            4: self.excluir_pessoa, 
            0: self.retornar
        }
        while True:
            opcao = self.__tela_pessoa.tela_opcoes()
            funcao = opcoes.get(opcao)
            
            if opcao == 0:
                funcao()
                break
            elif funcao:
                funcao()
            else:
                self.__tela_pessoa.mostra_mensagem("Opção inválida.")