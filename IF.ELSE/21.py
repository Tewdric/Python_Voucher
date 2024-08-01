lab = float(input("Digite sua nota de atividade de laboratorio:"))
avBi= float(input("Digite sua nota na avaliação bimestral:"))
exF= float(input("Digite sua nota no exame final:"))

lb = 2
aV = 3
exFF = 5

x = (lab * lb)+(avBi*aV)+(exF*exFF)/lb+aV+exFF
m = x/6

if m >= 0 and m <= 2.9:
    print("Aluno reprovado!")
elif m >= 3 and m <= 5.9:
    print("Aluno de recuperação!")
else:
    print("Aluno aprovado!")