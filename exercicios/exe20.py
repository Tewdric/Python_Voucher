valor = int(input("Digite 1 para começar: "))
impar = []
par = []
total= []

cont_par = 0
cont_impar = 0

while valor == 1:

    print("Caso queira sair, digite 0!")
    n = int(input("Digite um numero:"))
    total.append(n)

    div = n % 2

    if div == 0:
        par.append(n)
    else:
        impar.append(n)
    
    if n == 0:
        break

total.remove(0)
par.remove(0)
print(total)
print(par)
print(impar)