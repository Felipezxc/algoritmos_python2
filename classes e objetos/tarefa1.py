class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocar_cor(self, nova_cor):
        self.cor = nova_cor

    def mostrar_cor(self):
        return self.cor

bola_futebol = Bola("Branca", 70, "Couro")
print(f"A cor da bola é: {bola_futebol.mostrar_cor()}")
bola_futebol.trocar_cor("Preta")
print(f"A nova cor da bola é: {bola_futebol.mostrar_cor()}")