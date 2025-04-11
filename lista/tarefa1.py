lista = []

for i in range(5):
    numero = int(input(f"Digite o número {i + 1}: "))
    lista.append(numero)

print("Os números digitados foram:")
for numero in lista:
    print(numero)