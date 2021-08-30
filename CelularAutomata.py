import GameOfLife
from PIL import Image, ImageDraw, ImageColor

class CelularAutomata:
    # metodo que cria a classe CelularAutomata, o parâmetro modelo definirá qual classe de células será utilizada
    def __init__(self, modelo, linhas, colunas):
        self.__linhas = linhas
        self.__colunas = colunas
        self.__modelo = modelo
        # quantas vezes o automata celular foi atualizado
        self.__interacao = 0

        self.__matrix = [[GameOfLife.CelulaGOL() for x in range(colunas)] for y in range(linhas)]
        
        for i in range(linhas):
            for j in range(colunas):
                # Adicionar para cada celula as referencias dos oito vizinhos
                if (i > 0 and j > 0):
                    self.__matrix[i][j].AddVizinho(self.__matrix[i - 1][j - 1])
                if (i > 0):
                    self.__matrix[i][j].AddVizinho(self.__matrix[i - 1][j])
                if (i > 0 and j < colunas - 1):
                    self.__matrix[i][j].AddVizinho(self.__matrix[i - 1][j + 1])
                if (j > 0):
                    self.__matrix[i][j].AddVizinho(self.__matrix[i][j - 1])
                if (j < colunas - 1):
                    self.__matrix[i][j].AddVizinho(self.__matrix[i][j + 1])
                if (i < linhas - 1 and j > 0):
                    self.__matrix[i][j].AddVizinho(self.__matrix[i + 1][j - 1])
                if (i < linhas - 1):
                    self.__matrix[i][j].AddVizinho(self.__matrix[i + 1][j])
                if (i < linhas - 1 and j < colunas - 1):
                    self.__matrix[i][j].AddVizinho(self.__matrix[i + 1][j + 1])

    # retorna a celula na posicao i,j
    def getCelula(self, i, j):
        return self.__matrix[i][j]

    # método que processa os estados das celulas vizinhas para definir o proximo estado de cada celula
    def analisaCA(self):
        for i in range(self.__linhas):
            for j in range(self.__colunas):
                self.__matrix[i][j].analisarVizinhos()

    # método que atualiza o estado de cada celula com base em seu estado futuro
    def atualizaCA(self):
        for i in range(self.__linhas):
            for j in range(self.__colunas):
                self.__matrix[i][j].atualizarEstado()
        self.__interacao = self.__interacao + 1

    # método que conta a quantidade de celulas que possui determinado estado
    # utilizarei para parar a criacao de imagens, quanto todas as celulas estiver mortas
    def contaCelulasEstado(self, estado):
        qte = 0
        for i in range(self.__linhas):
            for j in range(self.__colunas):
                if self.__matrix[i][j].getEstado() == estado:
                    qte = qte + 1
        return qte

    #verifica se há no CA celulas que permitam interacao (nao mortas)
    # True - todas as células morreram
    def morreu(self):
        if self.__modelo != 3:
            if self.contaCelulasEstado(0) == self.__linhas*self.__colunas:
                return True
            else:
                return False
        else:
            soma = 0
            for i in range(self.__linhas):
                for j in range(self.__colunas):
                    soma = soma + self.__matrix[i][j].getEstado()
            if soma == 0:
                return True
            else:
                return False

    def getImage(self, legenda):
        # diametro do circulo a ser inserido na imagem, igual ao da referencia Generative Art.
        tam = 10
        img = Image.new('RGB', (tam * self.__linhas, tam * self.__colunas), color='white')
        d = ImageDraw.Draw(img)

        for i in range(self.__linhas):
            for j in range(self.__colunas):
                # o metodo ImageColor.getrgb transforma o texto em um objeto color (r,g,b)
                d.ellipse((tam * i, tam * j, tam * (i + 1), tam * (j + 1)),
                  fill=ImageColor.getrgb(self.__matrix[i][j].getColor()), outline=(0, 0, 0))

        if legenda > 0:
            msg = "Modelo: " + self.__matrix[i][j].getModelo() + " interacao: " + str(self.__interacao)
            # inserindo texto na imagem, posicao (1,1), cor amarela
            d.text((1, 1), msg, fill=(18, 10, 143))
        return img