hora = 40.50

hora_trab=int (input("Digite as horas trabalhadas do seu funcionario:"))

total = hora*hora_trab

if total >= 2500:
    
    imposto = total -(total*0.11)
    print(f"Salario bruto R$ {total}\nSalario liquido R$ {imposto}")