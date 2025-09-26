import abc


from abc import ABC, abstractmethod
class Pagamento:
    def __init__(self, forma_pagamento: str, pagou: str, data:str, valor_total: float, passageiro: list):
        self.__forma_pagamento = forma_pagamento
        self.__pagou = pagou 
        self.__data = data
        self.__valor_total = valor_total
        self.__passageiro = passageiro

    @property
    def forma_pagamento(self):
        return self.__forma_pagamento
    
    @forma_pagamento.setter
    def forma_pagamento(self, forma_pagamento):
       self.__forma_pagamento = forma_pagamento

    @property
    def pagou(self):
        return self.__pagou 

    @pagou.setter
    def pagou(self, pagou):
        self.__pagou = pagou 

    @property 
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property 
    def valor_total(self):
        return self.__valor_total

    @valor_total.setter
    def valor_total(self, valor_total):
        self.__valor_total = valor_total

    @property 
    def passageiro(self):
        return self.__passageiro
    
    @passageiro.setter 
    def passageiro(self, passageiro ):
        self.__passageiro = passageiro

class Cartao(Pagamento):
    def __init__(self, processar_pagamento):
        super().__init__(processar_pagamento)

class pix(Pagamento):
    def __init__(self, processar_pagamento):
        super().__init__(processar_pagamento)


class Cedula(Pagamento):
    def __init__(self, processar_pagamento):
        super().__init__(processar_pagamento)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 