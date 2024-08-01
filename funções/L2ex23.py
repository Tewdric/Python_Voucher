import random

def aluno(n1):
    
    alunos=[]
    
    for i in range(n1):
        alunos.append(input('Digite o nome do aluno: '))

    
    aluno_random = random.choice(alunos)
    
    print(f'O primeiro aluno a apresentar será: {aluno_random}')
    


print(aluno(3))