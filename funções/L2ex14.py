def economia(km,litros):
    consumo = km/litros
    
    if consumo < 8:
        return print('Gasta Muito!')
    elif consumo >= 8 and consumo <= 15:
        return print('Economico!')
    else:
        return print('Super Economico!')


print(economia(100,4))