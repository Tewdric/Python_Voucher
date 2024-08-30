class Pessoa:
    
    def __init__(self,nome, idade, endereco):
        
        self.__nome = nome
        self.__idade = idade
        self.__endereco= endereco

    
    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade
            
    def setIdade(self, nova_idade):
        
        self.__idade = nova_idade
        
        return self.__idade
    
    def getEndereco(self):
        return self.__endereco

    def getPessoas(self):
        
        cadastrados={
            'nome' :self.__nome,
            'idade' : self.__idade,
            'endereco' : self.__endereco}
        
        for keys, values in cadastrados.items():
            
            print(f"{keys}: {values}")
            
        

