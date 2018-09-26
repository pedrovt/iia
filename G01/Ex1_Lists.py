# Guide 1, Functions to Process Lists
# 
# Introduction to Artificial Intelligence
# Pedro Teixeira, 84715, MIECT

# Functions
# 1. Dada uma lista, retorna o seu comprimento.
def lengthList(lista):
	"""Returns the length of the list"""
	if (lista == []):
		return 0
	
	return 1 + lengthList(lista[1:])

# 2. Dada uma lista de numeros, retorna a respectiva soma.
def sumOfElems(lista):
	"""Returns the sum of the elements of a numeric list (recursive solution)"""

	if (lista == []): 
		return 0

	return lista[0] + sumOfElems(lista[1:])

# 3. Dada uma lista e um elemento, verica se o elemento ocorre na lista. 
# Retorna um valor booleano.
def contains(lista, elem):
	"""Verifies if a list contains the element elem"""
	
	if (lista == []):
		return False

	return lista[0] == elem or contains(lista[1:], elem)

# 4. Dadas duas listas, retorna a sua concatenação.
# Nota: Embora seja possivel programar a concatenacão de forma recursiva, as 
# listas de Python suportam operacoes de modicação que permitem implementar a 
# concatenação sem usar qualquer tipo de processamento iterativo ou recursivo.
def concatenate(list1, list2):
	"""Concatenates two lists, list1 and list2"""
	if (list1 == []):
		return list2

	return [list1[0]] + concatenate(list1[1:], list2)

# 5. Dada uma lista, retorna a sua inversa.
def invert(lista):
	"""Inverts a list"""
	if (lista == []):
		return []

	return [lista[-1]] + invert(lista[:-1])
	#return invert(lista[1:]) + [lista[0]]
	
# 6. Dada uma lista, verica se forma uma capicua, ou seja, se, quer se leia da 
# esquerda para a direita ou vice-versa, se obtêm a mesma sequência de elementos
def isPalindromic(lista):
	"""Verifies if a numerical list is palindromic"""
	#return (lista[0] == lista[len(lista-1)]) and isPalindromic(lista[1:len(lista-2)])
	return lista == invert(lista)

# 7. Dada uma lista de listas, retorna a concatenação dessas listas.
def concatenateListOfLists(listOfLists):
	"""Concatenates the elements of the lists of a list of lists"""
	if (listOfLists == []):
		return listOfLists
		
	#return concatenate(listOfLists[0] + listOfLists, listOfLists[1:])
	return listOfLists[0] + concatenateListOfLists(listOfLists[1:])

# 8. Dada uma lista, um elemento x e outro elemento y, retorna uma lista similar
# à lista de entrada, na qual x é substituido por y em todas as ocorrências de x
def replace(lista, x, y):
	"""Replaces all occurrences in the list of x with y"""
	# if (not contains(lista, x) or not contains(lista, y)): return

	if (lista == []):
		return []

	if (lista[0] == x):
		lista[0] = y

	return [lista[0]] + replace(lista[1:], x, y)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Tests
def main():
	# Non exhaustive tests!!
	print("Testing functions...")

	list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	list2 = [10, 14, 25]
	listOfLists = [list1, list2, [4, 1, 2]]
	listEmpty = []
	

	assert list1 == [1, 2, 3, 4, 5, 6, 7, 8, 9], "List 1 changed!"
	assert list2 == [10, 14, 25], "List 2 changed!"
	assert listOfLists == [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 14, 25], [4, 1, 2]], "Lists of lists changed!"
	print("Lists: OK (lists not changed, all tests MUST work)")

	assert lengthList(list1) 	 == 9, "Error in length Test 1 "
	assert lengthList(list2) 	 == 3, "Error in length Test 2"
	assert lengthList(listEmpty) == 0, "Error in length (empty list) Test 3 "
	print("Length: OK")

	assert sumOfElems(list1)	 == 45, "Error in Sum of Elements Test 1"
	assert sumOfElems(list2) 	 == 49, "Error in Sum of Elements Test 2"
	assert sumOfElems(listEmpty) == 0,  "Error in Sum of Elements Test 3 (empty list)"
	print("Sum of Elements: OK")

	assert contains(list1, 0) 	  == False, "Error in Contains Test 1"
	assert contains(list2, 10) 	  == True,  "Error in Contains Test 2"
	assert contains(listEmpty, 5) == False, "Error in Contains Test 3 (empty list)"
	print("Contains: OK")

	assert concatenate(list1, list2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 25], "Error in Concatenate Test 1"
	assert concatenate(list2, listEmpty) == list2,  "Error in Concatenate Test 2"
	assert concatenate(listEmpty, listEmpty) == [], "Error in Concatenate Test 3"
	print("Concatenate: OK")

	assert invert(list2) == [25, 14, 10],  "Error in Invert Test 1"
	assert invert(listEmpty) == [], "Error in Invert Test 2 (empty list)"
	print("Invert: OK")

	assert isPalindromic(list1) == False, "Error in Is Palindromic Test 1"
	assert isPalindromic([1, 3, 2, 2, 3, 1]) == True,  "Error in Is Palindromic Test 2"
	assert isPalindromic([]) == True, "Error in Is Palindromic Test 3 (empty list)"
	print("Is Palindromic: OK")

	assert concatenateListOfLists(listOfLists) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 25, 4, 1, 2], "Error in Concatenate Lists of Lists Test 1"
	assert concatenateListOfLists([]) == [], "Error in Is Concatenate Lists of Lists Test 2 (empty list)"
	print("Concatenate Lists of Lists: OK")

	assert replace(list2, 10, 14) == [14, 14, 25], "Error in Replace Test 1"
	assert replace(list2, 10, 32) == [14, 14, 25], "Error in Replace Test 2"
	assert replace(list2, 14, 18) == [18, 18, 25], "Error in Replace Test 3"
	assert replace([], 1, 4) 	  == [], "Error in Replace Test 4 (empty list)"
	print("Replace: OK")

if __name__ == "__main__":
	main()
