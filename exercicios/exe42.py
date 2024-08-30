import math
print("Digite 0 para sair")
while True:
    try:
        r1 = int(input("Digite um numero: \n"))
       
        
        if r1 == 0:
            print("Até a próxima!")
            break
        else:
            quadrado = r1 **2
            cubo = r1 **3
            raiz = math.sqrt(r1)
        
    except (ValueError, TypeError):
        print("O valores não aceitam String, digite novamente!")
    except Exception as error:
        print(f"A causa do erro foi: {error.__class__}")
    else:
        print(f'O quadrado do {r1} é: {quadrado}')
        print(f'O cubo do {r1} é: {cubo}')
        print(f'A raiz do {r1} é: {raiz:.2f}')
    