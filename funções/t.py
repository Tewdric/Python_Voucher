
valor = float(input())
  
valores={
    'valor':valor
}
cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
 
quantidade_notas = 0
soma = 0

num = valores['valor']
print(num)
 
if valor > 3000:
    print("Valor não permitido, o saque deve ser menor que 3.000")
else:
    while valor >= 100:
        if valor >= 100:
            valor -=100
            cem +=1
            soma+=100
            quantidade_notas+= 1
        if valor >= 50 and valor <=99:
            valor-= 50
            cinquenta +=1
            soma+=50
            quantidade_notas+= 1
        if valor >= 20 and valor <= 49:
            valor-=20
            vinte += 1
            soma+=20
            quantidade_notas+= 1
        if valor >= 10 and valor<=19:
            valor-=10
            dez += 1
            soma+=10
            quantidade_notas+= 1
        if valor >= 5 and valor<= 9:
            valor-=5
            cinco+= 1
            soma+=5
            quantidade_notas+= 1
        if valor == 2:
            valor-= 2
            dois += 1
            soma+=2
            quantidade_notas+= 1
 
        if valor == 1:
            print("Não há como sacar o valor de R$ 1,00")
            print(f"Saldo restante R$ {valor}")
        if valor == 0:
            break
   

 
notas = {
    '100' : cem,
    '50':cinquenta,
    '20' : vinte,
    '10':dez,
    '5':cinco,
    '2':dois
}
 
 
for nota in notas:
    print(f'{notas[nota]}-{[nota]}')
print(f'Soma total do saque: R$ {soma:.2f}')
print(f"Quantidade notas que serão entregues: {quantidade_notas}")