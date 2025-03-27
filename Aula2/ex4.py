lista = [1, 2, 3, 2, 5, 3, 7, 5, 9, 10]

def duplicados(lista):
    lista = list(set(lista))
    return lista

print("Lista sem Duplicados: " + str(duplicados(lista)))