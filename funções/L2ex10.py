def notas(n1:float,n2:float,n3:float,letra:str):
    
    if letra == 'A':
        media = n1+n2+n3/10
        return print(media)
    elif letra == 'P':
        media_ponderada = (n1*5)+(n2*3)+(n1*2)/10
        return print(media_ponderada)

print(notas(10,7,8,'P'))