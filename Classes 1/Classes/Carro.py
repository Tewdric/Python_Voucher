class Carro:
    
    def __init__(self, modelo, marca, cor, ano, valor,consumo, nivel =5) -> None:
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano 
        self.valor = valor 
        self.consumo = consumo
        self.nivel = nivel 
    
    
    def ligar(self):
        return"VRUUUUUUUUUUUUM"
    def setAbastecer(self,abastecer):
        self.nivel = self.nivel + abastecer  
        return self.nivel
    def getAndar(self, distancia):
        return distancia
    def verificar_nivel (self, distancia):
        media = self.nivel / distancia
        return f"{media:.1f}"
    def calcularImposto(self):
        ipva = self.valor*0.025
        return f"{ipva:.2f}"
    def carrinho(self):
        
        carrito ={
            "Modelo" : self.modelo,
            "Marca" : self.marca,
            "Cor" : self.cor,
            "Ano" : self.ano,
            "Valor" : self.valor,
            "Consumo" : self.consumo
            
        }
        
        for key, value in carrito.items():
            
            print(f"{key} : {value}")