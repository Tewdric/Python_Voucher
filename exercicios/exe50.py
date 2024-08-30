tam = int(input("Digite o tamanho do laço: "))

i = 2
j = 3

cont = 0
lista = []
while cont < tam:
    
   
    t1 = j*cont
    
   
    lista.append(t1)
    
    
    cont += 1
    t = i*cont
    lista.append(t)
    if len(lista) == tam:
        break
    

print(lista)