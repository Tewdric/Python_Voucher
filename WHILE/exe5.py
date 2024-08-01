i = 0

while i <= 100000:
    print(i)
    i+=1000

cont = 0
soma = 0
for cont in range (100):
    
    cont += 1000
    soma += cont
    if soma >= 100000:
        break
    print(soma)