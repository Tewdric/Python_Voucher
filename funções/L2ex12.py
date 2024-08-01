def soma(n1,n2):
    
    if n2 < n1:
        return print(f"O {n2} não pode ser menor que o {n1}")
    else:
        i = n1
        soma = 0
        
        while i < n2:
            soma+=1
            i+=1
        

        return soma


x = soma(30,20)
print(x)