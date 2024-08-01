print("TABELA DE IMPOSTO ENCIMA DO PRODUTO DE CADA ESTADO: \nMG: 7%\nSP:12%\nRJ:15%\nMS:8%")
estado = str (input("Digite o estado de destino:"))
valor = float (input("Digite o valor do produto:"))

if estado != "MG" and estado != "SP" and estado != "RJ" and estado != "MS":
    print("Estado invalido")
elif estado == "MG":
    imposto = valor -(valor*0.07)
    print(f"O valor do produto será vendido por R$ {imposto:.2f}")
elif estado == "SP":
    imposto = valor -(valor*0.12)
    print(f"O valor do produto será vendido por R$ {imposto:.2f}")
elif estado == "RJ":
    imposto = valor -(valor*0.15)
    print(f"O valor do produto será vendido por R$ {imposto:.2f}")
elif estado == "MS":
    imposto = valor -(valor*0.07)
    print(f"O valor do produto será vendido por R$ {imposto:.2f}")