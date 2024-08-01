i = 0
soma = []

while i < 3:
    valor= int(input("Digite um valor: "))
    i += 1
    if valor > 0:
        soma.append(valor)

print(sum(soma))

soma1 = []
for i in range (3):
    valor= int(input("Digite um valor: "))
    i += 1
    if valor > 0:
        soma1.append(valor)
        
print(sum(soma1))
