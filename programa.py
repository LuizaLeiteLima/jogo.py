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
                continue

        define_posicoes(linha, coluna, orientacao, tamanho)
        frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)

print(frota)
