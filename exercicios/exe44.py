
sair = True
while sair:
    print("\n======MENU=======")
    print("1 - ADIÇÂO")
    print("2 - SUBTRAÇÃO")
    print("3 - MULTIPLICAÇÃO")
    print("4 - DIVISÃO")
    print("5 - SAIR")
    option = int(input())
    
    match option:
        case 1:
            n1 = int(input())
            n2 = int(input())
            
            soma = n1+n2
            print("Resultado",soma)
        case 2:
            n1 = int(input())
            n2 = int(input())
            
            sub = n1-n2
            print("Resultado",sub)
        case 3:
            n1 = int(input())
            n2 = int(input())
            
            mul = n1*n2
            print("Resultado",mul)
        case 4:
            n1 = int(input())
            n2 = int(input())
            
            if n2 == 0:
                print("Não se pode dividir por zero")
            else:
                div = n1/n2
                
            print("Resultado",mul)
        case 5:
            print("Até a próxima!")
            sair = False
        case _:
            print("Opção invalida")
            