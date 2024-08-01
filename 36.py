salario_atual = float (input("Digite o salario atual: "))
tempo_serviço = int(input("Digite o tempo de serviço na empresa: "))

if salario_atual <= 500 :
    reajuste = salario_atual +(salario_atual*0.25)
    
    if tempo_serviço < 0: 
        bonus = reajuste + 0
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    elif tempo_serviço >= 1 and tempo_serviço <=3 : 
        bonus = reajuste + 100
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    elif tempo_serviço >= 4 and tempo_serviço <= 6: 
        bonus = reajuste + 200
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    elif tempo_serviço >= 7 and tempo_serviço <= 10: 
        bonus = reajuste + 300
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    else:
        bonus = reajuste + 500
        print(f"Seu salario será reajustado para R${bonus:.2f}")

elif salario_atual <= 1000 :

    reajuste = salario_atual +(salario_atual*0.20)

    if tempo_serviço < 0: 
        bonus = reajuste + 0
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    elif tempo_serviço >= 1 and tempo_serviço <=3 : 
        bonus = reajuste + 100
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    elif tempo_serviço >= 4 and tempo_serviço <= 6: 
        bonus = reajuste + 200
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    elif tempo_serviço >= 7 and tempo_serviço <= 10: 
        bonus = reajuste + 300
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    else:
        bonus = reajuste + 500
        print(f"Seu salario será reajustado para R${bonus:.2f}")

elif salario_atual <= 1500 :

    reajuste = salario_atual +(salario_atual*0.15)

    if tempo_serviço < 0: 
        bonus = reajuste + 0
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    elif tempo_serviço >= 1 and tempo_serviço <=3 : 
        bonus = reajuste + 100
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    elif tempo_serviço >= 4 and tempo_serviço <= 6: 
        bonus = reajuste + 200
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    elif tempo_serviço >= 7 and tempo_serviço <= 10: 
        bonus = reajuste + 300
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    else:
        bonus = reajuste + 500
        print(f"Seu salario será reajustado para R${bonus:.2f}")

elif salario_atual <= 2000 :

    reajuste = salario_atual +(salario_atual*0.)

    if tempo_serviço < 0: 
        bonus = reajuste + 0
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    elif tempo_serviço >= 1 and tempo_serviço <=3 : 
        bonus = reajuste + 100
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    elif tempo_serviço >= 4 and tempo_serviço <= 6: 
        bonus = reajuste + 200
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    elif tempo_serviço >= 7 and tempo_serviço <= 10: 
        bonus = reajuste + 300
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    else:
        bonus = reajuste + 500
        print(f"Seu salario será reajustado para R${bonus:.2f}")


elif salario_atual > 2000 :

    reajuste = salario_atual 

    if tempo_serviço < 0: 
        bonus = reajuste + 0
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    elif tempo_serviço >= 1 and tempo_serviço <=3 : 
        bonus = reajuste + 100
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    elif tempo_serviço >= 4 and tempo_serviço <= 6: 
        bonus = reajuste + 200
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    elif tempo_serviço >= 7 and tempo_serviço <= 10: 
        bonus = reajuste + 300
        print(f"Seu salario será reajustado para R${bonus:.2f}")
    else:
        bonus = reajuste + 500
        print(f"Seu salario será reajustado para R${bonus:.2f}")

