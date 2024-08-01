base = int(input("Digite a base X da potencia: "))
expoente = int(input("Digite o expoente Y da potencia: "))

sub = expoente -1
lista = []
potencia = 0

i= 0
while i < sub:
    i+= 1

    potencia+= base*base
    print(potencia)
    lista.append(f"{base} X"*1)
lista.reverse()
print(f"{base}^{expoente} = {lista} = RESULTADO {potencia}")