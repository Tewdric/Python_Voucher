class Imovel:
    def __init__(self,inscricao_municipal, valor_aluguel, iptu):
        self.inscricao_municipal = inscricao_municipal
        self.valor_aluguel = valor_aluguel
        self.iptu = iptu
    
    def obter_parcela_IPTU(self):
        
        while True:
            option = input(f"""
                           O iptu pode ser parcelado em até 5x
                           O valor total de seu IPTU é de R${self.iptu}""")
            
            match option:
                case 1:
                    desconto = self.iptu-(self.iptu*0.05)
                    return f"Ganha com 5% de desconto. \nSeu iptu será R${desconto}"
                case 2:
                    return f"Seu IPTU será parcelado em 2x de {self.iptu/2}"
                case 3:
                    return f"Seu IPTU será parcelado em 2x de {self.iptu/3}"
                case 4:
                    return f"Seu IPTU será parcelado em 2x de {self.iptu/4}"
                case 5:
                    return f"Seu IPTU será parcelado em 2x de {self.iptu/5}"
    
    def set_valor_Aluguel(self, novo_valor):
        self.valor_aluguel = novo_valor
        return self.valor_aluguel
    
class Casa(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu,bairro):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.bairro = bairro
        
    def mostrarBairro(self):
        return self.bairro

class Condominio(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu,psicina :bool):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.psicina = psicina
        
    def mostrarBairro(self):
        return self.psicina


class Terreno(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu,tamanho):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.tamanho = tamanho
        
    def mostrarTamanho(self):
        return self.tamanho
    
class Chacara(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu,lago:bool):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.lago = lago
        
    def mostrarTamanho(self):
        return self.lago
    