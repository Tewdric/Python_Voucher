matriz = [  [1,120,-3],
            [4,5,250],
            [4,0,9]]

menor = 0

c = 0
for linha in range(3):
    lin = []
    for coluna in range(3):
        if matriz[linha][coluna] > c:
            c = matriz[linha][coluna]
    
        if matriz[linha][coluna] <= menor:
            menor = matriz[linha][coluna]

print(c, menor)