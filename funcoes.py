def define_posicoes(linha, coluna, orientacao, tamanho):
    i = 0
    posicao = []
    while i < tamanho :
        u = []
        if orientacao == "vertical":
            u.append(linha)
            u.append(coluna)
            linha = linha + 1 
        elif orientacao == "horizontal":
            u.append(linha)
            u.append(coluna)
            coluna = coluna + 1 
        i = i + 1
        posicao.append(u)
    return posicao
   
def preenche_frota (frota,nome, linha, coluna, orientacao, tamanho):

    o = define_posicoes(linha, coluna, orientacao, tamanho)


    if nome in frota:
        frota[nome].append(o)
    else:
        frota[nome] = [o]

    return frota

def faz_jogada (tabuleiro,linha,coluna):

    if tabuleiro[linha][coluna] == 1:
         tabuleiro[linha][coluna] = 'X'

    else: 
        tabuleiro[linha][coluna] = '-'

    return tabuleiro


