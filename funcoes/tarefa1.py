def imprimir_padrao(n):
    for x in range(1, n+1):
        for y in range(1, x+1):
            print(x, end='')
        print()

n = int(input("Digite um número inteiro: "))
imprimir_padrao(n)