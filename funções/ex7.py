def salarioFinal (s,d):
    div = s/d
    
    if d > 40:
        div = div+(div*0.5)
        return div
    
    return div

print(f'Ganho por hora trabalhada: R${salarioFinal(1415,41):.2f}')