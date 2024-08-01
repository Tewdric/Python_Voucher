alunos = [("João", 8.0), 
          ("Maria", 9.5), 
          ("Pedro", 7.5), 
          ("Ana", 8.5)]
i = 0 
c = 1
cc = -1
while i < len(alunos):    
    
    if alunos[i][c] < alunos[cc][c]:
        n = alunos[cc][c]
        print(alunos.index(i,n))
    
    i +=1
    cc -= 1



    

