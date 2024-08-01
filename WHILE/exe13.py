i = 0
guardar = []

while i < 3:
    num = int(input('Valor:'))
    i+= 1
    
    div = num%2

    
    if div == 0:
        guardar.append(num)

guardar.sort(key=int)
print(guardar)
