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

def posiciona_frota (frota):

    tabuleiro = []
    
    for i in range(10):
        t = []
        for o in range(10):
            t.append(0)
        tabuleiro.append(t)
    for elem in frota.keys():
        for v in frota[elem]:
            for elem1 in v:
                x,y= elem1
                tabuleiro[x][y] = 1

    return tabuleiro

def afundados (frota,tabuleiro):
    mortos = 0

    for elem in frota.keys():
        for o in frota[elem]:
            contador = 0
            for v,k in o:
                if tabuleiro[v][k] == 'X':
                    contador += 1
                    if contador == len(o):
                        mortos += 1
    return mortos

def posicao_valida (frota,linha, coluna, orientacao, tamanho):
    x,y = linha,coluna
    pos = []
    
    for i in range(tamanho):
        if orientacao == 'horizontal':
            if y + i >= 10:
                return False
            pos.append([x,y+i])
        else:
            if x + i >= 10:
                return False
            pos.append([x+i,y])
        for elem in frota.keys():
            for o in frota[elem]:
                for l in o:
                    v,k = l
                    if 0 < v > 9 or 0 < k > 9:
                        return False
                    if [v,k] in pos:
                        return False
    return True

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto
                





