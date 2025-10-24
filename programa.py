from funcoes import * 



frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}  

navio = {
    "porta-aviões": 4,
    "navio-tanque": 3,
    "contratorpedeiro": 2,
    "submarino": 1,
}  


i = 0

for nome, tamanho in frota.items():
    linha = int(input("coloque a linha:"))
    coluna = int(input("coloque a coluna:"))
    orientacao = int(input("coloque a orientação:"))

    if nome == "submarino":
        pass
    else:
        if orientacao == 1:
            orientacao = 'vertical'
        else:
            orientacao = 'horizontal'



    print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho} ")

    # if posicao_valida == False:
    #     print("Esta posição não está válida!")
    #     linha = int(input("coloque a linha:"))
    #     coluna = int(input("coloque a coluna:"))
    # if posicao_valida == True:
    #     if define_posicoes(linha, coluna, orientacao, tamanho):
    #        frota[nome] = preenche_frota(frota,nome, linha, coluna, orientacao, tamanho).append(define_posicoes(linha, coluna, orientacao, tamanho))
    #        linha = int(input("coloque a linha:"))
    #        coluna = int(input("coloque a coluna:"))
    #        i += 1
    #        tamanho += 1

    if posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
        print("Esta posição não está válida!")
        linha = int(input("coloque a linha:"))
        coluna = int(input("coloque a coluna:"))
    else:
        if define_posicoes(linha, coluna, orientacao, tamanho):
           frota = preenche_frota(frota,nome, linha, coluna, orientacao, tamanho)
           linha = int(input("coloque a linha:"))
           coluna = int(input("coloque a coluna:"))
           i += 1

print(frota)