class Transporte:
    def __init__(self,capacidade):
        self.capacidade = capacidade
    


class Aquatico(Transporte):
    def __init__(self, capacidade, nome):
        super().__init__(capacidade)
        self.nome = nome

    def getNome(self):
        return self.nome

class Terrestre(Transporte):
    def __init__(self, capacidade,rodas,cor,numero_portas,placa):
        super().__init__(capacidade)
        self.rodas=rodas
        self.cor = cor
        self.numero_portas = numero_portas
        self.placa = placa
    
    def descricao(self):

        info = {
            "Capacidade" : self.capacidade,
            "Rodas":self.rodas,
            "Cor":self.cor,
            "Numero de Portas": self.numero_portas,
            "Placa": self.placa
        }

        for key, values in info.items():
            print(f"{key}:{values}")

class Aereo(Transporte):
    def __init__(self, capacidade,nome):
        super().__init__(capacidade)
        self.nome = nome 
    
    def descricao(self):
        
        info = {
            "Capacidade":self.capacidade,
            "Nome" :self.nome

        }
        for key, values in info.items():
                print(f"{key}:{values}")



class Automovel(Terrestre):
    def __init__(self, capacidade, rodas, cor, numero_portas, placa,marca,modelo,ano):
        super().__init__(capacidade, rodas, cor, numero_portas, placa)
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def descricao(self):

        info = {
            "Capacidade" : self.capacidade,
            "Rodas":self.rodas,
            "Cor":self.cor,
            "Numero de Portas": self.numero_portas,
            "Placa": self.placa,
            "Marca" :self.marca,
            "Modelo" : self.modelo,
            "Ano":self.ano
        }

        for key, values in info.items():
            print(f"{key}:{values}")

class Lancha(Aquatico):
    def __init__(self, capacidade, nome, tamanho, cor):
        super().__init__(capacidade, nome)
        self.tamanho = tamanho
        self.cor = cor
    
    def descricao(self):

        info = {
            "Capacidade" : self.capacidade,
            "Nome": self.nome,
            "Tamanho": self.tamanho,
            "Cor" : self.cor
        }

        for key, values in info.items():
            print(f"{key}:{values}")

    
class Navio(Aquatico):
    def __init__(self, capacidade, nome, tamanho, cor):
        super().__init__(capacidade, nome)
        self.tamanho = tamanho
        self.cor = cor
    
    def descricao(self):

        info = {
            "Capacidade" : self.capacidade,
            "Nome": self.nome,
            "Tamanho": self.tamanho,
            "Cor" : self.cor
        }

        for key, values in info.items():
            print(f"{key}:{values}")


    

class AviaoMonomotor(Aereo):
    def __init__(self, capacidade, nome, tamanho, cor):
        super().__init__(capacidade, nome)
        self.tamanho = tamanho
        self.cor = cor
    
    def descricao(self):

        info = {
            "Capacidade" : self.capacidade,
            "Nome": self.nome,
            "Tamanho": self.tamanho,
            "Cor" : self.cor
        }

        for key, values in info.items():
            print(f"{key}:{values}")

class AviaoComercial(Aereo):
    def __init__(self, capacidade, nome, tamanho, cor):
        super().__init__(capacidade, nome)
        self.tamanho = tamanho
        self.cor = cor
    
    def descricao(self):

        info = {
            "Capacidade" : self.capacidade,
            "Nome": self.nome,
            "Tamanho": self.tamanho,
            "Cor" : self.cor
        }

        for key, values in info.items():
            print(f"{key}:{values}")

