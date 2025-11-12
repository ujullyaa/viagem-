from daos.dao import DAO
from model.itinerario import Itinerario

class ItinerarioDAO(DAO):
    def __init__(self):
        super().__init__('itinerario.pkl')

    def add(self, itinerario: Itinerario):
        if itinerario and isinstance(itinerario, Itinerario) and isinstance(itinerario.codigo_itinerario, int):
            super().add(itinerario.codigo_itinerario, itinerario)

    def update(self, itinerario: Itinerario):
        if itinerario and isinstance(itinerario, Itinerario) and isinstance(itinerario.codigo_itinerario, int):
            super().update(itinerario.codigo_itinerario, itinerario)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
