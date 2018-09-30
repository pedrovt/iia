# Guide 1, Functions with Lambda Expressions
#
# Introduction to Artificial Intelligence
# Pedro Teixeira, 84715, MIECT

import math

# Functions
# 1. (Implementar na forma de uma expressão-lambda:) Dado um número inteiro, retorna True
# caso o número seja ímpar, e False caso contrário.
oddNum = lambda num : num % 2 != 0

# 2. (Implementar na forma de uma expressão-lambda:) Dado um número, retorna True caso o número seja positivo, e False caso contrário.
posNum = lambda num : num > 0

# 3. (Implementar na forma de uma expressão-lambda:) Dados dois números, x e y, retorna True caso |x| < |y|, e False caso contrário.
compareAbsNums = lambda x, y : abs(x) < abs(y)

# 4. (Implementar na forma de uma expressao-lambda:) Dado um par (x; y), representando coordenadas cartesianas de um ponto no plano XY, retorna um par (r, Θ), correspondente as coordenadas polares do mesmo ponto.
#coordCartToPolar = lambda coords: math.sqrt(coords[0]**2, coords[1]**2), math.atan(coords[1]/coords[0])

# 5. Dadas três funções de duas entradas, f, g e h, retorna uma função de três entradas, x, y e z, cujo resultado é dado por: h(f(x, y), g(y, z).
functs = lambda f,g,h : lambda x,y,z : h(f(x, y), g(y,z))

# 6. Dada uma lista e uma função booleana unária, retorna True caso a função também retorne True para todos os elementos da lista, e False caso contrário. ( Quanticador universal ) 
ex6 = lambda lista, f : [elem for elem in lista if not f(elem)] == []


# 9. Dada uma lista com pelo menos um elemento e uma relação de ordem (ou seja, uma função booleana binaria usada para comparação elemento a elemento), retorna o menor elemento da lista de acordo com essa relação de ordem.
def smallerElem(lista, compare):
    if (lista == []):
        return []

    if (len(lista) == 1):
        return lista[0]

    if (compare(lista[0], lista[1])):
        return smallerElem([lista[0]] + lista[2:], compare)

    return smallerElem([lista[1]] + lista[2:], compare)

# 10. Dada uma lista com pelo menos um elemento e uma relação de ordem, retorna um par contendo o menor elemento da lista, de acordo com essa relação de ordem, e uma lista com os restantes elementos.
def smallerAndOtherElem(lista, compare):
    elem = smallerElem(lista, compare)
    otherElems = [e for e in lista if e != elem]
    return elem, otherElems


# Selection sort with compare filter
def removeCount(lista, elem):
    """Removes elem from the list and returns a tuple (elements in the list that are different from elem, #occurrences of elem)"""
    if (lista == []):
        return [], 0

    a, b = removeCount(lista[1:], elem)

    if (lista[0] == elem): 
        return a, 1 + b
    
    return [lista[0]] + a, 0 + b

def selectionSort(lista, compare):
    if (lista == []):
        return []
    elem, otherElems = smallerAndOtherElem(lista, compare)
    return [elem] + selectionSort(otherElems, compare)



# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Tests
def main():
    # Non exhaustive tests!!
    print("Testing functions...")
    
    assert oddNum(4)  == False
    assert oddNum(4)  == False
    assert oddNum(3)  == True

    assert posNum(5)  == True
    assert posNum(5)  == True
    assert posNum(0)  == False
    assert posNum(-3) == False
    
    assert compareAbsNums(5, 8)  == True
    assert compareAbsNums(0, -3) == True
    assert compareAbsNums(-9, 5) == False
    
    #print(coordCartToPolar((5, 8)))

    assert(ex6([2, 4, 6, 8, 10], lambda num : num % 2 == 0)) == True
    assert(ex6([2, 4, 7, 8, 10], lambda num : num % 2 == 0)) == False


    print(smallerElem([3, 4, 1, 6], lambda x, y: x < y))
    print(smallerAndOtherElem([3, 4, 1, 6], lambda x, y: x < y))
    print(selectionSort([3, 4, 1, 6], lambda x, y: x < y))


if __name__ == "__main__":
    main()

