n1 = int(input("Digite o primeiro numero "))
n2 = int(input("Digite o segundo numero "))

if n1>n2:
    resto = n1 - n2 
    print(f"O primeiro número é maior que o segundo!")
    print(f'A diferença entre os dois numero é de: {resto}')
elif n2>n1:
    resto = n2 - n1 
    print(f"O segundo número é maior que o primeiro!")
    print(f'A diferença entre os dois numero é de: {resto}')
else:
    print(f"Os numeros são iguais")