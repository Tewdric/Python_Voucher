from random import sample

def palavra(palavra:str):
    
    nome = palavra
    a = sample(nome,len(nome))

    i = 0
    txt = ''

    while i < len(a):
        txt += a[i]
        i+=1
        
    return print(txt)

print(palavra('Abelha'))
