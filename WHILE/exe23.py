div = []
i = 0

divisor = int (input("Digite um divisor: "))

while i < divisor:
    i+= 1
    
    if divisor % i == 0:
        div.append(i)

soma = sum(div)
print(f"Os dividores de {divisor} são {div} e sua soma é {soma}")