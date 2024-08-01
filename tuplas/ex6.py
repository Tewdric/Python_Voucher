matriz = [[1,0,0],
          [0,1,0],
          [0,0,1]]
mat = []

for linha in range (5):
    lin = []
    for coluna in range (5):
        if linha == coluna:
            lin.append(1)
        else:
            lin.append(0)
    mat.append(lin)

for i in mat:
    print(i)