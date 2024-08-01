def convert(h,m,s):
    h = h*3600
    m= m*  60
    
    soma = h+m+s
    print(soma)

print(convert(3,45,15))