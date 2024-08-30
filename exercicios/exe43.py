
soma = 0
while True:
    numero = 10
    
    option = int(input("Tenta acertar o numero: "))
    
    if option < numero:
        sub = numero - option
        print(f"Ainda não, esta quase lá, diferença de {sub}")
        soma += 1
    elif option > numero:
        sub = numero - option
        print(f"Ainda não, esta quase lá, diferença de {sub}")
        soma += 1
    
    if option == numero:
        print(f"Numero de tentativas {soma}")
        print("Até a proxima!")
        break