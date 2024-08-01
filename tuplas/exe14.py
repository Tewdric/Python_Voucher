a = [[1,13,3],
     [4,45,67],
     [7,80,9]]
b = [[100,8,7],
     [6,5,4],
     [3,25,10]]

soma = []
s1 = []
s2 = []
s3 = []
for linha in range(3):
    for coluna in range(3):
        
        if linha == 0:
            adicao = a[linha][coluna] + b[linha][coluna]
            s1.append(adicao)
            
        elif linha == 1:
            adicao = a[linha][coluna] + b[linha][coluna]
            s2.append(adicao)
            
        elif linha == 2:
            adicao = a[linha][coluna] + b[linha][coluna]
            s3.append(adicao)
            
    soma.append(s1)
    soma.append(s2)
    soma.append(s3)
for i in range(3):
    print(soma[i])