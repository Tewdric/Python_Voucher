"""Faça um Programa que verifique se uma letra digitada é "F",
"M" ou "L" conforme a letra escrever: F - Feminino, M - Masculino, L – 
LGBT. Caso o usuário não selecione a opção
correta uma exceção apresenta a mensagem: “Opção Inválida”."""



try:
    generos={
        "f":"Feminino",
        "m":"Masculino",
        "l":"LGBT"
    }
    print("""
          "f"-"Feminino",
          "m"-"Masculino",
          "l"-"LGBT"
          """)
    letra = input("Digite seu genero: ")
        
    if letra != "f" and letra != "m" and letra != "l":
        raise RuntimeError("Letra não corresponde as solicitadas!")
    else:
        print(generos[letra])
except ValueError:
    print("Tipo de entrada inválida!")
except RuntimeError as e:
    print(f"Error, opção inválida: {e}")