class Conta:

  def __init__(self,numero,titular,saldo,limite):
    print("Construindo um objeto...")
    self.__numero = numero
    self.__titular = titular
    self.__saldo = saldo
    self.__limite = limite
    

  def extrato(self):
    print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

  def deposita(self, valor):
    self.__saldo += valor  

  def __pode_sacar(self, valor_a_sacar):
    valor_disponivel_a_sacar =(self.__limite + self.__saldo)
    return valor_a_sacar <= valor_disponivel_a_sacar
    pass

  def saque(self, valor):
    if(self.__pode_sacar(valor)):
      self.__saldo -= valor  
    else:
      print("O valor {} passou o limite ".format(valor))  

  def transfere(self, valor, origem, destino):
    self.saque(valor)
    destino.deposita(valor)

  @property
  def saldo(self):
    return self.__saldo  

  @property
  def titular(self):
    return self.__titular

  @property
  def limite(self):
    return self.__limite

  @limite.setter
  def limite(self,limite):
    self.__limite = limite

@staticmethod
def codigo_banco(self):
  return "001"

@staticmethod
def codigos_bancos(self):
  return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'} 
  