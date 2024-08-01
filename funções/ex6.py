def tabela_precos():
    i = 1
    valor = 1.99
    while i < 51:
        print(f'{i} - R${valor*i:.2f}')
        i+=1

tabela_precos()