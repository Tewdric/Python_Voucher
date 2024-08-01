km = float(input("Digite a distancia percorrida: "))
litros = float(input("Digite a quantidade de litros de gasolina gastos no percusso: "))

media = km/litros

if media <8:
    print("Venda o carro!")
elif media >= 8 and media <= 8:
    print("Economico!")
else:
    print("Super economico!")