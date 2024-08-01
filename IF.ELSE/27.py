n1 = float (input("Digite um lado: "))
n2 = float (input("Digite outro lado: "))
n3 = float (input("Digite outro lado: "))


if n1 == n2 == n3 :
    print("Triangulo equilatero!")
elif n1 == n2 or n2 == n3 or n1 == n3 :
    print("Triangulo isoceles!")
elif n1 != n2 != n3:
    print("Triangulo escaleno")
else:
    print("Não é triangulo")