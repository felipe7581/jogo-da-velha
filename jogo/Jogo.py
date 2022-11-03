import random as gerador
tabuleiro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def mostrar_tabuleiro():    # função que vai exibir o tabuleiro na tela
    print()
    print("\t0\t1\t2\n")
    for linha in range(3):
        print(linha, end=" ")
        for coluna in range(3):
            if tabuleiro[linha][coluna] == 0:
                print("\t~", end="")
            elif tabuleiro[linha][coluna] == 1:
                print("\tO", end="")
            elif tabuleiro[linha][coluna] == -1:
                print("\tX", end="")
        print("")


def checa_tabuleiro():      # função que checa o tabuleiro
    # primeiro checa as 3 linhas, se a somatoria dos valores seja igual a 3 ou -3 então
    # significa que as linhas foram preenchidas por um dos simbolos "x" ou "O"
    if (tabuleiro[0][0] + tabuleiro[0][1] + tabuleiro[0][2] == 3 or
            tabuleiro[1][0] + tabuleiro[1][1] + tabuleiro[1][2] == 3 or
            tabuleiro[2][0] + tabuleiro[2][1] + tabuleiro[2][2] == 3):
        return 1
    if (tabuleiro[0][0] + tabuleiro[0][1] + tabuleiro[0][2] == -3 or
            tabuleiro[1][0] + tabuleiro[1][1] + tabuleiro[1][2] == -3 or
            tabuleiro[2][0] + tabuleiro[2][1] + tabuleiro[2][2] == -3):
        return -1

    # agora checaremos as colunas, seguindo a mesma logica das checagem de linhas
    if (tabuleiro[0][0] + tabuleiro[1][0] + tabuleiro[2][0] == 3 or
            tabuleiro[0][1] + tabuleiro[1][1] + tabuleiro[2][1] == 3 or
            tabuleiro[0][2] + tabuleiro[1][2] + tabuleiro[2][2] == 3):
        return 1
    if (tabuleiro[0][0] + tabuleiro[1][0] + tabuleiro[2][0] == -3 or
            tabuleiro[0][1] + tabuleiro[1][1] + tabuleiro[2][1] == -3 or
            tabuleiro[0][2] + tabuleiro[1][2] + tabuleiro[2][2] == -3):
        return -1

    # agora checaremos as diagonais ainda repetindo a logica
    if (tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2] == 3 or
            tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[0][2] == 3 ):
        return 1
    if (tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2] == -3 or
            tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[0][2] == -3 ):
        return -1

    return 0


def jogada_computador():
    linha = gerador.randrange(3)
    coluna = gerador.randrange(3)

    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = 1
    else:
        while tabuleiro[linha][coluna] != 0:
            linha = gerador.randrange(3)
            coluna = gerador.randrange(3)
        tabuleiro[linha][coluna] = 1 


def jogada_humano():
    linha = int(input("linha que deseja jogar: "))
    coluna = int(input("Coluna que deseja jogar: "))

    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = -1
    else:
        while tabuleiro[linha][coluna] != 0:
            print("Jogada invalida!")
            linha = int(input("linha que deseja jogar: "))
            coluna = int(input("Coluna que deseja jogar: "))
        tabuleiro[linha][coluna] = -1


def jogar():
    vez = 1
    while checa_tabuleiro() == 0:
        mostrar_tabuleiro()
        if vez == 1:
            print("vez da maquina")
            jogada_computador()
            vez = -1
        else:
            print("vez do jogador")
            jogada_humano()

            vez = 1


        if verifica_empate() == 1:
            break


def verifica_empate():
    soma = 0
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == 0:
                return 0
            else:
                soma += 1
    if soma == 9:
        return 1


jogar()
