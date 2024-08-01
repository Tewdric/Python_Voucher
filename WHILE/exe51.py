jose = 0
joao = 0
maria = 0
mario = 0
nulo = 0
branco = 0

sair = True

lista = []
print("Digite 0 para sair!")

while sair == True:
    print("1 - José")
    print("2 - João")
    print("3 - Maria")
    print("4 - Mario")
    print("5 - Voto Nulo")
    print("6 - Voto em Branco\n")
    
    option = int(input())
    
    match option:
        case 1:
            if option == 1:
                jose+=1
        case 2:
            if option == 2:
                joao +=1
        case 3:
            if option == 3:
                maria +=1
        case 4:
            if option == 4:
                mario +=1
        case 5:
            if option == 5:
                nulo += 1
        case 6:
            if option == 6:
                branco+=1
        case 0:
            sair = False
        case _:
            print("Digite uma opção!")


soma = jose+joao+maria+mario+nulo+branco

print(f"O total de votos foram: {soma}")
print(f"Total de votos para José :{jose}")
print(f"Total de votos para João :{joao}")
print(f"Total de votos para Maria :{maria}")
print(f"Total de votos para Mario :{mario}")
print(f"Total de votos Nulos :{nulo}")
print(f"Total de votos em Brancos :{branco}")

