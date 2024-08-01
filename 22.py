dia = int(input("Que dia da semana estamos?\n1 - Para Domingo\n2 - Para Segunda-Feira\n3 - Para Terça-feira\n3 - Para Quarta-Feira\n5 - Para Quinta-Feira\n6 - Para Sexta-Feira\n7 - Para Sabado"))

if dia == 1:
    print("Domingo, quero te encontrar, e te abraçar.. ♫")
elif dia == 2:
    print("Segunda, I don't like")
elif dia == 3:
    print("Terça...")
elif dia == 4:
    print("Quarta, usamos rosa")
elif dia == 5:
    print("Quinta, ta quase")

    s = str(input("É solteiro?"))

    if s == 'sim':
        print("Já pode sair")
    else:
        print("Vai pra casa")
elif dia == 6:
    print("SEXTOU, ta quase")
    s = str(input("É solteiro?"))

    if s == 'sim':
        print("Já pode sair")
    else:
        print("APARENTEMENTE, NÃO PODE SAIR NÃO ")

elif dia == 7:
    print("Sabado, ta quase")

else:
    print("Numero invalido!")