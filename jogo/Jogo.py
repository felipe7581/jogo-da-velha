tabuleiro = [[0,0,0],[0,0,0],[0,0,0]]

print("\t0\t1\t2\n")
def mostrar_tabuleiro():
    for linha in range(3):
        print(linha,end=" ")
        for coluna in range(3):
            print(f"\t{tabuleiro[linha][coluna]}",end='')
        print("")

mostrar_tabuleiro()