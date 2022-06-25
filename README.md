# EP-2-MATRIZES
Exercício programa 2 - MATRIZES - PYTHON

Código completo!
25/06

Caso 1 - Completo
Caso 2 - Completo
Caso 3 - Completo


1 Matriz Constante
Uma Matriz Constante ´e uma matriz quadrada de ordem n ≥ 3, preenchida com os valores
1, 2, . . . , n2, tal que a soma dos elementos em cada linha, coluna, diagonal principal e diagonal
secundária, possui o mesmo valor. Este valor é chamado de constante da matriz. Por exemplo,
8 1 6
3 5 7
4 9 2
é uma matriz constante de ordem n = 3 e sua constante ´e 15.
2 Gerando Matrizes Constantes
Para gerar uma matriz constante de ordem n ≥ 3 separamos em trˆes casos: quando n ´e ´ımpar;
quando n = 4m para algum m ≥ 1; e para n = 4m + 2 para algum m ≥ 1.
2.1 Caso 1: n ´ımpar
Este m´etodo come¸ca colocando o valor 1 na posi¸c˜ao que est´a no meio da primeira linha. Por
exemplo, para n = 3, ter´ıamos:
1
A partir desta posi¸c˜ao, a ideia ´e ir caminhando sempre para cima e para a direita, preenchendo
os quadrados com os inteiros 2, 3, . . . , n2
, nesta ordem. Se vocˆe andar para cima e cair para fora
da matriz, vocˆe ´e jogado para a ´ultima linha; se vocˆe andar para a direita e cair para fora da
matriz, vocˆe ´e jogado para a primeira coluna. Continuando o exemplo, ao andarmos para cima
e para a direita, cairemos em uma posi¸c˜ao que est´a fora dos limites da matriz, nos levando a
preencher a terceira coluna da ´ultima linha:
1
2
1
Universidade Federal de Mato Grosso do Sul
Faculdade de Computa¸c˜ao
Algoritmos e Programa¸c˜ao I - Prof. Carlos Higa
Seguindo para cima e para a direita, cairemos para fora tamb´em. Logo o pr´oximo passo ´e colocar
o 3 na segunda linha e primeira coluna:
1
3
2
Continuando a partir do quadrado onde est´a o 3, se andarmos para cima e para a direita
veremos que o pr´oximo quadrado j´a est´a ocupado pelo 1. Sempre que o pr´oximo quadrado
estiver ocupado, vocˆe anda apenas para baixo:
1
3
4 2
Agora ´e s´o continuar com o mesmo racioc´ınio:
1
3 5
4 2
1 6
3 5
4 2
1 6
3 5 7
4 2
8 1 6
3 5 7
4 2
8 1 6
3 5 7
4 9 2
Note que ap´os colocar o 6 na matriz, tentamos camimhar para cima e para a direita, caindo
para fora da matriz, tanto na parte de cima quanto na parte da direita. Neste caso, tentaremos
colocar o 7 na ´ultima linha e primera coluna; mas como esta posi¸c˜ao est´a ocupada pelo 4,
caminhamos apenas para baixo.
2.2 Caso 2: n = 4m para m ≥ 1
Neste caso iremos construir matrizes constantes para n m´ultiplo de 4, ou seja, 4, 8, 12, 16, . . ..
Vamos utilizar um exemplo com n = 8. O primeiro passo ´e preencher a matriz com os n´umeros
1, 2, . . . , n2
, da esquerda para a direita e de cima para baixo:
2
Universidade Federal de Mato Grosso do Sul
Faculdade de Computa¸c˜ao
Algoritmos e Programa¸c˜ao I - Prof. Carlos Higa
1 2 3 4 5 6 7 8
9 10 11 12 13 14 15 16
17 18 19 20 21 22 23 24
25 26 27 28 29 30 31 32
33 34 35 36 37 38 39 40
41 42 43 44 45 46 47 48
49 50 51 52 53 54 55 56
57 58 59 60 61 62 63 64
O passo seguinte ´e dividir esta matriz em submatrizes de tamanho 4 × 4, fazendo um X no
meio de cada uma para marcar a diagonal principal e secund´aria:
1 2 3 4 5 6 7 8
9 10 11 12 13 14 15 16
17 18 19 20 21 22 23 24
25 26 27 28 29 30 31 32
33 34 35 36 37 38 39 40
41 42 43 44 45 46 47 48
49 50 51 52 53 54 55 56
57 58 59 60 61 62 63 64
O pr´oximo passo ´e substituir cada elemento ai,j nas diagonais pelo valor (n
2 + 1) − ai,j . Por
exemplo, o elemento a0,0 que vale 1 deve ser substituido por (82 + 1) − 1 = 64. Fazendo isso
para todos os quadrados coloridos temos:
3
Universidade Federal de Mato Grosso do Sul
Faculdade de Computa¸c˜ao
Algoritmos e Programa¸c˜ao I - Prof. Carlos Higa
64 2 3 61 60 6 7 57
9 55 54 12 13 51 50 16
17 47 46 20 21 43 42 24
40 26 27 37 36 30 31 33
32 34 35 29 28 38 39 25
41 23 22 44 45 19 18 48
49 15 14 52 53 11 10 56
8 58 59 5 4 62 63 1
A matriz acima ´e uma matriz constante de ordem 8 e o sua constante ´e 260. Confira!
2.3 Caso 3: n = 4m + 2 para m ≥ 1
Aqui iremos construir matrizes constantes de ordem n = 4m + 2, onde m ≥ 1, ou seja, n =
6, 10, 14, . . .. Para exemplificar, iremos usar n = 10, ou seja, m = 2.
O primeiro passo ´e criar uma matriz auxiliar de tamanho (2m + 1) × (2m + 1) e preenche-la
da seguinte maneira:
• m + 1 linhas com L’s;
• 1 linha com U’s;
• m − 1 linhas com X’s;
• Trocar o U central pelo L acima dele.
No nosso caso ter´ıamos uma matriz assim:
L L L L L
L L L L L
L L U L L
U U L U U
X X X X X
4
Universidade Federal de Mato Grosso do Sul
Faculdade de Computa¸c˜ao
Algoritmos e Programa¸c˜ao I - Prof. Carlos Higa
Cada letra na matriz acima corresponde a uma submatriz 2 × 2 na matriz final. Por exemplo,
o L na matriz em vermelho corresponde `a submatriz em vermelho na matriz final abaixo:
Cada letra (L, U ou X), indica a ordem como devemos preencher a submatriz 2 × 2:
L
1
2 3
4
U
4
2 3
1
X
4
3 2
1
A primeira submatriz a ser preenchida ´e a submatriz em vermelho da figura anterior. Devemos preencher de acordo com a ordem indicada pela letra L:
5
Universidade Federal de Mato Grosso do Sul
Faculdade de Computa¸c˜ao
Algoritmos e Programa¸c˜ao I - Prof. Carlos Higa
4 1
2 3
Agora iremos caminhar na matriz da mesma maneira que caminhamos no m´etodo Siamese,
sempre preenchendo a submatriz de acordo com a ordem indicada pela respectiva letra. Sendo
assim, a pr´oxima submatriz a ser preenchida ´e a submatriz correspondente ao X em verde abaixo:
L L L L L
L L L L L
L L U L L
U U L U U
X X X X X
Sendo assim, temos na matriz final:
6
Universidade Federal de Mato Grosso do Sul
Faculdade de Computa¸c˜ao
Algoritmos e Programa¸c˜ao I - Prof. Carlos Higa
4 1
2 3
5 8
7 6
Caminhando para cima e para a direita teremos:
4 1
2 3
9 12
10 11
5 8
7 6
7
Universidade Federal de Mato Grosso do Sul
Faculdade de Computa¸c˜ao
Algoritmos e Programa¸c˜ao I - Prof. Carlos Higa
Seguindo este algoritmo, a matriz final dever´a ser:
68 65 96 93 4 1 32 29 60 57
66 67 94 95 2 3 30 31 58 59
92 89 20 17 28 25 56 53 64 61
90 91 18 19 26 27 54 55 62 63
16 13 24 21 49 52 80 77 88 85
14 15 22 23 50 51 78 79 86 87
37 40 45 48 76 73 81 84 9 12
38 39 46 47 74 75 82 83 10 11
41 44 69 72 97 100 5 8 33 36
43 42 71 70 99 98 7 6 35 34
A matriz acima ´e uma matriz constante de ordem n = 10 e sua constante ´e 505.
3 Implementa¸c˜ao
Vocˆe dever´a escrever um programa em linguagem Python 3 que recebe como entrada um inteiro
n, onde 3 ≤ n ≤ 100, e imprime como sa´ıda uma matriz constante de ordem n.
3.1 Exemplo de entrada
A entrada consiste de um inteiro n, tal que 3 ≤ n ≤ 100. Por exemplo:
4
8
Universidade Federal de Mato Grosso do Sul
Faculdade de Computa¸c˜ao
Algoritmos e Programa¸c˜ao I - Prof. Carlos Higa
3.2 Exemplo de sa´ıda
A sa´ıda consiste em imprimir uma matriz constante de ordem n, dado como entrada. Observe
que ap´os cada n´umero existe uma tabula¸c˜ao, e n˜ao um espa¸co em branco:
Caso 2:
16 2 3 13
5 11 10 8
9 7 6 12
4 14 15 1
4 Entrega
Instru¸c˜oes para entrega do seu trabalho:
1. Forma de entrega
A entrega ser´a realizada diretamente no site do AVA. Vocˆe pode entregar o seu c´odigo
quantas vezes quiser at´e `as 23 horas e 59 minutos do dia 28 de junho de 2022. A
´ultima vers˜ao entregue ´e aquela que ser´a corrigida. Encerrado o prazo, o arquivo n˜ao ser´a
mais aceito.
2. Atrasos
Trabalhos atrasados n˜ao ser˜ao aceitos. N˜ao deixe para entregar seu trabalho na ´ultima
hora. Para prevenir imprevistos como queda de energia, problemas com o sistema, falha
de conex˜ao com a internet, sugiro que a entrega do exerc´ıcio seja feita pelo menos um dia
antes do prazo determinado.
9
Universidade Federal de Mato Grosso do Sul
Faculdade de Computa¸c˜ao
Algoritmos e Programa¸c˜ao I - Prof. Carlos Higa
3. O que entregar?
Vocˆe deve entregar um ´unico arquivo contendo apenas o seu programa fonte cujo nome
deve ser, seunome_ultimonome.py. Por exemplo, no meu caso seria carlos_higa.py.
Nao˜ entregue qualquer outro arquivo.
4. Verifica¸c˜ao dos dados de entrada
N˜ao se preocupe com a verifica¸c˜ao dos dados de entrada do seu programa. Seu programa
n˜ao precisa fazer consistˆencia dos dados de entrada. Isto significa que o usu´ario n˜ao ir´a
digitar um n < 3, por exemplo.
5. Conduta ´etica
A atividade deve ser feita individualmente. Cada estudante tem responsabilidade sobre
c´opias de seu c´odigo fonte, mesmo que parciais. N˜ao fa¸ca o exerc´ıcio em grupo e n˜ao
compartilhe seu programa ou trechos do seu programa. Vocˆe pode consultar seus colegas
para esclarecer d´uvidas e discutir ideias sobre o trabalho, mas nao˜ copie o programa!
Em caso de pl´agio, os envolvidos receber˜ao nota zero na media dos exerc ´ ´ıcios, ou seja,
ME = 0 no c´alculo da m´edia de aproveitamento.
