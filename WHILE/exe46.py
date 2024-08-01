chico = 170
ze = 120

sair = True
i = 0
z = 0
anos = 0
while sair :
    
    i += 2
    z += 3
    anos += 1
    
    chico += i
    ze += z
    
    if ze > chico:
        print(f"Depois de {anos} anos, altura deles:")
        print(f"Altura do Ze atualmente {ze}")
        print(f"Altura do Chico atualmente {chico}")
        break
    