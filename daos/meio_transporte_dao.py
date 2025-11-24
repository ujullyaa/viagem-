from daos.dao import DAO
from model.meio_transporte import MeioTransporte
import uuid


class MeioTransporteDAO(DAO):
    def __init__(self):
        super().__init__('meio_transporte.pkl')

    def add(self, meio: MeioTransporte):
        if meio is not None:
            chave = uuid.uuid4()
            super().add(chave, meio)

    def update(self, meio):
        if meio is not None:
            chave = self.__find_key(meio)
            if chave:
                super().update(chave, meio)

    def get(self, key):
        return super().get(key)

    def remove(self, meio: MeioTransporte):
        chave = self.__find_key(meio)
        if chave:
            super().remove(chave)

    def get_all(self):
        return list(super().get_all())

    def __find_key(self, meio_procurado):
        todos = super().get_all()
        for chave, objeto in self._DAO__cache.items():
            if objeto == meio_procurado:
                return chave
        return None
