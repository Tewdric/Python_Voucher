print("*********** CALCULADORA")
print("*********** 1 - SOMA")
print("*********** 2 - DIFERENÇA ENTRE DOIS NUMEROS")
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

    if v1>v2:
        sub = v1 - v2
        print(f"O resultado é {sub}")
    else:
        sub = v2 - v1
        print(f"O resultado é {sub}")

elif opcao == 3 :
    v1 = float(input("Digite o primeiro valor: "))
    v2 = float(input("Digite o segundo valor: "))

    mult = v1 * v2 
    
    print(f"A divisão dos valores é de {mult}")

elif opcao == 4 :
    v1 = float(input("Digite divisorr: "))
    v2 = float(input("Digite o denominador: "))

    div = v1 / v2 
    print(f"A divisão dos valores é de {div}")
    
    if v2 == 0:  
        print("O denominador não pode ser igual a zero")

else:
    print("Opção invalida!")
