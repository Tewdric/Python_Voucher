intervalo = int(input("Digite um intervalo de impressão: "))
maximo = int(input("Digite o limite de impresão: "))

i = 0

while i < maximo:

    i+= 1 + intervalo
    if i % 2 == 1:
        print(i)
