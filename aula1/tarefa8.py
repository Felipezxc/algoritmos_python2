# Solicitar informações ao usuário
valor_por_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcular o salário total
salario_total = valor_por_hora * horas_trabalhadas

# Exibir o resultado
print(f"O total do seu salário no referido mês é: R${salario_total:.2f}")