r = int(input("Digite o tamanho da escada: \n"))
i = 0
count = r
while i < r:
    i+= 1
    count -= 1
    x = "*"
    v =" "
   
    print(v*count,v*count+x*i,x*i,i*x,i*x+count*v,count*v)