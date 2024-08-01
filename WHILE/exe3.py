i = 0
guarda = []


while i < 20:
    
    i += 1
    impares = i %2
    if impares == 0:
        guarda.append(i)
    if len(guarda) >= 10:
        break
print(guarda)