idades = []

idade = True

while idade != False :
    idade = int(input("Digite sua idade: "))
    idades.append(f"Idade: {idade}")
    if idade == 0:
        break
    
    
print(idades)