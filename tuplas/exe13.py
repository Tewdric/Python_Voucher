mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

soma = 0
for linha in range(3):
    lin = []
    for coluna in range(3):
        
        if linha == coluna:
            soma += mat[linha][coluna]
            
print("a soma é: ",soma)
     

