def ordenar_lista(lista, expresion=None):
    return sorted(lista, reverse=expresion)

lista_desordenada = [3, 1, 4, 1, 5, 9, 2, 6, 5]
expresion_verdadera = True
expresion_falsa = False

print("Lista ordenada ascendente:", ordenar_lista(lista_desordenada, False))
print("Lista ordenada descendente:", ordenar_lista(lista_desordenada, True))
print("Lista ordenada ascendente:", ordenar_lista(lista_desordenada, False))