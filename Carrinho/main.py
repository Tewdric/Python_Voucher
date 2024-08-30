from Teste import Teste
i = 0
estoque = []

while True:
    print("""
        1 - Fazer Compras
        2 - Carrinho
        3 - Total de compras
        4 - Pagamento
        5 - Limpar Carrinho
        0 - Sair
    """)
    option = int(input())
    
    match option:
        case 1:
            id = estoque.append(f"ID: {i}")
            nome = estoque.append(f"Nome: {input('Nome do Produto: ')}")
            tipo = estoque.append(f"Tipo: {input('Tipo do Produto: ')}")
            preco = estoque.append(float(input('Preço do Produto: ')))
            qtd = estoque.append(int(input('Quantidade do produto: ')))

            p1 = Teste(estoque=estoque)
            i+=1
        case 2:
            print(p1.listar())
        case 3:
            print(p1.soma())
        case 4:
            print("É possivel parcelar em até 4x")
            parcelas = int(input('Digite a quantidade desejada de parcelas:'))

            print(p1.parcelar(parcelas))
            
            finalizar = input("Deseja finalizar a compra?\n'SIM'|'NÂO\n")
            if finalizar == 'sim' or finalizar=='SIM':
                p1.limparCarrinho()
            else:
                pass
        case 5:
            p1.limparCarrinho()
            print("Carrinho Limpo!")
        case 0:
            print("Obrigado pela preferência!")
            break

