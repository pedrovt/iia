
from constraintsearch import *


def map_constraint(p1,c1,r2,c2):
    if c1 == c2:
        return False

    return True

def make_constraint_graph(n):
    return { (X,Y):map_constraint for X in paises for Y in paises[X]}

paises = { "A": "BDE",
           "B": "ACE",
           "C": "BDE",
           "D": "ACE",
           "E": "ABCD",
         }

def make_domains(n):
    cores = "rgbyw"

    return { p:cores for p in paises }

cs = ConstraintSearch(make_domains(10),make_constraint_graph(10))

print(cs.search())

