item = []
prod = []

for i in range (1):
    i+= 1
    item.append(f"Produto Nº {i}")
    prod.append(f"Codigo do produto: {i}")
    marca = input("Marca: ")
    prod.append(f"Marca: {marca}")
    model = input("Modelo: ")
    prod.append(f"Modelo: {model}")
    quantidade= int(input("QUantidade:"))
    prod.append(quantidade)

item.append(prod)

print(f"{item}")
selecionar = int(input("Selecione o item que gostaria de excluir:"))

if selecionar == 1:
    print(f"Item selecionado {item[1]}")
    deletar = input("Digite s/n para deletar item:")

    if deletar == 's' or deletar == "S":
        item.remove(item[1])
        print(item)
    else:
        print("Nenhum Item excluido!")
        print(item)
        pass
elif selecionar == 2:
    prod.pop()
    sub = 3
    prod.insert(3, sub)

print(item)