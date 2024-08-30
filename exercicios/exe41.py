print("Digite 0 no R2 para sair")
while True:
    try:
        r1 = int(input("Digite R1: \n"))
        r2 = int(input("Digite R2: \n"))
        
        if r1 == 0 or r2 == 0:
            print("Até a próxima!")
            break
        else:
            r = (r1*r2)/(r1+r2)

        
    except (ValueError, TypeError):
        print("O valores não aceitam String, digite novamente!")
    except ZeroDivisionError:
        print("Os campos não podem ser zero")
    else:
        print(f'O resultado é {r:.2f}')
    