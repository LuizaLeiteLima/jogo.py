from funcoes import * 



frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}  


for nome in frota.keys():
    if nome == 'porta-aviões':
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho4")
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        orientação = int(input('[1] Vertical [2] Horizontal >'))

    elif nome == 'navio-tanque':
        for e in range(2):
            print(f'Insira as informações referentes ao navio {nome} que possui tamanho 3')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            orientação = int(input('[1] Vertical [2] Horizontal >'))

    elif nome == 'contratorpedeiro':
        for e in range(3):
            print(f'Insira as informações referentes ao navio {nome} que possui tamanho 2')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            orientação = int(input('[1] Vertical [2] Horizontal >'))
    elif nome == 'submarino':
        for e in range(4):
            print(f'Insira as informações referentes ao navio {nome} que possui tamanho 1')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
        orientação = 1
    elif posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
        print("Esta posição não está válida!")
        linha = int(input("coloque a linha:"))
        coluna = int(input("coloque a coluna:"))
    else:
        if define_posicoes(linha, coluna, orientacao, tamanho):
           frota = preenche_frota(frota,nome, linha, coluna, orientacao, tamanho)
           linha = int(input("coloque a linha:"))
           coluna = int(input("coloque a coluna:"))
           
           
print(frota)