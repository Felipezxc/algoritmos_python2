while True:

    nota = float(input("Digite a nota (entre 0 e 10): "))

    if 0 <= nota <= 10:
        print("Nota ok")
        break
    else:
        print("Nota inválida.")


