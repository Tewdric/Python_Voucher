def operacao(n1, simbol:str,n2):
    
    if simbol == '/':
        conta = n1/n2
        return print(conta)
    elif simbol == '+':
        conta = n1+n2
        return print(conta)
    elif simbol == '-':
        conta = n1-n2
        return print(conta)
    elif simbol == '*':
        conta = n1*n2
        return print(conta)
    

print(operacao(10,'*',5))