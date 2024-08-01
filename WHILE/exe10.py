i = 0
guardar = []

while i < 10:
    n = int(input("Digite um numero inteiro:"))
    i+= 1
    
    div = n%2
    
    if div == 1:
        guardar.append(n)
    if len(guardar) >= 3:
        break
    
print(guardar)


i = 0
guardar = []

for i in range (10):
    i+= 3
    n = int(input("Digite um numero inteiro:"))
    i+= 1
    
    div = n%2
    
    if div == 1:
        guardar.append(n)
    if len(guardar) >= 3:
        break

print(guardar)
