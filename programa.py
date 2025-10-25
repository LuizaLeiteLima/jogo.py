from funcoes import *

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

for nome in frota.keys():
    if nome == "porta-aviões":
        tamanho = 4
        quantidade = 1
    elif nome == "navio-tanque":
        tamanho = 3
        quantidade = 2
    elif nome == "contratorpedeiro":
        tamanho = 2
        quantidade = 3
    elif nome == "submarino":
        tamanho = 1
        quantidade = 4

    for v in range(quantidade):
        f = False
        while not f:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input("coloque a linha:"))
            coluna = int(input("coloque a coluna:"))

            if nome != "submarino":
                orientacao = int(input("coloque a orientação:"))
                if orientacao == 1:
                    orientacao = 'vertical'
                elif orientacao == 2:
                    orientacao = 'horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
                print("Esta posição não está válida!")
            else:
                define_posicoes(linha, coluna, orientacao, tamanho)
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                f = True

import random

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)
print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
while True:
    linha = int(input('qual linha ataca:'))
    while linha < 0 or linha > 9:
        print('Linha inválida!')
        linha = int(input('qual linha ataca:'))
    coluna = int(input('qual coluna ataca: '))
    while coluna < 0 or coluna > 9:
        print('Coluna inválida!')
        coluna = int(input('qual coluna ataca:'))
    if tabuleiro_oponente[linha][coluna] == '-' or tabuleiro_oponente[linha][coluna] == 'X':
        print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        continue
    else:
        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)
    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        break
    else:
        while True: 
            linha1 = random.randint(0, 9)
            coluna2 = random.randint(0, 9)
            if tabuleiro_jogador[linha1][coluna2] == '-' or tabuleiro_jogador[linha1][coluna2] == 'X':
                continue
            tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha1, coluna2)
            print(f"Seu oponente está atacando na linha {linha1} e coluna {coluna2}")
            break

    if afundados(frota, tabuleiro_jogador) == 10:
        print("o oponente derrubo suas frotas")
        break
    
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))


