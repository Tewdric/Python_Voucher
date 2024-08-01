i = 0
guardar = []

while i < 100:
    i+= 1
    
    div = i%2
    
    if div == 0:
        guardar.append(i)
    if len(guardar) >= 50:
        break
    
print(sum(guardar))

guardar1 = []

for i in range(100):
    
    i+= 1
    
    div = i%2
    
    if div == 0:
        guardar1.append(i)
    if len(guardar1) >= 50:
        break
    
print(sum(guardar1))