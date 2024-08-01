turno = str(input("Qual turno você estuda? \n'M' para Matutino \n'V' para vespertino \n'N' para Noturno\nQualquer outra letra derá errado!\nDigite o turno:"))

if turno == 'M' or turno == 'm':
    print('Bom dia!')
elif turno == 'V' or turno == 'v':
    print("Boa tarde!")
elif turno == 'N' or turno == 'n':
    print('Boa noite!')
else:
    print('Opção invalida, digite novamente:')
    turno = str(input("Qual turno você estuda? \n'M' para Matutino \n 'V' para vespertino \n 'N' para Noturno\n Qualquer outra letra derá errado! "))