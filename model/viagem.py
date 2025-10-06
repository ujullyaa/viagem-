from Itinerario import *
from Meio_transporte import *
from Empresa_transporte import *
from Pagamento import *
from Pessoa import *

class Viajem:
  
  def __init__(self, codigo: str, itinerario: Itinerario, data_partida: str, data_chegada: str, meio_transporte: Meio_transporte, empresa_transporte: Empresa_transporte, status: str, preco_base: float, pagamento: Pagamento, passageiro: Pessoa):
    
    if (isinstance(itinerario, Itinerario)):
      self.__itinerario = itinerario
    if (isinstance(meio_transporte, Meio_transporte )):
      self.__meio_transporte = meio_transporte
    if (isinstance(empresa_transporte, Empresa_transporte)):
      self.__empresa_transporte = empresa_transporte
    if (isinstance(pagamento, Pagamento)):
      self.__pagamento = pagamento
    if (isinstance(passageiro, Pessoa)):
      self.__passageiro = passageiro

    self.__codigo = codigo
    self.__data_partida = data_partida
    self.__data_chegada = data_chegada
    self.__status = status
    self.__preco_base = preco_base

  
  @property
  def itinerario(self):
    return self.__itinerario
  
  @itinerario.setter
  def itinerario(self, itinerario: Itinerario):
    if (isinstance(itinerario, Itinerario)):
      self.__itinerario = itinerario

  @property
  def meio_transporte(self):
    return self.__meio_transporte
  
  @meio_transporte.setter
  def meio_transporte(self, meio_transporte: Meio_transporte):
    if (isinstance(meio_transporte, Meio_transporte )):
      self.__meio_transporte = meio_transporte

  @property
  def empresa_transporte(self):
    return self.__empresa_transporte

  @empresa_transporte.setter
  def empresa_transporte(self, empresa_transporte: Empresa_transporte):
    if (isinstance(empresa_transporte, Empresa_transporte)):
      self.__empresa_transporte = empresa_transporte
  
  @property
  def pagamento(self):
    return self.__pagamento
  
  @pagamento.setter
  def pagamento(self, pagamento: Pagamento):
    if (isinstance(pagamento, Pagamento)):
      self.__pagamento = pagamento

  @property
  def passageiro(self):
    return self.__passageiro
  
  @passageiro.setter
  def passageiro(self, passageiro: Pessoa):
    if (isinstance(passageiro, Pessoa)):
      self.__passageiro = passageiro
      
  @property
  def codigo(self):
    return self.__codigo
  
  @codigo.setter
  def codigo(self, codigo):
    self.__codigo = codigo
  
  @property
  def data_partida(self):
    return self.__data_partida

  @data_partida.setter
  def data_partida(self, data_partida):
    self.__data_partida = data_partida
  
  @property
  def data_chegada(self):
    return self.__data_chegada
  
  @data_chegada.setter
  def data_chegada(self, data_chegada):
    self.__data_chegada = data_chegada
  
  @property
  def status(self):
    return self.__status
  
  @status.setter
  def status(self, status):
    self.__status = status
  
  @property
  def preco_base(self):
    return self.__preco_base
  
  @preco_base.setter
  def preco_base(self, preco_base):
    self.__preco_base = preco_base
  

