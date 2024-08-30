class Funcionario:
    def __init__(self,nome,matricula,salario):
        self.nome = nome 
        self.matricula = matricula
        self.salario = salario 
        
    def bater_ponto(self):
        return f"{self.nome} bateu o ponto!"


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario, comissao):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao 
    
    def bater_meta(self):
        return f"Bater a meta"


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario, senha):
        super().__init__(nome, matricula, salario)
        self.senha = senha
    
    def loja(self,loja):
        return f"{self.nome} é gerente da loja {loja}"