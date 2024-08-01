idade = int (input("Digite a idade do nadador:"))

if idade >= 5 and idade <= 12:
    print("Nadador infantil!")
elif idade >= 12 and idade <= 17:
    print("Nadador Juvenil!")
else:
    print("Nadador Senior!")