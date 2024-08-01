matriz =[[1,2,3],
         [5,4,6],
         [7,8,9]]

i = 0
soma = 0

while i < 3:
    soma += sum(matriz[i])
    
    i+= 1

print(f"R ={soma}")