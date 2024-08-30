i = 1
lista = []

nome = input("Nome do atleta: ")
while i < 7:
    
    nota = float(input("Digite a nota: "))
    lista.append(nota)
    i+=1


lista.sort()
lista.pop()
del(lista[0])

media = sum(lista)/len(lista)

print("\nResultado final:\n ")
print(f"Atleta: {nome}")
print(f"Melhor nota: {max(lista)}")
print(f"Pior nota: {min(lista)}")
print(f"Media: {media}")
