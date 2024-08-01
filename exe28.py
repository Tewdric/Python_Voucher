s = int(input("Digite um numero: "))

top = 0
bottom = 0
l1 = []
l2 = []
i = 0

while i < s:
    top += 2
    l1.append(top)
    bottom += 1
    l2.append(bottom)
    print(top)
    print(bottom)
   
    i+= 1

r1 = sum(l1)+1
r2 = sum(l2)

m = r1/r2

print(m)
