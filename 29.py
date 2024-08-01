idade = int (input("Digite sua idade: "))
ano = int (input("Digite o tempo trabalho: "))

if idade >= 65:
    print("Pode se aposentar")
elif idade >= 60 and ano >= 25:
     print("Pode se aposentar")
elif ano >= 30:
      print("Pode se aposentar")
else:
      print("Não pode se aposentar")
