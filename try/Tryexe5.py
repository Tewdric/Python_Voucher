"""
Crie uma função que receba e retorne a raiz quadrada de um número recebido por parâmetro, 
caso ocorra uma exceção de ValueError, 
apresentar a seguinte mensagem: "Valor impróprio para raiz quadrada“
"""

try:
    n1 = int(input())
    res = n1**2
        
    print(res)   
except ValueError:
        print("Valor impróprio para raiz quadrada!")
    

