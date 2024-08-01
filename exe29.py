numero = int(input("Digite um numero: "))

i = 10
sobras = []

while i > 0:
    m = numero/i
    print(numero,i,"=", m)
    if m % i == 0:
        sobras.append(i)
    i-=1

print(sobras)