
num = int(input("Digite um numero entre 100 a 9999:"))

if num < 100 or num > 9999:
    print("Numero invalisdo!")
    num = int(input("Digite um numero entre 100 a 9999:"))
    lista = str (num)
else:
    lista = str (num)

soma = ''
for i in range(len(lista)):
    soma = lista[i]
    print(soma)
    i += 1