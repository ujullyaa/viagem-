from daos.dao import DAO
from model.meio_transporte import MeioTransporte
import uuid

class MeioTransporteDAO(DAO):
    def __init__(self):
        super().__init__('meio_transporte.pkl')

    def add(self, meio: MeioTransporte):
        if meio is not None:
            # CORREÇÃO: Usar um ID único (UUID) como chave. 
            # Se usar apenas meio.tipo, você só poderia ter 1 Carro no sistema todo.
            chave = uuid.uuid4()
            super().add(chave, meio)

    def update(self, meio):
        if meio is not None:
            # Para atualizar, precisamos encontrar a chave original deste objeto
            chave = self.__find_key(meio)
            if chave:
                super().update(chave, meio)

    def get(self, key):
        return super().get(key)

    def remove(self, meio: MeioTransporte):
        # Para remover, precisamos achar a chave associada a este objeto específico
        chave = self.__find_key(meio)
        if chave:
            super().remove(chave)

    def get_all(self):
        return list(super().get_all())

    # Método auxiliar para achar a chave (UUID) baseada no objeto
    def __find_key(self, meio_procurado):
        todos = super().get_all()
        # O get_all do DAO genérico geralmente retorna valores.
        # Precisamos acessar o dicionário interno self._DAO__cache (depende da sua implementação do DAO pai)
        # Se não tiver acesso direto às chaves, iteramos sobre o cache:
        for chave, objeto in self._DAO__cache.items():
            if objeto == meio_procurado:
                return chave
        return None