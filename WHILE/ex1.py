n_v = int (input("O numero de provas: "))

i = 0
soma = 0

while i < n_v:
    soma += float(input("Digite a nota: "))
    i += 1

m = soma / n_v

print(m)