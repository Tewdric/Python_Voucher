class NF:
    
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, valor_produtos, ICMS, frete, IPI, valor_total = 0):
        self.numero = numero
        self.tipo = tipo 
        self.serie = serie
        self.cnpj = cnpj 
        self.razao_social = razao_social
        self.data = data
        self.valor_produtos = valor_produtos
        self.icms = ICMS
        self.frete = frete
        self.ipi = IPI
        self.valor_total = valor_total

    def obterNumero(self):
        
        return self.numero
    
    def obterDataEmissão(self):
        
        return self.data
    
    def alterarRazaoSocial(self, nova_razao_social):
        
        self.razao_social = nova_razao_social
        
        return self.razao_social
    
    def calcularValor(self):
        self.valor_total = self.valor_produtos + self.frete + self.icms + self.ipi
        
        return self.valor_total