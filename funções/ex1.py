
def calcularPorcetagem(salario,inss, meses):
    anual = (salario -(salario*inss))*meses
 
    
    return anual

print(f"Ganho anual de salario minimo = R$ {calcularPorcetagem(1412, 0.08,12)}")
