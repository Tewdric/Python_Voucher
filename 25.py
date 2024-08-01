print("*********** CALCULADORA")
print("*********** 1 - SOMA")
print("*********** 2 - SUBTRAÇÃO")
print("*********** 3 - DIVISÃO")
print("*********** 4 - MULTIPLICAÇÃO")

opcao = int(input("Digite uma opção para utilizar:"))

if opcao == 1 :
    v1 = float(input("Digite o primeiro valor: "))
    v2 = float(input("Digite o segundo valor: "))

    soma = v1 + v2 
    print(f"A soma dos valores é de {soma}")

elif opcao == 2 :
    v1 = float(input("Digite o primeiro valor: "))
    v2 = float(input("Digite o segundo valor: "))

    sub = v1 - v2 
    print(f"A subtração dos valores é de {sub}")

elif opcao == 3 :
    v1 = float(input("Digite o primeiro valor: "))
    v2 = float(input("Digite o segundo valor: "))

    div = v1 / v2 
    print(f"A divisão dos valores é de {div}")

elif opcao == 4 :
    v1 = float(input("Digite o primeiro valor: "))
    v2 = float(input("Digite o segundo valor: "))

    mult = v1 * v2 
    print(f"A divisão dos valores é de {mult}")
else:
    print("Opção invalida!")


