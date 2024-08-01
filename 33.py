hot_dog = 12.00
x_salada = 18.50
x_bacon = 25.50
x_burguer = 17.00
suco = 9.50
refri = 10

opcao = int (input("Digite o codigo do produto desejado: "))
quant = int(input("Digite a quantidade desejada: "))

if opcao == 100:
    valor = hot_dog * quant
    print(f"O valor a ser pago será de : R${valor:.2f}")
elif opcao == 102:
    valor = x_salada * quant
    print(f"O valor a ser pago será de : R${valor:.2f}")
elif opcao == 103:
    valor = x_bacon * quant
    print(f"O valor a ser pago será de : R${valor:.2f}")
elif opcao == 104:
    valor = x_burguer * quant
    print(f"O valor a ser pago será de : R${valor:.2f}")
elif opcao == 105:
    valor = suco * quant
    print(f"O valor a ser pago será de : R${valor:.2f}")
elif opcao == 106:
    valor = refri * quant
    print(f"O valor a ser pago será de : R${valor:.2f}")
else:
    print("Codigo invalido!")

