def imprimir_num(n):
    for x in range(1,n+1):
        print(x , end ='\n')
        if x == n:
            break
        else:
            for y in range(1,n+1):
                if x >= y:
                    print(y, end='')

imprimir_num(9)