def soma_imposto(taxaImposto, altera):
    novo_valor = taxaImposto +(taxaImposto*altera)
    
    return novo_valor

print(f'Valor do novo produto = R${soma_imposto(1780,0.03):.2f}')
