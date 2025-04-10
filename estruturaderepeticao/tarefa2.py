while True:

    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == senha:
        print("Senha inválida.")
    else:
        print("Login aceito")
        break