class Circulo:
    
    def __init__(self,raio) -> None:
        self.raio = raio
        
        
    def getCircunferencia(self):
        r = self.raio/(2*3.14)
        
        return f"Circunferencia: {r:.2f}"
    
    def getArea(self):

        a = 3.14*(self.raio*self.raio)
        
        return f"Area: {a:.2f}"
    
    def getRaio(self):
        
        return f"Raio: {self.raio}"