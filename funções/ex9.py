##def calcularTempo():


n = 9
m = 1.50

minutos= int(input())

div = minutos/60

if div <= 0.25:
    print('Não precisa pagar')
elif div > 0.25 and div <= 1:
    print('Valor a ser pago: ', n)
elif div> 1:
    total = n*div
    
    print(total)