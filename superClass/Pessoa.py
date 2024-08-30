class Pessoa:
    def __init__(self,matricula,nome,idade) :
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
    

class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, notas, media):
        super().__init__(matricula, nome, idade)
        self.notas = notas
        self.media = media
        
    
    def notas(self,n1,n2,n3):
        
        notas = {
            "Nota 1" : n1,
            "Nota 2" : n2,
            "Nota 3" : n3
        }
        
        for key, value in notas.items():
            print(f"{key} : {value}")
    
    def media(self, n1,n2,n3):
        
        m = (n1+n2+n3)/3
        
        if m >= 7:
            return "Passou"
        elif m >= 5 and m <= 6.9:
            return "Exame"
        else:
            return "Reprovado"
    
    def estudar(self):
        return f"{self.nome} está estudando!"


class Professor(Pessoa):
    def __init__(self, matricula, nome, idade,formacao,disciplina,cargaHorario,salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.cargaHorario = cargaHorario
        self.salario = salario
    
    def info(self):
        
        informacoes ={
            
            'Matricula' : self.matricula,
            'Nome' : self.nome,
            'Idade' : self.idade,
            'Formação' : self.formacao,
            'Disciplina' : self.disciplina,
            'Carga Horária' : self.cargaHorario,
            'Salário' : self.salario
        }
        
        for key, value in informacoes.items():
            print(f"{key} : {value}")
        
    def estudar(self):
        return f"{self.nome} está dando aula!"