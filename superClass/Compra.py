class Compra:
    def __init__(self,numero,produto,valor,valor_total = 0):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = valor_total
    

    def calcular_valor_total(self):
        self.valor_total = self.valor +(self.valor*0.17)+(self.valor_total*0.05)

        return self.valor_total


class Avista(Compra):
    def __init__(self, numero, produto, valor, desconto,valor_total=0,):
        super().__init__(numero, produto, valor, valor_total)
        self.desconto = desconto 

    
    def valorDesconto(self):
        self.valor_total = self.valor_total - (self.valor_total*self.desconto)
        return self.valor_total

class Parcelada(Compra):
    def __init__(self, numero, produto, valor, parcelas,valor_total=0):
        super().__init__(numero, produto, valor, valor_total)
        self.parcelas = parcelas
    

    def qtdParcelas(self):
        return f"O produto será parcelado em x{self.parcelas}"