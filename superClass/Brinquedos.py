class Brinquedo:
    def __init__(self,nome,cor,tamanho,preco):
        self.nome = nome 
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco 
        
    def brincar(self):
        return f"Estou brincando com o {self.nome}"


class Bleyblad(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, bico):
        super().__init__(nome, cor, tamanho, preco)
        self.bico = bico 
    
    def novo_bico(self, novo_bico):
        self.bico = novo_bico
        return self.bico

class Bola(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, tipo):
        super().__init__(nome, cor, tamanho, preco)
        self.tipo = tipo 
    
    def novo_tipo(self, novo_tipo):
        self.tipo = novo_tipo
        return self.tipo

class Boneca(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, desenho):
        super().__init__(nome, cor, tamanho, preco)
        self.desenho = desenho 
    
    def thisIS(self):
        return f"Essa boneca é do {self.desenho}"

class Pipa(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, linha):
        super().__init__(nome, cor, tamanho, preco)
        self.linha = linha 
    
    def thisIS(self):
        return self.linha

