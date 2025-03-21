km = float(input("Informe a Distância da Viagem: "))
if km <= 200:
    preco = km * 0.5
else:
    preco = km * 0.45

print(f"Valor Total da Viagem: {preco:.2f}")