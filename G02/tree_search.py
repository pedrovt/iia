
# Modulo: tree_search
# 
# Fornece um conjunto de classes para suporte a resolucao de 
# problemas por pesquisa em arvore:
#    SearchDomain  - dominios de problemas
#    SearchProblem - problemas concretos a resolver 
#    SearchNode    - nos da arvore de pesquisa
#    SearchTree    - arvore de pesquisa, com metodos para 
#                    a respectiva construcao
#
#  (c) Luis Seabra Lopes
#  Introducao a Inteligencia Artificial, 2012-2018,
#  Inteligência Artificial, 2014-2018

from abc import ABC, abstractmethod

# Dominios de pesquisa
# Permitem calcular
# as accoes possiveis em cada estado, etc
class SearchDomain(ABC):

    # construtor
    @abstractmethod
    def __init__(self):
        pass

    # lista de accoes possiveis num estado
    @abstractmethod
    def actions(self, state):
        pass

    # resultado de uma accao num estado, ou seja, o estado seguinte
    @abstractmethod
    def result(self, state, action):
        pass

    # custo de uma accao num estado
    @abstractmethod
    def cost(self, state, action):
        pass

    # custo estimado de chegar de um estado a outro
    @abstractmethod
    def heuristic(self, state, goal_state):
        pass

# Problemas concretos a resolver
# dentro de um determinado dominio
class SearchProblem:
    def __init__(self, domain, initial, goal):
        self.domain = domain
        self.initial = initial
        self.goal = goal
    def goal_test(self, state):
        return state == self.goal

# Nos de uma arvore de pesquisa
class SearchNode:
    def __init__(self,state,parent,cost, depth): 
        self.state  = state
        self.parent = parent
        self.cost   = cost	#*Question 4
        self.depth	= depth

    def __str__(self):
        return "no(" + str(self.state) + "," + str(self.parent) + ")"
    def __repr__(self):
        return str(self)

    #* Question 1 : method to verify if a SearchNode with the given state is a parent of the current SearchNode
    def inParent(self, state):
        if (self.parent == None):
            return False

        if (self.parent.state == state):
            return True
        
        return self.parent.inParent(state)

# Arvores de pesquisa
class SearchTree:

    # construtor
    def __init__(self,problem, strategy='breadth'): 
        self.problem = problem
        root = SearchNode(problem.initial, None, 0, 0)
        self.open_nodes = [root]
        self.strategy = strategy
        self.cost = 0       #* Question 5
        self.length = 0	    #* Question 7

    # obter o caminho (sequencia de estados) da raiz ate um no
    def get_path(self,node):
        if node.parent == None:
            return [node.state]
        path = self.get_path(node.parent)
        path += [node.state]
        return(path)

    # procurar a solucao
    def search(self, limit=None):
        while self.open_nodes != []:
            node = self.open_nodes.pop(0)
            if self.problem.goal_test(node.state):
                self.cost = node.cost
                self.length = node.depth
                return self.get_path(node), node.cost, node.depth
            lnewnodes = []
            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state,a)
                lnewnodes += [SearchNode(newstate,node, self.problem.domain.cost(node.state, a) + node.cost, node.depth + 1)]

            #* Question 1 : only add nodes who are not parents of the current node
            #*! Question 8 : only add nodes with depth < limit (if limit exists)
            self.add_to_open([nodes for nodes in lnewnodes if not node.inParent(nodes.state) and nodes.depth < limit if limit else True]) 
        return None

    # juntar novos nos a lista de nos abertos de acordo com a estrategia
    def add_to_open(self,lnewnodes):
        if self.strategy == 'breadth':
            self.open_nodes.extend(lnewnodes)
        elif self.strategy == 'depth':
            self.open_nodes[:0] = lnewnodes
        elif self.strategy == 'uniform':    #* Question 4 (Uniform Tree Search)
            # Add to the open_nodes list the lnewnodes and sort the result by cost
            sorted(self.open_nodes + lnewnodes, key = lambda search_node : search_node.cost)
            pass

