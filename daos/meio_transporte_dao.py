from daos.dao import DAO
from model.meio_transporte import MeioTransporte

class MeioTransporteDAO(DAO):
    def __init__(self):
        super().__init__('meio_transporte.pkl')

    def add(self, meio_transporte: MeioTransporte):
        
        if meio_transporte and isinstance(meio_transporte, MeioTransporte) and isinstance(meio_transporte.tipo, str):
            super().add(meio_transporte.tipo.lower().strip(), meio_transporte)

    def update(self, meio_transporte: MeioTransporte):
        
        if meio_transporte and isinstance(meio_transporte, MeioTransporte) and isinstance(meio_transporte.tipo, str):
            super().update(meio_transporte.tipo.lower().strip(), meio_transporte)

    def get(self, key: str):
       
        if isinstance(key, str):
            return super().get(key.lower().strip())

    def remove(self, key: str):
       
        if isinstance(key, str):
            return super().remove(key.lower().strip())
