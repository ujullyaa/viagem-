from daos.dao import DAO
from model.meio_transporte import MeioTransporte

class MeioTransporteDAO(DAO):
    def __init__(self):
        super().__init__('meio_transporte.pkl')

    def add(self, meio: MeioTransporte):
        if meio is not None:
            super().add(meio.tipo, meio)

    def update(self, meio):
        if meio is not None:
            super().update(meio.tipo, meio)

    def get(self, tipo: str):
        return super().get(tipo)

    def remove(self, tipo: str):
        super().remove(tipo)

    def get_all(self):
        return list(super().get_all())
