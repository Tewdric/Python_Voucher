venda_mensal = float(input("Digite o valor da vensa deste mês: "))

if venda_mensal >= 100000:
    vendedor = 700 +(venda_mensal*0.16)
    print(f"O vendededor ganhará de comissão este mes o valor de R${vendedor:.2f}")
elif venda_mensal < 1000000 or venda_mensal <= 80000:
    vendedor = 650 +(venda_mensal*0.14)
    print(f"O vendededor ganhará de comissão este mes o valor de R${vendedor:.2f}")
elif venda_mensal < 80000 or venda_mensal <= 60000:
    vendedor = 600 +(venda_mensal*0.14)
    print(f"O vendededor ganhará de comissão este mes o valor de R${vendedor:.2f}")
elif venda_mensal < 80000 or venda_mensal <= 60000:
    vendedor = 550 +(venda_mensal*0.14)
    print(f"O vendededor ganhará de comissão este mes o valor de R${vendedor:.2f}")
elif venda_mensal < 60000 or venda_mensal <= 40000:
    vendedor = 500 +(venda_mensal*0.14)
    print(f"O vendededor ganhará de comissão este mes o valor de R${vendedor:.2f}")
elif venda_mensal < 40000 or venda_mensal <= 20000:
    vendedor = 400 +(venda_mensal*0.14)
    print(f"O vendededor ganhará de comissão este mes o valor de R${vendedor:.2f}")
