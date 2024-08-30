class Pessoa1:
    def __init__(self,nome,telefone,email,endereco):
        self.nome = nome 
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
    
    def negociar(self):
        return "Negociação:"


class PessoaFisica(Pessoa1):
    def __init__(self, nome, telefone, email, endereco,cpf):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf
        
    def fisica(self):
        return self.cpf

class PessoaJuridica(Pessoa1):
    def __init__(self, nome, telefone, email, endereco,cnpj):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj
        
    def juridica(self):
        return self.cnpj