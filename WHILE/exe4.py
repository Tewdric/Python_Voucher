i = 0
cont = 0
for i in range (100):
    i+= 1
    print(i)

    if i == 100:
        print("******************************")
        for i in range (100):
            i+= 1
            print(i)
            if i == 100:
                print("\nCOMEÇANDO WHILE\n")
                break
        
i =0
while i < 100:
    i+= 1
    print(i)
    if i == 100:
        print("******************************")
        for i in range (100):
            i+= 1
            print(i)
            if i == 100:
                print("\n FINALIZANDO WHILE\n")
                break
    
    