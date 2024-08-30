carlos = 1000
joao = carlos/3

soma = 0
i = 0
while soma < carlos:
    
    porcentagem = (joao*0.05)
    soma+= porcentagem
    
    i+=1 
    
print(f"Demorará {i} meses para que João ganhe R$ {soma:.2f}")
