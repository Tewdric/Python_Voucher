num = int(input("Digite um numero: "))

i = 1
soma = 0
while i <= num:
    div = num/i
    if div %i == 0 or div % i == 1:
        soma+=1
    i+=1

if soma == 2:
    print(f'O numero digitado {num} é primo')
else:
    print(f'O numero digitado {num} não é primo')