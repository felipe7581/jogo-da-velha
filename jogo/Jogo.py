tabuleiro = [[0,0,0],[0,0,0],[0,0,0]]

print("\t0\t1\t2\n")
def mostrar_tabuleiro():
    for linha in range(3):
        print(linha,end=" ")
        for coluna in range(3):
            if tabuleiro[linha][coluna] == 0:
                print("\t~",end="")
            elif tabuleiro[linha][coluna] == 1:
                print("\tO",end="")
            elif tabuleiro[linha][coluna] == -1:
                print("\tX",end="")
        print("")

mostrar_tabuleiro()