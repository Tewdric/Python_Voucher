matriz = [[1,2,11,13],
          [4,15,16,60],
          [7,8,19,200],
          [20,100,5,3]]

soma = 0
for linha in range(4):
    lin = []
    for coluna in range(4):
        if (matriz[linha][coluna]) > 10:
            soma += 1

print(f"R= {soma} valores maiores que dez.")
        