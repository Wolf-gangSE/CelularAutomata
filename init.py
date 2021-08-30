from CelularAutomata import CelularAutomata
import imageio
import os

# cria para o modelo de automata celular indicado por m, as imagens para interacoes pedidas
def criaImagens(diretorio, m, interacoes):
    if m > 3:
        print('Modelo nao previsto')
        exit()
    ca = CelularAutomata(m, 50, 30)
    # tenho que padronizar a quantidade de digitos a ser escrita no nome do arquivo
    # para ordenar
    tam = len(str(interacoes))
    indice = ''
    for i in range(tam):
        indice = indice + str(0)
    ca.getImage(1).save(diretorio + 'img_' + str(m) + '_' + indice + '.jpeg')
    # faca n  mudancas de estado e salve a imagem de cada uma
    for i in range(0, interacoes):
        # ao analisar e atualizar, acontece uma interacao
        ca.analisaCA()
        ca.atualizaCA()
        indice = ''
        for j in range(tam - len(str(i + 1))):
            indice = indice + str(0)
        indice = indice + str(i + 1)
        ca.getImage(1).save(diretorio + 'img_' + str(m) + '_' + indice + '.jpeg')
        # se todo o CA morreu, terminar
        if ca.morreu() == True: 
            break

def criarGif(pathImagens, pathGifs, m):
    dirImagens = os.fsencode(pathImagens)
    imagens = []
    for file in os.listdir(dirImagens):
        filename = os.fsdecode(file)
        if filename.endswith( ('.jpeg', '.gif') ) and filename.find("img_" + str(m)) != -1:
            imagens.append(imageio.imread(pathImagens + filename))
    imageio.mimsave(pathGifs + 'exemplo' + str(m) + '.gif', imagens)

def apagarArquivos(path):
    dir = os.listdir(path)
    for file in dir:
        os.remove(path + file)


if __name__ == "__main__":
    pathImagens = '/Users/lucas/Programacao/TC/CelularAutomata/Imagens/'
    pathGifs = '/Users/lucas/Programacao/TC/CelularAutomata/Gifs/'
    apagarArquivos(pathGifs)
    for m in range(4):
        if m == 0:
            # GOL 100 iteracoes
            criaImagens(pathImagens, m, 100)
            criarGif(pathImagens, pathGifs, m)
        elif m == 1:
            #  Vichniac, 166 iteracoes
            criaImagens(pathImagens, m, 166)
            criarGif(pathImagens, pathGifs, m)
        elif m == 2:
            #  Brian Brain, 20 iteracoes
            criaImagens(pathImagens, m, 20)
            criarGif(pathImagens, pathGifs, m)
        elif m == 3:
            #  Onda, 70 iteracoes
            criaImagens(pathImagens, m, 70)
            criarGif(pathImagens, pathGifs, m)
    apagarArquivos(pathImagens)