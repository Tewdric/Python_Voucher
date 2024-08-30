i = 1
soma = 0

while i < 100:
    soma += i**2
    i+= 1
    
quadrado = soma ** 2
dif = quadrado - soma

print(f"Soma dos 100 numeros naturais = {soma}")
print(f"O quadrado da soma dos numeros = {quadrado}")
print(f"A diferença entre eles = {dif}")