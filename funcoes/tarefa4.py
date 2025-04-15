def num(x):
    if x > 0:
        valor = 'P'
    elif x < 0:
        valor = 'N'
    else:
        valor = 'O'
    return valor

resultado = num(10)
print(f"O valor retornado é: {resultado}")