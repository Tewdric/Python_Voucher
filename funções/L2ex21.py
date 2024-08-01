def matriz(n1):
    n2 = n1
    mat = []

    for linha in range (n1):
        lin = []
        for coluna in range (n2):
            lin.append(1)
        mat.append(lin)

    for i in mat:
        print(i)

print(matriz(4))