i = 0
guarda = []


while i < 20:
    
    i += 1
    impares = i %2
    if impares == 1:
        guarda.append(i)
    if len(guarda) >= 5:
        break
print(guarda)