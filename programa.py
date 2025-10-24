from funcoes import * 

linha = int(input("coloque a linha:"))
coluna = int(input("coloque a coluna:"))
orientacao = int(input("coloque a orientação:"))


frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}  
tamanho = 1
if orientacao == 1:
    orientacao == 'vertical'

else:
    orientacao == 'horizontal' 

i = 0

for nome in frota.keys():
    print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho} ")

    if posicao_valida == False:
        print("Esta posição não está válida!")
        linha = int(input("coloque a linha:"))
        coluna = int(input("coloque a coluna:"))
    if posicao_valida == True:
        if define_posicoes(linha, coluna, orientacao, tamanho):
           frota[nome] = preenche_frota(frota,nome, linha, coluna, orientacao, tamanho).append(define_posicoes(linha, coluna, orientacao, tamanho))
           linha = int(input("coloque a linha:"))
           coluna = int(input("coloque a coluna:"))
           i += 1
           tamanho += 1
    print(frota)