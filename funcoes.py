def define_posicoes(linha, coluna, orientacao, tamanho):
    i = 0
    posicao = []
    while i < tamanho + 1:
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
    
linha = 2
coluna = 4
orientacao = "vertical"
tamanho = 3

print(define_posicoes(linha, coluna, orientacao, tamanho))
        

