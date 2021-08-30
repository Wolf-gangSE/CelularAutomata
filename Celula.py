
class Celula:
  def __init__(self, estado):
      self.__estado = estado
      self.__vizinhos = []
      self.__estadoFuturo = estado

  def getEstado(self):
      return self.__estado

  def setEstado(self, estado):
      self.__estado = estado

  def setEstadoFuturo(self, estado):
      self.__estadoFuturo = estado

  def getEstadoFuturo(self):
      return self.__estadoFuturo

  # a regra de atualizacao do estado futuro será implementada nas classes filhas
  def analisarVizinhos(self):
      raise NotImplementedError

  # depois de analisar a vizinhanca, a celula deve atualizar o seu estado atual
  def atualizarEstado(self):
      self.__estado = self.__estadoFuturo

  # adiciona uma célula na lista de células vizinhas
  def AddVizinho(self, c):
      self.__vizinhos.append(c)

  # retorna a lista de vizinhos da célula
  def getVizinhos(self):
      return self.__vizinhos

  # Verificar quantos vizinhos cada celula possui
  def contaVizinhos(self):
      return len(self.__vizinhos)

  # as cores serao definidas de acordo com as classes filhas
  def getColor(self):
      raise NotImplementedError

  def getModelo(self):
      return "Celula"

  def getQteVizinhosEstado(self, state):
      qte = 0
      for i in range(0, len(self.__vizinhos)):
          vizinho = self.__vizinhos[i]
          if vizinho.getEstado() == state:
              qte += 1
      return qte