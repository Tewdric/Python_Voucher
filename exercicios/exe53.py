idades = []
alturas = []
pesos = []
imc = []
s = []


i = 0

while i < 3:
    
    nome = input("\nDigite seu nome: ")
    idade = int(input("Digite sua idade: "))
    idades.append(idade)
    
    sexo = input("Digite 'F' para Feminino, 'M' para Masculino: ")
    s.append(sexo)
    
    altura = int(input("Digite sua altura: "))
    alturas.append(altura)
    
    peso = float(input("Digite seu peso: "))
    pesos.append(peso)

    imcc = peso/(altura*altura)
    imc.append(imcc)

    i+= 1

media_altura = sum(alturas)/len(alturas)
media_imc = sum(imc)/len(imc)

mulheres = s.count('F')
homens = s.count('M')

porc_f = (mulheres/100*len(s))*1000
porc_m = (homens/100*len(s))*1000

print(f"\nA idade da pessoa mais velha: {max(idades)}")
print(f"A idade da pessoa mais nova: {min(idades)}")
print(f"A altura da pessoa mais alta: {max(alturas)}")
print(f"A altura da pessoa mais baixa: {min(alturas)}")
print(f"O peso da pessoa mais pesada: {max(pesos)}")
print(f"A media da altura: {media_altura:.0f}\nA media do imc: {media_imc:.4f}")
print(f"Porcetagem de mulheres: {porc_f}%")
print(f"Porcetagem de homens: {porc_m}%")

