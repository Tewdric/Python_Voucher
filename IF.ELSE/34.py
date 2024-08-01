valor_ant = float(input("Digite o valor antigo do produto: "))

if valor_ant <= 50 :
    att = valor_ant +(valor_ant*0.05)
    print(f"O valor atualizado do valor vai para R${att:.2f}")
elif valor_ant >= 50 and valor_ant <= 100 :
    att = valor_ant +(valor_ant*0.1)
    print(f"O valor atualizado do valor vai para R${att:.2f}")
else:
    att = valor_ant +(valor_ant*0.15)
    print(f"O valor atualizado do valor vai para R${att:.2f}")

