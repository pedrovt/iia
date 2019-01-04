# OLD


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
#  (c) Luis Seabra Lopes, Introducao a Inteligencia Artificial, 2012-2014

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
    def __init__(self,state,parent, depth, cost, heuristic): 
        self.state = state
        self.parent = parent
        self.depth = depth
        self.children = []
        self.cost = cost
        self.heuristic = heuristic	    # TODO Ex11

    #TODO ex5
    def addChildren(self, c):
        self.children += c
        
    #TODO Exercício 1
    def inParent(self, state):
        if (self.parent == None):
            return False

        if self.parent.state == state:
            return True

        return self.parent.inParent(state)

    def __str__(self):
        return "no(" + str(self.state) + "," + str(self.parent) + ",depth: " + str(self.depth) + ",cost: " + self.cost + ", estimated cost (heuristic) " + self.heuristic + ")"
    def __repr__(self):
        return str(self)

# Arvores de pesquisa
class SearchTree:

    # construtor
    def __init__(self,problem, strategy='breadth'): 
        self.problem = problem
        root = SearchNode(problem.initial, None, 0, 0, self.problem.domain.heuristic(problem.initial, problem.goal))
        self.open_nodes = [root]
        self.strategy = strategy
        self.cost = None
        self.nodes = 1
        self.leafs = 0
        self.costly_nodes = [root]
        
        self.averageDepth = 0
        self.sumDepth = 0

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
            #print(node)
            if self.problem.goal_test(node.state):
                self.averageDepth = self.sumDepth / self.nodes
                return self.get_path(node), node.depth, node.cost, self.averageDepth
            lnewnodes = []
            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state,a)
                cost = node.cost + self.problem.domain.cost(node.state, a)
                new_search_node = SearchNode(newstate, node, node.depth + 1, cost, self.problem.domain.heuristic(newstate, self.problem.goal))

                #! ex 15
                if self.costly_nodes[0].cost == cost:
                    #self.costlyNodes.extend(new_search_node)
                    self.costly_nodes += [new_search_node]
                elif self.costly_nodes[0].cost > cost:
                    self.costly_nodes = [new_search_node]

                #! ex 16
                self.sumDepth += new_search_node.depth

                lnewnodes += [new_search_node]  #! not node.state, a. Not from where I am to the goal but from the next step to the goal
                self.nodes += 1

            if (lnewnodes == []):
                self.leafs += 1
            self.add_to_open([nn for nn in lnewnodes if 
                not node.inParent(nn.state)
                and (nn.depth < limit if limit else True)])
            
            # TODO changed for ex. 5
            #children = [newNode for newNode in lnewnodes if not node.inParent(
            #    newNode.state) and (newNode.depth < limit if limit else True)]
            
            #node.addChildren(children)
            #self.add_to_open(children)
            # filter the visited nodes (or using an if in the previous for statement). None is always false

        
        return None

    # juntar novos nos a lista de nos abertos de acordo com a estrategia
    def add_to_open(self,lnewnodes):
        if self.strategy == 'breadth':
            self.open_nodes.extend(lnewnodes) # add to the end of the list
        elif self.strategy == 'depth':
            self.open_nodes[0:0] = lnewnodes  # add to the beginning
        elif self.strategy == 'uniform':      # order by the cost (choosing the )
            # TODO Ex 10           
            #self.open_nodes.sort(key=lambda node: node.cost)
            self.open_nodes = sorted(
                self.open_nodes + lnewnodes, key=lambda node: node.cost)
        elif self.strategy == 'greedy':      # order by the estimated cost (choosing the )    
            #self.open_nodes.sort(key=lambda node: node.cost)
            self.open_nodes = sorted(
                self.open_nodes + lnewnodes, key=lambda node: node.heuristic)
        elif self.strategy == 'a*':      # order by the cost + estimated cost (choosing the )    
            #self.open_nodes.sort(key=lambda node: node.cost)
            self.open_nodes = sorted(
                self.open_nodes + lnewnodes, key=lambda node: node.cost + node.heuristic)

