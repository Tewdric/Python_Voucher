class Aluno:
    
    def __init__(self,nome, ra, n1,n2,n3,n4):
        
        self.__nome = nome
        self.__ra = ra
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.situacao = 0

    
    def getNome(self):
        return self.__nome
    
    def getRA(self):
        return self.__ra
    
    def getSituacao(self):
        
        media = (self.n1+self.n2+self.n3+self.n4)/4
        
        if media >=7:
            self.situacao =  "Aprovado, parabéns!"
            return f"{self.__nome} está de {self.situacao}"
        
        if media >= 5 or media <=6.9:
            self.situacao =  "Exame!"
            return f"{self.__nome} está de {self.situacao}"
        else:
            self.situacao = "Reprovado, uma pena!"
            return f"{self.__nome} está de {self.situacao}"

    def getAlunos(self):
        
        cadastrados={
            'Nome' :self.__nome,
            'RA' : self.__ra}
        
        for keys, values in cadastrados.items():
            
            print(f"{keys}: {values}")
            
        
