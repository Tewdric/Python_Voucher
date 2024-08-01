import random

def sorteio():
    numeros =[]
    
    for i in range(5):
        numeros.append(random.randint(1,20))
    

    return numeros

lista = sorteio()

print(lista)

def soma_lista(lista):
    
    i = 0
    soma = 0
    while i < len(lista):
        if lista[i] % 2== 0:
            soma+= lista[i]
        
        i+=1

    print(soma)


print(soma_lista(lista))
    
