from daos.dao import DAO
from model.itinerario import Itinerario

class ItinerarioDAO(DAO):
    def __init__(self):
        super().__init__('itinerario.pkl')

    def add(self, itinerario: Itinerario):
        if itinerario is not None:
            super().add(itinerario.codigo_itinerario, itinerario)

    def update(self, itinerario: Itinerario):
        if itinerario is not None:
            super().update(itinerario.codigo_itinerario, itinerario)

    def get(self, codigo_itinerario: int):
        return super().get(codigo_itinerario)

    def remove(self, codigo_itinerario: int):
        super().remove(codigo_itinerario)

    def get_all(self):
        return list(super().get_all())
