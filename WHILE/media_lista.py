n_v = int (input("O numero de provas: "))

i = 0
notas = []

while i < n_v:
    notas.append(float(input("Digite a nota: ")))
    i += 1


media = sum(notas)/len(notas)
print(media)