salario = 1412
emprestimo = float(input("Digite o valor que deseja o emprestimo:"))

desc = salario*0.2

if emprestimo >= desc:
    print("Emprestimo não pode ser concedido, valor acima do minimo!")
else:
    print("Emprestimo concedido!")