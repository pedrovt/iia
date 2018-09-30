# Guide 1, Developing Classes
#
# Introduction to Artificial Intelligence
# Pedro Teixeira, 84715, MIECT


# Pretende-se desenvolver um programa que seja capaz de representar uma árvore 
# genealógica e que possa responder a perguntas sobre as relações existentes.

# 1. Proponha classes para representar as relações familiares Pai(x; y) e 
# Mae(x; y), juntamente os respectivos métodos de inicialização e conversão 
# para cadeia de caracteres.
class Person:
    # The node of the family tree

    # Fields: Name, Parents (Dad, Mom), Children

    # CTOR & Predefined Methods
    def __init__ (self, name = "Unnamed", dad = None, mom = None, child = None):
        self.name = name
        self.set_dad(dad)
        self.set_mom(mom)
        self.children = []
        self.set_children(child)

    def __str__ (self):
        return self.name

    # Setters
    def set_dad(self, dad):
        self.dad = Dad(dad, self)

    def set_mom(self, mom):
        self.mom = Mom(mom, self)

    def set_children(self, child):
        if (isinstance(child, list)):
            for c in child:
                self.set_children(c)
        else:
            child.set_dad(self)
            self.children = self.children + [child]

    # Getters
    def get_dad(self):
        return self.dad

    def get_mom(self):
        return self.mom

     # 3. Desenvolva um método que, dado um indivíduo, retorna um par formado
    # pelos seus pais.
    def get_parents(self, person):
        return person.get_mom(), person.get_dad()

    # 4. Desenvolva um método que, dado um indivíduo, retorna uma lista com os
    # seus filhos.
    def get_children(self):
        return self.children  

        # 5. Desenvolva um método que, dados dois indivíduos, retorna True caso o
    # primeiro seja progenitor do segundo, e False caso contrário.
    def isParentOf(self, x, y):
        return x.get_children.contains(y)

    # 6. Desenvolva um método que, dados dois indivíduos, retorna True caso o
    # primeiro seja antepassado do segundo, e False caso contrário.
    def isChildrenOf(self, x, y):
        return self.isParentOf(y, x)

class Dad:
    def __init__ (self, x, y):  # x and y are Person nodes
        """Constructor"""
        self.x = x
        self.y = y

    def __str__ (self):
        """String representation"""
        return "Dad " + str(self.x) + " of " + str(self.y) 

class Mom:
    def __init__(self, x, y):
        """Constructor"""
        self.x = x
        self.y = y

    def __str__(self):
        """String representation"""
        return "Mom " + str(self.x) + " of " + str(self.y)

# 2. Proponha uma classe para representar uma família (ou genealogia) através 
# de uma colecção de relações familiares, juntamente os respectivos métodos de 
# inicialização e conversão para cadeia de caracteres.
class Family:
    def __init__ (self, name = "Unnamed", root = Person()):
        """Initializes an empty family with the given name"""
        self.name = name
        self.root = root

    def __str__ (self):
        return "Family " + self.name + ":\n" + self._printMembers(self.root)

    def _printMembers (self, node, indent = 0):
        # Print the parents of the node
        print(str(node.get_dad()))
        print("\t" * indent  + str(node.get_mom()))

        # Print the node
        print("\t" * (indent + 1) + str(node))
        
        # Print the children of the node
        children = node.get_children()
        for child in children:
            self._printMembers(child, (indent + 1))


def main():
    p   = Person("A")
    fam = Family("Smith", p)

    p2 = Person("B")
    p.set_children(p2)
    p.set_children(Person("C"))
    p.set_children(Person("D"))

    p2.set_children(Person("E"))

    print(str(fam))

if __name__ == "__main__":
    main()
