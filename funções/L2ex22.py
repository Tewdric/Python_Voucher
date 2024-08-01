def soma_matriz(n1):
    matriz = [[10,20,30,40],
              [45,26,33,78],
              [19,18,17,16],
              [13,14,15,16]]
    if n1 > len(matriz) or n1 < 0:
        print('Valor não permitido')
    else:
        soma = sum(matriz[n1])
    
        
        print(soma)
        
    
print(soma_matriz(1))