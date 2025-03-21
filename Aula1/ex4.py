altura = float(input("Informe a Altura em Metros: "))
peso = float(input("Informe o Peso em Quilos: "))
imc = (peso / (altura ** 2))

if imc < 18.5:
    print("Abaixo do Peso!")
elif imc < 24.9:
    print("Peso Normal!")
elif imc < 29.9:
    print("Sobrepeso!")
else:
    print("Obesidade!")