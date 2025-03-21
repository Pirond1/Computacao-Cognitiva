soma = 0

for n in range(5):
    nota = float(input(f"Digite a nota {n+1}: "))
    soma += nota
media = soma / 5
print(f"A Média é {media:.2f}")