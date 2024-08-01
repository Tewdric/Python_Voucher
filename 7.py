produto = float (input ("Digite o valor de aquisição deste produto:"))

if produto <= 50:
    desc = produto+(produto*0.45)
    print(f"O produto poderá ser vendido com o reajuste por {desc:.2f}")
elif produto >= 50:
    desc = produto+(produto*0.3)
    print(f"O produto poderá ser vendido com o reajuste por R${desc:.2f}")
