t = (3,6,2,1,7,5)

i = 0 

while i < len(t):
    
    n = t[i]
    
    if t[i-1] > t[i]:
        print(t[i-1])
        n = t[i-1]
    
    i +=1

print(n)