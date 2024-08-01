def valor_multa(peso):
    
    if peso > 50:
        multa = peso-50
        total_multa = multa * 4

        return print(f'Você paragará multa pois excedeu o peso minimo no valor de : R${total_multa}')
    else:
        return print(f"A pesca foi boa")

valor_multa(45)