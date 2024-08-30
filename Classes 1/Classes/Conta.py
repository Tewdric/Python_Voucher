class Banco:
    
    def __init__(self,nome,cpf,numero,saldo=0) -> None:
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo 
        
        
    
    def setDepositar(self, deposito):
        
        self.saldo = self.saldo + deposito
        
        return f"Deposito realizado de R${deposito}. \nSaldo atualdo R${self.saldo}"
    
    def setSacar(self, saque):
        
        self.saldo = self.saldo - saque
        
        return f"Deposito realizado de R${saque}. \nSaldo atualdo R${self.saldo}"
    
    def getSaldo(self):
        
        return self.saldo

    def getInfo(self):
        
        cadastrados={
            'Nome' :self.nome,
            'CPF' : self.cpf,
            'Número' : self.numero,
            'Saldo' : self.saldo}
        
        for keys, values in cadastrados.items():
            
            print(f"{keys}: {values}")
            