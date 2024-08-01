a = int (input("Digite o numero fatorial: "))
lista = []
pp = []
i = a
fatorial = 0
soma = 0
while i > 0:
    i-=1
    fatorial = a * i
    soma = fatorial * (i-1)

    print(soma)
    pp.append(soma)
    lista.append(f"{i}X")

lista.pop()
lista.insert(0,f"{a}!")
print(f"{a}!={lista} = {pp[0]}")
    