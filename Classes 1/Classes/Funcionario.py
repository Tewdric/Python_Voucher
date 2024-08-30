class Funcionario:
    
    def __init__(self,nome,sobrenome,horas_trabalhadas:float,valor_hora:float):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
        
    def getNomeCompleto(self):
        
        nomeCompleto = (f"{self.__nome} {self.__sobrenome}")
        
        return nomeCompleto

    def getCalcularSalario(self):
        
        salario = self.horas_trabalhadas*self.valor_hora
        
        return (f"Salário: R$ {salario:.2f}")
    
    def setIncrementarHoras(self,horas_incrementadas):
        
        self.valor_hora = self.valor_hora + horas_incrementadas
        
        return (f"Horas trabalhadas atualizadas: {self.valor_hora}")
    
    def getFuncionário(self):
       salario = self.horas_trabalhadas*self.valor_hora
           
       cadastrados={
            'Nome' :self.__nome,
            'CPF' : self.__sobrenome,
            'Salário': salario}
        
       for keys, values in cadastrados.items():
            
            print(f"{keys}: {values}")