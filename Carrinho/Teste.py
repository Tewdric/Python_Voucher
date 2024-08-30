class Teste:
    
    def __init__(self,estoque,total=None):
        self.estoque = estoque
        self.total = total
        
    def soma(self):
        
        p = 3
        qtd_estoque = 0
        count = 4
        soma = 0
        
        while p < len(self.estoque):
            soma+=self.estoque[p]
            qtd_estoque+=self.estoque[count]
            p+=5
            count+=5
            
        self.total =  soma*qtd_estoque
        return (f"Total de compras R${soma*qtd_estoque:.2f}")

    def listar(self):
        
        for itens in self.estoque:
           print(itens)
    
    def parcelar(self,qtd_parcelas):
        p = 3
        qtd_estoque = 0
        count = 4
        soma = 0
        
        while p < len(self.estoque):
            soma+=self.estoque[p]
            qtd_estoque+=self.estoque[count]
            p+=5
            count+=5
            
        self.total =  soma*qtd_estoque
        if qtd_parcelas == 1:
            return f"Ficará R${self.total-(self.total*0.05):.2f} com 5% de Desconto"
        elif qtd_parcelas == 2:
            return f'Ficará {qtd_parcelas}x de R${self.total/2:.2f}'
        elif qtd_parcelas == 3:
            return  f'Ficará {qtd_parcelas}x de R${self.total/3:.2f}'
        elif qtd_parcelas == 4:
            return  f'Ficará {qtd_parcelas}x de R${self.total/4:.2f}'
        else:
            return "Não é possivel parcelar mais de que 4x"

    def limparCarrinho(self):
        self.estoque = []
        return self.estoque