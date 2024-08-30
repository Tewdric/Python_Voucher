class Filme:
    def __init__(self,nome,duracao):
        self.nome = nome
        self.duracao = duracao
        
    def play(self):
        
        return "O filme foi iniciado."
    

class Acao(Filme):
    
    def __init__(self, nome, duracao, personagem):
        super().__init__(nome, duracao)
        self.personagem = personagem
        
    
    def efeitoSonoro(self):
        
        return f"O {self.personagem} explodiu!"