i = -1
guardar = []

while i < 10:
    i+= 1
    
    div = i%2
    
    if div == 0:
        guardar.append(i)

guardar.reverse
print(guardar)

guardar1 = []


for i in range(10):
    
    i+= 1
    
    div = i%2
    
    if div == 0:
        guardar1.append(i)

guardar1.reverse
print(guardar1)