class Ingresso:
    def __init__(self,preco,setor):
        self.preco = preco
        self.setor = setor 
    
    
    def setPreco(self, operacao:str, novo_preco):
        
        if operacao == "+":
            self.preco = self.preco + novo_preco
            return self.preco
        else:
            self.preco = self.preco - novo_preco
            return self.preco
    
    def getSetor(self):
        return self.setor
    

class IngressoVIP(Ingresso):
    def __init__(self, preco, setor,camarote:bool,open_bar:bool,open_food:bool,estacionamento:bool):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento
        
    def pegarBebida(self):
        
        return f"Pegou bebida"
    
    def irCamarote(self):
        return "Foi ao camarote"
        