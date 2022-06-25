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
    return matriz

#========================================================================
def caso2(n_bkp: int, matriz: list, coluna: int, linha: int):
    valor = 1
    for i in range(n_bkp):
        row = [0] * n_bkp
        matriz.append(row)
    for i in range(n_bkp):
        for j in range(n_bkp):
            matriz[i][j] = valor
            valor += 1
        
    diagonalPrincipal(matriz, n_bkp, coluna, linha)
    
#========================================================================
def diagonalPrincipal(matriz, n_bkp, coluna, linha):
    alcance = n_bkp // 4
    coluna = -4
    for tamanho in range(alcance):
        linha = -4
        coluna += 4
        for a in range(alcance):
            linha += 4
            linha_usada = linha
            coluna_usada = coluna
            for i in range(4): # Diagonais da esquerda pra direita
                valorIncluso = matriz[coluna_usada][linha_usada]
                matriz[coluna_usada][linha_usada] = (n_bkp ** 2 + 1) - valorIncluso
                coluna_usada += 1
                linha_usada += 1

        linha = n_bkp + 3
        for b in range(alcance):
            linha -= 4
            linha_usada = linha
            coluna_usada = coluna
            for i in range(4): # Diagonais da direita pra esquerda
                valorIncluso = matriz[coluna_usada][linha_usada]
                matriz[coluna_usada][linha_usada] = (n_bkp ** 2 + 1) - valorIncluso
                coluna_usada += 1
                linha_usada -= 1

    return matriz

#========================================================================
def caso3(matriz: list, n: int):
    m = 0
    resultado = 0
    while resultado != n:
        m += 1
        resultado = (2 * m + 1) + (2 * m + 1)
    resultado = resultado // 2

    for i in range(resultado):
        linhas = [0] * resultado
        matriz.append(linhas)
    
    for i in range(m+1): # m + 1 linhas com L's
        for j in range(resultado):
            matriz[i][j] = "L"

    posU = m + 1
    for i in range(resultado): # 1 linha com U's
        matriz[posU][i] = "U"
    
    for i in range(m + 2, resultado): # m - 1 linhas com X's
        for j in range(resultado):
            matriz[i][j] = "X"
    
    trocaU = (resultado // 2) # Trocar o U central pelo L acima dele
    matriz[posU][trocaU] = "L"
    matriz[trocaU][m] = "U"

    matriz2x2(matriz, resultado)
        
#========================================================================
def matriz2x2(matriz: list, resultado: int):
    resultado2 = resultado * 2
    matriz2 = []
    for i in range(resultado2):
        linhas2 = [0] * resultado2
        matriz2.append(linhas2)
    
    coluna = resultado2
    linha = resultado2
    valores = coluna * linha
    valoresFinal = valores // 4
    valorInicial = 1
    linha1 = (linha // 2) -1
    coluna1 = 0

    matriz2[coluna1][linha1 + 1] = valorInicial
    valorInicial += 1
    matriz2[coluna1 + 1][linha1] = valorInicial
    valorInicial += 1
    matriz2[coluna1 + 1][linha1 + 1] = valorInicial
    valorInicial += 1
    matriz2[coluna1][linha1] = valorInicial
    valorInicial += 1
    

    for i in range(valoresFinal -1):
        if matriz2[coluna1][linha1] != 0:
            coluna1_bkp = coluna1
            linha1_bkp = linha1
            coluna1 -= 2 # vai pra cima
            linha1 += 2 # vai pra direita
            if coluna1 < 0: # se tiver na coluna 0
                coluna1 = (coluna -2) # vai pra coluna 2
                if linha1 == linha: # se tiver no max da direita vai pra (0)
                    linha1 = 0
                    if matriz2[coluna1][linha1] == 0: # se tiver desocupado
                        analisarTipo(matriz, matriz2, valorInicial, coluna1, linha1)
                        valorInicial += 4 #c1
                    else: # se tiver ocupado
                        coluna1 = coluna1_bkp + 2
                        linha1 = linha1_bkp
                        analisarTipo(matriz, matriz2, valorInicial, coluna1, linha1)
                        valorInicial += 4 #c2
                elif matriz2[coluna1][linha1] == 0: # se tiver desocupado
                    analisarTipo(matriz, matriz2, valorInicial, coluna1, linha1) #c3
                    valorInicial += 4
                else: # se tiver ocupado
                    coluna1 = (coluna1_bkp + 2)
                    linha1 = linha1_bkp
                    analisarTipo(matriz, matriz2, valorInicial, coluna1, linha1) #c4
                    valorInicial += 4
            else: # se nao tiver na coluna 0
                if linha1 == linha: # se nao der pra ir pra direita
                    linha1 = 0
                    if matriz2[coluna1][linha1] == 0: # se tiver desocupado
                        analisarTipo(matriz, matriz2, valorInicial, coluna1, linha1) #c5
                        valorInicial += 4
                    else: # se tiver ocupado
                        coluna1 = (coluna1_bkp + 2)
                        linha1 = linha1_bkp
                        analisarTipo(matriz, matriz2, valorInicial, coluna1, linha1) #c6
                        valorInicial += 4
                else: # se der pra ir pra direita
                    if matriz2[coluna1][linha1] == 0: #se estiver desocupado
                        analisarTipo(matriz, matriz2, valorInicial, coluna1, linha1) #c7
                        valorInicial += 4
                    else: # se estiver ocupado
                        coluna1 = (coluna1_bkp + 2)
                        linha1 = linha1_bkp
                        analisarTipo(matriz, matriz2, valorInicial, coluna1, linha1) #c8
                        valorInicial += 4

    imprimir2(matriz2, resultado2)
            
#========================================================================
def analisarTipo(matriz: list, matriz2: list, valorInicial: int, coluna1: int, linha1: int):
    coluna2 = coluna1 // 2
    linha2 = linha1 // 2
    #=========================
    coluna3 = coluna1
    linha3 = linha1
    
    if matriz[coluna2][linha2] == "L":
        execTipoL(matriz2, coluna3, linha3, valorInicial)
    elif matriz[coluna2][linha2] == "U":
        execTipoU(matriz2, coluna3, linha3, valorInicial)
    else:
        execTipoX(matriz2, coluna3, linha3, valorInicial)

#========================================================================
def execTipoL(matriz2: list, coluna3: int, linha3: int, valorInicial: int):
    matriz2[coluna3][linha3 + 1] = valorInicial
    valorInicial += 1
    matriz2[coluna3 + 1][linha3] = valorInicial
    valorInicial += 1
    matriz2[coluna3 + 1][linha3 + 1] = valorInicial
    valorInicial += 1
    matriz2[coluna3][linha3] = valorInicial
    valorInicial += 1

    return matriz2
    
#========================================================================
def execTipoU(matriz2: list, coluna3: int, linha3: int, valorInicial: int):
    matriz2[coluna3][linha3] = valorInicial
    valorInicial += 1
    matriz2[coluna3 + 1][linha3] = valorInicial
    valorInicial += 1
    matriz2[coluna3 + 1][linha3 + 1] = valorInicial
    valorInicial += 1
    matriz2[coluna3][linha3 + 1] = valorInicial
    valorInicial += 1

    return matriz2

#========================================================================
def execTipoX(matriz2: list, coluna3: int, linha3: int, valorInicial: int):
    matriz2[coluna3][linha3] = valorInicial
    valorInicial += 1
    matriz2[coluna3 + 1][linha3 + 1] = valorInicial
    valorInicial += 1
    matriz2[coluna3 + 1][linha3] = valorInicial
    valorInicial += 1
    matriz2[coluna3][linha3 + 1] = valorInicial
    valorInicial += 1

    return matriz2

#========================================================================
def imprimir(matriz: list, coluna: int, linha: int):
    for i in range(coluna):
        for j in range(linha):
            print(matriz[i][j], end="\t")
        print()

#========================================================================
def imprimir2(matriz: list, resultado2):
    for i in range(resultado2):
        for j in range(resultado2):
            print(matriz[i][j], end="\t")
        print()

#========================================================================
def main():
    n = int(input())
    matriz = []
    n_bkp = n
    coluna = n_bkp
    linha = n_bkp
    if n % 2 != 0:
        casoImpar(matriz, coluna, linha)
        imprimir(matriz, coluna, linha)
    elif n % 4 == 0:
        caso2(n_bkp, matriz, coluna, linha)
        imprimir(matriz, coluna, linha)
    else:
        caso3(matriz, n)
        
            
main()
