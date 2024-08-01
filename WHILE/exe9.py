i = 0
soma = []

while i < 3:
    valor= int(input("Digite um valor: "))
    i += 1
    soma.append(valor)

print("Menor numero da lista: ",min(soma))
print("Maio numero da lista: ",max(soma))

soma1 = []

for i in range (3):
    valor= int(input("Digite um valor: "))
    i += 1
    soma1.append(valor)

print("Menor numero da lista: ",min(soma1))
print("Maio numero da lista: ",max(soma1))