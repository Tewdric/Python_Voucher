import random

item = []
produto = []
id_cliente=[]
cliente = []
nota = []
lista_geral = []

opcao = False

while opcao != True:
    
    print("\n============ MENU DE OPÇÕES ==============")
    #print("========== 10-CADASTRAR CLIENTE ===========")
    print("========== 2-GERENCIAR ESTOQUE ===========")
    print("========== 3-CADASTRAR PRODUTO ===========")
    print("========== 4-REALIZAR VENDA ==============")
    print("============ 0-SAIR  =====================\n")

    opcao = int(input("Digite a opção desejada: "))
    
    #if opcao == 10:
        
    if opcao == 3:
        
        print("========== CADASTRAR PRODUTO ===========\n")
        qtd_produto = int(input("Deseja Cadastrar quantos produtos:"))
        
        for i in range(qtd_produto):
            i+= 1
            item.append(f"Codigo do Produto {i}")
            
            tipo_produto= str(input("O tipo de produto eletronico:"))
            produto.append(f"Tipo: {tipo_produto}")

            modelo_produto= str(input("O modelo do produto:"))
            produto.append(f"Modelo: {modelo_produto}")

            quantidade_produto = int (input("Quantidade de produtos:"))
            
            while quantidade_produto >= 50:
                print("Quantidade excedente so permitido, não pode passar de 50")
                quantidade_produto = int (input("Quantidade de produtos:"))
           
                
            produto.append(quantidade_produto)
            
            
            preco_produto = float(input("Preço unitario: R$"))
            produto.append(preco_produto)
            item.append(produto)
            lista_geral.append(item)
        
    if opcao == 4:
        print("========== 4-REALIZAR VENDA ==============\n")
        print(f"Produtos disponiveis{item}")
        
        opcao_produto = int(input("Digite o Codigo do produto desejado:"))
        
        if opcao_produto == 1 :
            
            print("Produto celucionado: ",item[1])
            
            valor = int(input("Quantidade de produtos que levará: "))
            
            
            if valor > item[1][2]:
                print("Não há essa quantidade de produtos no momento!")
            else:
                total = item[1][3]
                final = total * valor
                print(f"O total a pagar ficará em R$ {final:.2f}")
                
                nota.append(f"Codigo da nota fical {random.getrandbits(20)}")
                metod_pagamento = str(input("Metodo de pagamentos: \nDEBITO desconto de 10%\nDINHEIRO desconto de 5%\nCREDITO 3x sem JUROS\n DIGITE O METODO DE PAGAMENTO:"))
                nota.append(f"Metodo de pagamento; {metod_pagamento}")
                
                
                if metod_pagamento == 'DEBITO' or metod_pagamento == 'debito':
                    desconto = final-(final*0.1)
                    nota.append(f"Desconto de 10% - Preço a ser pago R$ {desconto}")
                elif metod_pagamento == 'DINHEIRO' or metod_pagamento == 'dinheiro':
                    desconto = final-(final*0.05)
                    nota.append(f"Desconto de 5% - Preço a ser pago  R$ {desconto}")
                    
                else:
                    parcelas = int(input("Deseja parcelar em quantas vezes?"))
                    
                    desconto = final / parcelas
                    quantidade_parcelas =(f"Serão {parcelas} de R$ {desconto}")
                    nota.append(quantidade_parcelas)
                
                    
                finalizar = str(input("Digite s/n para finalizar:"))
                
                if finalizar == 's' or finalizar == 'S':
                    qtd_cliente = int(input("Deseja Cadastrar Quantos clientes?"))
        
                    for id in range(qtd_cliente):
                        
                        id+= 1
                        
                        id_cliente.append(f"Codigo do Cliente: {id}")
                        
                        print("========== CADASTRAR CLIENTE ===========\n")
                        nome_cliente= str(input("Nome do cliente:"))
                        cliente.append(nome_cliente)
                        endereco_cliente= str(input("Endereço:"))
                        cliente.append(endereco_cliente)
                        telefone_cliente = int (input("Telefone:"))
                        cliente.append(telefone_cliente)
                        id_cliente.append(cliente)
                        lista_geral.append(item)

                        #protudo_nota = item[1][0],item[1][1]

                       
                        nota.append(f"Cliente: {id_cliente[1]}")
                        nota.append(f"Produto {item[1][0],item[1][1]}")
                        
                        print(f"=================Nota Fiscal=================\n{nota}")
                        
                        sub_quantidade = produto[2]-valor
                        
                        produto.pop(2)
                        produto.insert(2,sub_quantidade)
                        
                        if produto[2] < 5:
                            print(f"Seu produto está quase acabando. faça pedido")
                            print(produto)
                else:
                    pass

    
    if opcao == 2:

        print("========== GERENCIAR ESTOQUE ===========\n")
        print("========= 1 -VISUALIZAR ESTOQUE ========")
        print("========= 2 - EXCLUIR ITEM =============")
        print("========= 0 - VOLTAR AO MENU============")
        acao = int(input("Digite uma opção:"))
        
        if acao == 1:
            print(f"Produtos: {item}\nClientes: {id_cliente}")
        elif acao == 2:
            print(f"Produtos: {item}\nClientes: {id_cliente}")
            selecionar = int(input("Digite 1 para excluir Cliente: \nDigite 2 para excluir Produtos: "))
            
            if selecionar == 1:
                print(f"Produtos: {item}")
                deletar = input("Digite s/n para deletar item:")

                if deletar == 's' or deletar == "S":
                    item.remove(item[1])
                    print(item)
                else:
                    print("Nenhum Item excluido!")
                    print(item)
                    pass
            elif selecionar == 2:
                print(f"Clientes: {id_cliente}")
                deletar = input("Digite s/n para deletar item:")

                if deletar == 's' or deletar == "S":
                    item.remove(id_cliente[1])
                    print(id_cliente)
                else:
                    print("Nenhum Item excluido!")
                    print(id_cliente)
                    pass
                
    #Clientes: {cliente}\nProdutos:{produto}\n
    elif opcao == 0:
        opcao = True
        print("Tchau")
        break
