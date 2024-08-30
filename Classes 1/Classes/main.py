from Pessoa import Pessoa
from Livro import Livro
from Aluno import Aluno
from Conta import Banco
from Funcionario import Funcionario
from Circulo import Circulo
from Agenda import Agenda
from Triangulo import Triangulo
from Academia import Academia
from Carro import Carro
from NF import NF

while True:
    
    print("""
          Opções de cadastro:
          1 - Pessoa
          2 - Livro
          3 - Aluno
          4 - Banco
          5 - Funcionário
          6 - Circulo
          7 - Agenda
          8 - Triângulo
          9 - Academia
          10 - Carro
          11 - Nota Fiscal
          
          0 - Sair
          
          Digite a opção desejada:
          """)
    
    option = int(input())
    
    match option:
        
        case 1 :
            nome = input("Digite seu nome:")
            idade = input("Digite sua idade: ")
            endereco = input("Digite seu endereço: ")
            p= Pessoa(nome=nome,idade=idade, endereco= endereco)                
            print(p.getPessoas())
            
        case 2 :
            nome = input("Digite o nome do livro:")
            autor = input("Digite o nome do autor: ")
            editora = input("Digite nome da editora: ")
            paginas = input("Digite a quantidade de paginas: ")
            l= Livro(nome=nome,autor=autor, editora= editora, paginas=paginas)
            print(l.getLivros())
            
        case 3:
            nome = input("Digite o nome do aluno: ")
            ra = input("Digite o RA do aluno: ")
            n1 = int(input("Digite a nota 1: "))
            n2 = int(input("Digite a nota 2: "))
            n3 = int(input("Digite a nota 3: "))
            n4 = int(input("Digite a nota 4: "))
            aluno1= Aluno(nome=nome, ra=ra, n1= n1, n2=n2, n3=n3,n4=n4)
            
            print(aluno1.getAlunos())
            print(aluno1.getSituacao())
 
        case 4:
            nome = input("Digite seu nome:")
            cpf = input("Digite seu cpf: ")
            numero = input("Digite o número da conta: ")
            saldo = float(input("Digite o saldo atual: "))
            cli= Banco(nome=nome,cpf=cpf, numero= numero, saldo=saldo)
            print(cli.getInfo())
            print(cli.setDepositar(150))
            print(cli.getInfo())
        
        case 5:
            
            nome = input("Digite seu nome: ")
            sobrenome = input("Digite seu sobrenome: ")
            horas = float(input("Digite a quantidade de horas trabalhadas: "))
            valor = float(input("Digite o valor da hora: "))
            func= Funcionario(nome=nome, sobrenome=sobrenome, horas_trabalhadas=horas, valor_hora=valor)
            
            print(func.getNomeCompleto())
            print(func.getCalcularSalario())
            print(func.setIncrementarHoras(85))
            ##print(func.getFuncionário())
            
        case 6:
            raio = float(input("Digite o valor do raio: "))
            
            cir = Circulo(raio=raio)
            
            print(cir.getArea())
            print(cir.getCircunferencia())
            print(cir.getRaio())
        
        case 7:
            dia = input("Digite o dia: ")
            mes = input("Digite o mês: ")
            ano = input("Digite o ano: ")
            anotacao = input("Digite sua anotação: ")
            
            agendar = Agenda(dia=dia, mes=mes, ano=ano,anotacao=anotacao)
            
            print(agendar.getValidarData())
            ##print(agendar.getAgendamento())
            
        case 8:
            a = int(input("Digite um lado: "))
            b = int(input("Digite um lado: "))
            c = int(input("Digite um lado: "))
            
            tri = Triangulo(a=a,b=b,c=c)
            
            print(tri.calcularPerimetro())
            print(tri.getLados())
        case 9:
            nome = input("Digite seu nome: ")
            idade = int(input("Sua idade "))
            peso = float(input("Digite o seu peso: "))
            altura = float(input("Digite a sua altura: "))
            aluno= Academia(nome=nome, idade=idade, peso=peso, altura=altura)
            
            print(aluno.calcularIMC())
            print(aluno.desconto())
            
        case 10:
            modelo = input("Modelo: ")
            marca = input("Marca: ")
            cor = input("Cor: ")
            ano = input("Ano: ")
            valor = float(input("Preço: "))
            consumo = float(input("Consumoa: "))
            carro= Carro(modelo=modelo, marca=marca, cor=cor, ano=ano, valor=valor, consumo=consumo)
            
            print(carro.ligar())
            print(carro.setAbastecer(25))
            print(carro.getAndar(855))
            print(carro.verificar_nivel(855))
            print(carro.calcularImposto())
            print(carro.carrinho())
            
        case 11:
            
            numero = input("Numero: ")
            tipo = input("Tipo: ")
            serie = input("Serie: ")
            cnpj = input("CNPJ: ")
            razao_social = (input("Razão Social: "))
            data = (input("Data: "))
            valor_produtos = float(input("Valor dos Produtos: "))
            icms = float(input("ICMS: "))
            frete = float(input("Data: "))
            ipi = float(input("IPI: "))
           
            nota_fiscal= NF(numero=numero, tipo=tipo, serie=serie, cnpj=cnpj, razao_social=razao_social, data=data,valor_produtos=valor_produtos, icms= icms, frete=frete, IPI=ipi)            
            
            
            print(nota_fiscal.obterNumero())
            print(nota_fiscal.obterDataEmissão())
            print(nota_fiscal.alterarRazaoSocial())
            print(nota_fiscal.calcularValor())
            
        case 0:
            print("Obrigado, e até a proxima!")
            break