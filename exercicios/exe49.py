sair = True

print("Digite 0 para sair!")

soma = 0
lista = []
listaPares = []
digitados = 0

while sair:
    num = int(input("Digite um numero: "))
    lista.append(num)
    soma += num
    digitados +=1
    if num % 2 == 0:
        listaPares.append(num)
    if num == 0:
        sair = False
        
lista.pop()
media = sum(lista)/len(lista)
maior = max(lista)
menor = min(lista)

mediasPares = sum(listaPares)/len(listaPares)

print(f"Soma dos numero digitados: {soma}")
print(f"A quantidade de numeos digitados: {digitados}")
print(f"A media de numeros digitados: {media}")
print(f"O maior numero digitado: {maior}")
print(f"O menor numero digitado: {menor}")
print(f"Media dos numeros pares da lista: {mediasPares}")
