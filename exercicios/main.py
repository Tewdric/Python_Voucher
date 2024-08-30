#base de produtos
produtos = [
    {
        "produto": "notebook",
        "marca" : "dell",
        "estoque" : 20,
        "estoqueminimo": 4,
        "estoquemaximo":8,
        "preco": 2000,
        "codBarra": "777888999"
    },
    {
        "produto": "computador",
        "marca" : "dell",
        "estoque" : 20,
        "estoqueminimo": 4,
        "estoquemaximo":8,
        "preco": 2000,
        "codBarra": "333444888"
    } 
]
#base de vendas
vendas = []
#cadastra um novo produto na base
def cadastrarProduto(nome, marca, estoque, estoqueminomo, preco, codbarras,estoquemaximo):
    produto = {
        "produto": nome,
        "marca" : marca,
        "estoque" : estoque,
        "estoqueminimo": estoqueminomo,
        "estoquemaximo"
        "preco": preco,
        "codBarra": codbarras
    }
    produtos.append(produto)

#grava as informações de venda do produto
def efetuarVenda(produto, desconto, cliente, valorliquido, quantidade):
    venda = {
        "produto":produto,
        "desconto":desconto * 100,
        "cliente":cliente,
        "quantidade": quantidade,
        "valorLiquido": valorliquido
    }
    vendas.append(venda)
    return venda

#registra a reposição do produto das quantidades informadas e referente ao produto do codigo de barras informado na base
def reposicaoProduto(codBarra, quantidade):
    index = 0
    for valor in produtos:
        if valor["codBarra"] == codBarra:
            produtos[index]["estoque"] = produtos[index]["estoque"] + quantidade
            if produtos[index]["estoque"] >= produtos[index]["estoquemaximo"]:
                print("O estoque excedeu a quantidade maxima trabalhada!\n Favor entre em contado com a area comercial para reajuste do planejamento!")
            return True
        index += 1
    return False

#registra saida do produto das quantidades informadas e referente ao produto do codigo de barras informado na base
def saidaProduto(codBarra, quantidade):
    index = 0
    for valor in produtos:
        if valor["codBarra"] == codBarra:
            if produtos[index]["estoque"]>=quantidade:
                produtos[index]["estoque"] = produtos[index]["estoque"] - quantidade
                if produtos[index]["estoque"] <= produtos[index]["estoqueminimo"]:
                    print("Produto atingiu o estoque minimo favor realizar a reposição do produto")
                return True
            else:
                return False
        index += 1
    return False

#procura o produto em nossa base e o retorna para verificação
def pesquisarProduto(codBarra):
    for valor in produtos:
        if valor["codBarra"] == codBarra:
            return valor
    return False
#inicia a interface da aplicação
def app():
    sair = True
    while sair:
        print("\
          ====================MENU=================\n\
          ======1 REALIZAR VENDA===================\n\
          ======2 CADASTRAR PRODUTO================\n\
          ======3 REALIZAR REPOR ESTOQUE===========\n\
          ======4 SAIR=============================\n")
        opcao = int(input())
        #faz a validação dos dados informados e chama a função de venda com os dados fornecidos
        match opcao:
            case 1:
                produto = pesquisarProduto(input("insira o codigo de barra: "))
                while produto == False:
                    print("produto não encontrado")
                    produto = pesquisarProduto(input("insira o codigo de barra: "))
                quantidade = input("digite a quantidade comprada: ")
                try:
                    quantidade = int(quantidade)
                except:
                    quantidade = ''
                while quantidade == '':
                    print("as quantidade precisam ser informada")
                    quantidade = input("digite a quantidade comprada: ")
                    try:
                        quantidade = int(quantidade)
                    except:
                        quantidade = ''
                
                valorTotal = quantidade * produto["preco"]
                cliente = input("digite o nome do cliente: ")
                while cliente == '':
                    print("o cliente precisa ser informado")
                    cliente = input("digite o nome do cliente: ")
                desconto = input("qual o valor de desconto %: ").replace(',','.')

                if desconto == '':
                    desconto = 0
                else:
                    try:
                        desconto = float(desconto)/100
                    except:
                        desconto = 0
                valorLiquido = valorTotal * (1-desconto)
                if saidaProduto(produto["codBarra"], quantidade=quantidade):
                    venda = efetuarVenda(produto=produto,desconto=desconto,cliente=cliente,valorliquido=valorLiquido, quantidade=quantidade)
                    print(f"Venda efetuada com sucesso!\n\Produto: {venda['produto']['produto']}\n\Cliente: {venda['cliente']}\n\Marca: {venda['produto']['marca']}\n\Valor a Ser pago R$: {venda['valorLiquido']:.2f}\n")

                else:
                    print("quantidade insuficiente para realização da venda, favor efetue a entrada do produto")
            # pega as informações do produtos valida as informações caso alguma seja invalida e chama a função de cadastro com os dados fornecidos
            case 2:
                nome = input("digite o nome do produto: ")
                while nome == '':
                    print("o nome do produto não foi informado")
                    nome = input("digite o nome do produto: ")
                marca = input("digite a marca do produto: ")
                while marca == '':
                    print("a marca do produto precisa ser informada")
                    marca = input("digite a marca do produto: ")
                estoqueInicial = input("digite a quantidade de estoque inicial do produto: ")
                if estoqueInicial:
                    try:
                        estoqueInicial = int(estoqueInicial)
                    except:
                        estoqueInicial = 0
                estoqueminimo = input("digite a quantidade de estoque minimo para controle: ")
                try:
                        estoqueminimo = int(estoqueminimo)
                except:
                    estoqueminimo = ''
                while estoqueminimo == '':
                    print("o estoque minimo deve ser informado")
                    estoqueminimo = input("digite a quantidade de estoque minimo para controle: ")
                    try:
                        estoqueminimo = int(estoqueminimo)
                    except:
                        estoqueminimo = ''
                preco = input("Digite o preço do produto: ")
                try:
                    preco = float(preco)
                except:
                    preco = ''
                while not preco:
                    print("O preco do produto precisa ser informado")
                    preco = input("Digite o preço do produto: ").replace(',','.')
                    try:
                        preco = float(preco)
                    except:
                        preco = ''
                codBarra = input("Digite o codigo de barra: ")
                while not codBarra:
                    print("o codigo de barra precisa ser informado!")
                    codBarra = input("Digite o codigo de barra: ")
                    if pesquisarProduto(codBarra=codBarra):
                        print("o codigo de barras do produto ja foi cadastrado em nossa base!")
                        codBarra = ''

                cadastrarProduto(nome=nome,marca=marca,estoque=estoqueInicial,estoqueminomo=estoqueminimo,preco=preco,codbarras=codBarra)
                produto = pesquisarProduto(codBarra=codBarra)
                print("Produto Cadastrado com sucesso")
                print(f"Produto: {produto['produto']}\nMarca: {produto['marca']}\nCodigo de Barras: {produto['codBarra']}\nPreço:R${produto['preco']:2f}\nEstoqueInicial: {produto['estoque']}\nEstoque Minimo: {produto['estoqueminimo']}")
            # faz a validação dos dados e chama a função de entrada de produto com os dados fornecidos
            case 3:
                produto = pesquisarProduto(input("insira o codigo de barra: "))
                while produto == False:
                    print("produto não encontrado")
                    produto = pesquisarProduto(input("insira o codigo de barra: "))
                entrada = input("digite a quantidade de entrada: ")
                try:
                        entrada = int(entrada)
                except:
                    entrada = ''
                while entrada == '':
                    print("a quantidade de entrada precisa ser informada")
                    entrada = input("digite a quantidade de entrada: ")
                    try:
                        entrada = int(entrada)
                    except:
                        entrada = ''
                if reposicaoProduto(produto["codBarra"], quantidade=entrada):
                    print("quantidade inserida com sucesso!")
                    produto = pesquisarProduto(produto["codBarra"])
                    print(f"estoque atual {produto['estoque']}")
            #encerra a aplicação
            case 4:
                sair = False
            case _:
                print("opção invalida")
app()


    
