print("Lata de 18L curstam em média R$80,00")
print("Galão de 3,6L curstam em média R$25,00")

metros = float(input("Digite os metros a serem pintados: "))

dilui = metros / 6

if dilui <= 21:
    print("Compre apenas galões de 3,6L")

elif dilui >= 108:
    print("Compre apenas um galão de 18L")

else:
    print("Misturar latas e galões, de forma que o preço seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.")
