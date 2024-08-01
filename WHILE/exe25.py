option = False 
idades = []

print("Digite 0 para Sair do programa!")
while option != True :
    
    idade = int (input("Digite sua idade: "))
    idades.append(idade)
    
    if idade == 0:
        print("Saindooo!")
        option= True
    

media = sum(idades)/len(idades)

print(f"A média das idades: {media} anos")
    
    
    