# Guide 2, Functions to Process Lists and Tuples
#
# Introduction to Artificial Intelligence
# Pedro Teixeira, 84715, MIECT

# Functions
# 1. Dada uma lista de pares, produzir um par com as listas dos primeiros e 
# segundos elementos desses pares.
# separar [(a1, b1), ... (an, bn)] = ([a1, ... an], [b1, ... bn])
def split(lista):
    """Splits a list of tuples into a tuple of two lists, each one containing the first and the second elements of the given tuples, ie [(a1, b1), ... (an, bn)]) = ([a1, ... an], [b1, ... bn]"""
    if (lista == []):
        return [], []

    r = split(lista[1:])

    return [lista[0][0]] + r[0], [lista[0][1]] + r[1]

# 2. Dada uma lista l e um elemento x, retorna um par formado pela lista dos 
# elementos de l diferentes de x e pelo numero de ocorrências x em l. 
# Exemplo:
# remove_e_conta ([1, 6, 2, 5, 5, 2, 5, 2], 2) --> ([1, 6, 5, 5, 5], 3)
def removeCount(lista, elem):
    """Removes elem from the list and returns a tuple (elements in the list that are different from elem, #occurrences of elem)"""
    if (lista == []):
        return [], 0

    a, b = removeCount(lista[1:], elem)

    if (lista[0] == elem): 
        return a, 1 + b
    
    return [lista[0]] + a, 0 + b

# 3. Dada uma lista, retorna o numero de ocorrencias de cada elemento, na forma 
# de uma lista de pares (elemento,contagem).
def countElems(lista):
    """Returns a list of tuples (element, #occurrences of elem), one for each element."""
    if (lista == []):
        return []
    
    elem = lista[0]
    newList, count = removeCount(lista, elem)

    return [(elem, count)] + countElems(newList)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Tests
def main():
    # Non exhaustive tests!!
    
    print("Testing functions...")

    assert split([(5, 4), (3, 2), (1, 0)]) == (
        [5, 3, 1], [4, 2, 0]), "Error in Split Test 1"
    print("Split: OK")
    
    assert removeCount([1, 6, 2, 5, 5, 2, 5, 2], 2) == ([1, 6, 5, 5, 5], 3), "Error in Remove+Count Test 1"
    print("Remove+Count: OK")

    assert countElems([1, 6, 2, 5, 5, 2, 5, 2]) == [(1, 1), (6, 1), (2, 3), (5, 3)], "Error in Count Elements Test 1"
    print("Count Elements: OK")

if __name__ == "__main__":
    main()
