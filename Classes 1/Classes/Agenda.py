class Agenda:
    
    def __init__(self,dia, mes,ano,anotacao):
        self.dia = dia
        self.mes = mes
        self.ano = ano 
        self.anotacao = anotacao
        
    def getValidarData (self):
        
        dia = input(f"A data informada está correta: {self.dia}/{self.mes}/{self.ano}?\n Digite 'S' ou 'N': ")

        if dia == "S" or dia == "s":
            return f"Agendado para: {self.dia}/{self.mes}/{self.ano}"
        else:
            return f"Agendamento adiado!"
    
    def setAnotar_Tarefa(self, nova_anotacao):
        
        self.anotacao = nova_anotacao
        
        return f"Anotação: {self.anotacao}"
    
    def getAnotacao(self):
        
        return f"Anotação: {self.anotacao}"
    
    def getAgendamento(self):
           
       cadastrados={
            'Dia' :self.dia,
            'Mes' : self.mes,
            'Ano': self.ano,
            'Anotacao': self.anotacao}
        
       for keys, values in cadastrados.items():
            
            print(f"{keys}: {values}")