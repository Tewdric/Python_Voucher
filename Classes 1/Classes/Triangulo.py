class Triangulo:
    
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    
    def calcularPerimetro(self):
        perimetro = self.a+self.b+self.c
        
        return f"Perimetro do triângulo: {perimetro}"
    
    def getMaiorLado(self):
        
        if self.a > self.b and self.a > self.c:
            return self.a
        elif self.b > self.a and self.b > self.c:
            return self.b
        else:
            return self.c
        
    def getLados(self):
        
       cadastrados={
            'Lado_A' :self.a,
            'Lado_B' :self.b,
            'Lado_C':self.c}
        
       for keys, values in cadastrados.items():
            
            print(f"{keys}: {values}")