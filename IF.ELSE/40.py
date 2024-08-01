salario_hora = float(input("Digite o salario ganho por hora. "))
hora_trabalhada = int(input("Digite a quantidade de horas que trabalhou esse mes: "))

salario_bruto = salario_hora*hora_trabalhada

imposto = (salario_bruto*0.11)
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05

salario_liquido = salario_bruto - imposto -inss -sindicato

print(f"Salário Bruto R${salario_bruto:.2f}")
print(f"Imposto de Renda R${imposto:.2f}")
print(f"INSS R${inss:.2f}")
print(f"Sindicato R${sindicato:.2f}")
print(f"Salário Liquido R${salario_liquido:.2f}")


