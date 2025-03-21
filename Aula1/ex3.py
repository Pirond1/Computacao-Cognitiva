valor = float(input("Informe o Valor da Compra: "))
if valor > 100:
    valor = valor * 0.9
    print(f"Valor da Compra: R$ {valor:.2f}")
else:
    print(f"Valor da Compra: R$ {valor:.2f}")