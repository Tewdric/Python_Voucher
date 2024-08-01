lista = [1,1,2,3,4,4,5,6,7]

i = 0
try:
    
    while i < 3:
    
        num = int(input("Digite um numero: "))
        print(f"Há {num} na lista = ",lista.count(num))
    
        i+=1
except (ValueError):
    print("O valor não pode ser letras")
except Exception as erro:
    print(f"A causa do erro foi: {erro.__cause__}")
finally:
    print("Finalizando programa, adios.")