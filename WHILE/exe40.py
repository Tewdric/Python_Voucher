try:
    a = int(input("Digite o intervalo a"))
    b = int(input("Digite o intervalo b"))
    i = a
    soma = 0
    while i < b:
        
        if i%2 == 1:
            soma+=i
           
        i+=1 
except ValueError:
    print("O numero não pode ser string")
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}")
else:
   print(soma)
finally:
    print("Até a proxima!")