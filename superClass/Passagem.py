class Passagem:
    def __init__(self,preco,assento):
        self.preco=preco
        self.assento = assento 
    
    
    def alterar_preco(self, novo_preco):
        
        self.preco = novo_preco
        return self.preco
    
class PassagemAviao(Passagem):
    def __init__(self, preco, assento, portaoEmbarque, checkin):
        super().__init__(preco, assento)
        self.portaoEmbarque = portaoEmbarque
        self.checkin = checkin
    
    def mostrarPortao(self):
        return f"Seu portão de embarco é {self.portaoEmbarque}"

class PassagemBus(Passagem):
    def __init__(self, preco, assento, placa, nivel=20):
        super().__init__(preco, assento)
        self.placa = placa
        self.nivel = nivel 
        
    
    def abastecer(self, novo_nivel):
        
        self.nivel = self.nivel + novo_nivel
        return self.nivel

