lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def maiormenor(lista):
    maior = max(lista)
    menor = min(lista)
    lista = [maior, menor]
    return lista

print("A Lista com o Maior e o Menor número é: " + str(maiormenor(lista)))