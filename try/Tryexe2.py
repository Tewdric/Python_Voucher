"""​
Escreva um programa Python que solicite ao usuário que insira dois números e gere uma exceção 
TypeError se as entradas não forem numéricas.
"""

try:
    n1 = int(input())
    n2 = int(input())
    
    soma = n1+n2
    print(f"Soma dos valores: {soma}")
except ValueError:
    print("Entrada invalidá")