class Livro:
    
    def __init__(self,nome, autor, editora, paginas):
        
        self.__nome = nome
        self.__autor = autor
        self.__editora = editora
        self.__paginas = paginas

    
    def getNome(self):
        return self.__nome
    
    def getAutor(self):
        return self.__autor
            
    def setEditora(self, nova_editora):
        
        self.__editora = nova_editora
        
        return self.__editora
    
    def getPaginas(self):
        return self.__paginas

    def getLivros(self):
        
        cadastrados={
            'nome' :self.__nome,
            'autor' : self.__autor,
            'editora' : self.__editora,
            'paginas' : self.__paginas}
        
        for keys, values in cadastrados.items():
            
            print(f"{keys}: {values}")
            
        
