def exclamacao(n1):
    
    i = 0
    cont = n1+1
    while cont > 0:
            print(cont*'!')
            cont-=1
            while i < n1:
                print(i*'!')
                i+=1
        
            
print(exclamacao(5))