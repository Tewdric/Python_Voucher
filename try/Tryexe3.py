"""Crie uma função para realizar o saque de conta corrente. Uma exceção é lançada sempre 
que o saldo da conta for inferior ao valor sacado."""


try:
    saldo = 1000
    saque = float(input("Digite o valor do saque: "))
    
    valor = saldo - saque
    
    
    if saque < saldo:
        print(f"Valor do saque: R${saque:.2f}")
        print(f"Saldo restante: R${valor:.2f}")
    elif saque > saldo:
        raise RuntimeError(f"Não há como prosseguir com o saque, valor superior ao saldo disponivel!")
except RuntimeError as e:
    print(f"Erro de execução: {e}")