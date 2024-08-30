i = 0
soma = []

while i < 5:
    i+=1
    n = int(input("Digite um numero natural:  "))
    if n >= 0:
        soma.append(n)

print(soma)
print(sum(soma))