from Celula import Celula
from random import SystemRandom

class CelulaGOL(Celula):
  def __init__(self):
      
      rnd = SystemRandom()
      escolha = rnd.random()

      if escolha > 0.5:
        # Celula indica chamada do metodo (__init__) da classe pai (Celula)
        Celula.__init__(self, False)  # morto
      else:
        Celula.__init__(self, True)  # vivo

  # o metodo verifica o estado de vivo das células adjacentes e em outro momento
  # derá atualizado o estado da celula, via método atualizarEstado()
  def analisarVizinhos(self):
      # Dois estados vivo(1) e morto (0)
      vivos = self.getQteVizinhosEstado(True)
      # Regra 1
      if (self.getEstado() == True):
          if (vivos == 2 or vivos == 3):
            self.setEstadoFuturo(True)
          # Caso contrário, morrerá por solidão ou superpopulação.
          else:
            self.setEstadoFuturo(False)
      # Regra 2: 
      else:
          if (vivos == 3):
            self.setEstadoFuturo(True)
          else:
            self.setEstadoFuturo(False)

  def getColor(self):
        if self.getEstado() == True:
            return 'black'
        else:
            return 'white'

      # sobrescrito o método getModelo para retornar o nome da classe de célula atual
  def getModelo(self):
        return "Celula da Vida"