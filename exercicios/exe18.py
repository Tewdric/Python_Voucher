qtd = int(input("Digite a quantidade numero que deseja:"))
i = 0
lista =[]

while i < qtd:
    num = int(input("Digite um numero: "))
    lista.append(num)
    i+=1 

print(f"Sua lista => {lista}")
print(f"Maior núnero da lista => {max(lista)}")