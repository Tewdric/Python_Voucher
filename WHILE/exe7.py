soma =0
i = 0

quantidadade = int (input("Quantas vezes voce ira adicionar valores? "))
while i < quantidadade:
    soma+= int(input("Digite um valor: "))
    i += 1
m= soma /quantidadade

print(soma)
print(m)


quantidadade = int (input("Quantas vezes voce ira adicionar valores? "))
soma_for= 0

for i in range (quantidadade):
    soma_for += int(input("Digite um valor: "))

media = soma_for/quantidadade
print(soma_for)
print(media)