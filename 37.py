custo_fabrica = float(input("Digite o custo de fabrica: "))

if custo_fabrica <= 12000:
    distribuidor = custo_fabrica +(custo_fabrica*0.05)
    print(f"O veiculo passará a custar agora o valor de R$ {custo_fabrica:.2f} ")

elif custo_fabrica >= 12000 and custo_fabrica <= 25000:
    distribuidor = custo_fabrica +(custo_fabrica*0.1)
    imposto = custo_fabrica+(custo_fabrica*0.15)
    total = distribuidor+imposto

    print(f"O veiculo passará a custar agora o valor de R$ {total:.2f} ")

else:
    distribuidor = custo_fabrica +(custo_fabrica*0.15)
    imposto = custo_fabrica+(custo_fabrica*0.2)
    total = distribuidor+imposto

    print(f"O veiculo passará a custar agora o valor de R$ {total:.2f} ")
