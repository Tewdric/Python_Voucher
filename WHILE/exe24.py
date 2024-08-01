i = 0
tabela = []
while i < 1000:
    i+=1
    if i % 3 == 0:
        tabela.append(i)
    if i % 5 == 0:
        tabela.append(i)
soma = sum(tabela)

print(soma)