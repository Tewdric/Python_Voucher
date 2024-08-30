class Academia:
    
    def __init__(self, nome, idade:int, peso:float, altura:float, mensalidade = float(120)) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso 
        self.altura = altura
        self.mensalidade = mensalidade
    
    
    def calcularIMC(self):
        
        imc = self.peso/(self.altura*self.altura)
        
        if imc <= 18.5:
            return f"Magreza = {imc}"
        elif imc >= 18.6 and imc <=24.9:
            return f"Normal = {imc}"
        elif imc >= 25 and imc <=29.9:
            return f"Sobrepeso = {imc}"
        elif imc >= 30 and imc <=39.9:
            return f"Obesidade = {imc}"
        else:
            return f"Obesdidade Grave = {imc}"
    
    def desconto(self):
        
        if self.idade < 18:
            return self.mensalidade-(self.mensalidade*0.1)
        else:
            return self.mensalidade