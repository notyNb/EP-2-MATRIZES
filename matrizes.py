def casoImpar(matriz: list, coluna: int, linha: int):
    for i in range(coluna):
        linhas = [0] * linha
        matriz.append(linhas)
    
    valores = coluna * linha
    valor_inicial = 2
    linha1 = linha // 2 
    coluna1 = 0
    matriz[coluna1][linha1] = 1
        
    for i in range(1, valores):
        if matriz[coluna1][linha1] != 0:
            coluna1_bkp = coluna1
            linha1_bkp = linha1
            coluna1 -= 1 # vai pra cima
            linha1 += 1 # vai pra direita
            if coluna1 < 0: # se tiver na coluna 0
                coluna1 = (coluna -1) # vai pra coluna 2
                if linha1 == linha: # se tiver no max da direita vai pra (0)
                    linha1 = 0
                    if matriz[coluna1][linha1] == 0: # se tiver desocupado
                        matriz[coluna1][linha1] = valor_inicial #c1
                        valor_inicial += 1
                    else: # se tiver ocupado
                        matriz[coluna1_bkp + 1][linha1_bkp] = valor_inicial #c2
                        coluna1 = (coluna1_bkp + 1)
                        linha1 = linha1_bkp
                        valor_inicial += 1
                elif matriz[coluna1][linha1] == 0: # se tiver desocupado
                    matriz[coluna1][linha1] = valor_inicial #c3
                    valor_inicial += 1
                else: # se tiver ocupado
                    matriz[coluna1_bkp+1][linha1_bkp] = valor_inicial #c4
                    coluna1 = (coluna1_bkp + 1)
                    linha1 = linha1_bkp
                    valor_inicial += 1
            else: # se nao tiver na coluna 0
                if linha1 == linha: # se nao der pra ir pra direita
                    linha1 = 0
                    if matriz[coluna1][linha1] == 0: # se tiver desocupado
                        matriz[coluna1][linha1] = valor_inicial #c5
                        valor_inicial += 1
                    else: # se tiver ocupado
                        matriz[coluna1_bkp + 1][linha1_bkp] = valor_inicial #c6
                        coluna1 = (coluna1_bkp + 1)
                        linha1 = linha1_bkp
                else: # se der pra ir pra direita
                    if matriz[coluna1][linha1] == 0: #se estiver desocupado
                        matriz[coluna1][linha1] = valor_inicial #c7
                        valor_inicial += 1
                    else: # se estiver ocupado
                        matriz[coluna1_bkp + 1][linha1_bkp] = valor_inicial #c8
                        valor_inicial += 1
                        coluna1 = (coluna1_bkp + 1)
                        linha1 = linha1_bkp
    imprimir(matriz, coluna, linha)
#========================================================================
def imprimir(matriz: list, coluna: int, linha: int):
    for i in range(coluna):
        for j in range(linha):
            print(matriz[i][j], end="\t")
        print()
#========================================================================
def caso2p2(n_bkp: int, matriz: list, coluna: int, linha: int):
    valor = 1
    for i in range(n_bkp):
        row = [0] * n_bkp
        matriz.append(row)
    for i in range(n_bkp):
        for j in range(n_bkp):
            matriz[i][j] = valor
            valor += 1
    diagonalPrincipal(matriz, n_bkp, coluna, linha)
    
#================================
def diagonalPrincipal(matriz, n_bkp, coluna, linha):
    coluna = 0
    linha = 0
    valorIncluso = 1
    for i in range(n_bkp): # Diagonal da esquerda pra direita
        matriz[coluna][linha] = (n_bkp ** 2 + 1) - valorIncluso
        coluna += 1
        linha += 1
        valorIncluso += 9

    coluna = 0
    linha = n_bkp - 1
    valorIncluso = 8
    for i in range(n_bkp): # Diagonal da direita pra esquerda
        matriz[coluna][linha] = (n_bkp ** 2 + 1) - valorIncluso
        coluna += 1
        linha -= 1
        valorIncluso += 7

    return matriz

#=======================================================================

#========================================================================
def main():
    n = int(input())
    matriz = []
    n_bkp = n
    coluna = n_bkp
    linha = n_bkp
    if n % 2 != 0:
        casoImpar(matriz, coluna, linha)
    elif n % 4 == 0:
        caso2p2(n_bkp, matriz, coluna, linha)
        imprimir(matriz, coluna, linha)
    
main()
