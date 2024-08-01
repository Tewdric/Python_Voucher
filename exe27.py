n = int(input("aa"))

fat = 1
i = 2
lista = []

while i <= n:
    fat = fat*i
    lista.append(f"{i}x")
    i+= 1
lista.insert(0,'1x')
lista.reverse()
print(f"{n}!= {lista} = {fat}")

