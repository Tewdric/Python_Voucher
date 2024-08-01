n1 = float (input("Digite sau primeira nota: "))
n2 = float(input("Digite a segunda nota:"))

if (n1 <= 0 or n1 >=10) or (n2 <=0 or n2 >=10):
    print("Notas validas!")
  
else:
    print("Notas invalidas") 
    media = (n1 + n2)/2
    print(f'A media das suas notas são: {media}')