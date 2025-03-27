lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

def somarlistas (lista1, lista2):
    if len(lista1) != len(lista2):
        print("Listas de Tamanhos Diferentes!")
    else:
        soma_listas = []
        for l in range(len(lista1)):
            soma_listas.append(lista1[l] + lista2[l])
            
    
    return soma_listas

print("Lista 1: " + str(lista1))
print("Lista 2: " + str(lista2))
print("Lista Somada: " + str(somarlistas(lista1, lista2)))