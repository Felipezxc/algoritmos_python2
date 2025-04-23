class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        return self.idade

    def engordar(self, quilos):
        self.peso += quilos
        return self.peso

    def emagrecer(self, quilos_perdidos):
        self.peso -= quilos_perdidos
        return self.peso

    def crescer(self, anos):
        if self.idade < 21:
            self.altura += (0.05) * anos
        return self.altura

Jose = Pessoa('Jose', 19, 68, 1.76)

print(Jose.__dict__)
print(f"nome: {Jose.nome}, idade: {Jose.idade}, peso: {Jose.peso} altura: {Jose.altura:.2f} metros.")

Jose.envelhecer(1)
Jose.crescer(2)
Jose.engordar(10)

print(Jose.__dict__)
print(f"nome: {Jose.nome}, idade: {Jose.idade}, peso: {Jose.peso}, altura:  {Jose.altura:.2f} metros.")

Jose.emagrecer(5)

print(Jose.__dict__)
print(f"nome: {Jose.nome}, idade: {Jose.idade}, peso: {Jose.peso} altura: {Jose.altura:.2f} metros.")