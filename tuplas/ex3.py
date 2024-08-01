t = []

for i in range(3):
    n = int(input())
    
    if n % 2 ==0 : 
        t.append(n)
    
soma = sum(t)

print(soma)