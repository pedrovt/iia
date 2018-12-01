
from constraintsearch import *


def bicicleta_constraint(amigo1, constrains1, amigo2, constrains2):
    bicicleta1, chapeu1 = constrains1	# friends having the bicicleta1, chapeu1
    bicicleta2, chapeu2 = constrains2

    # Can't use things from him/herself
    # orif (amigo1 == bicicleta1 or amigo1 == chapeu1)
    if amigo1 in [bicicleta1, chapeu1]:
        return False
    if amigo2 in [bicicleta2, chapeu2]:
        return False
    
    # Can't have things from the same friend
    if bicicleta1 == chapeu1 or bicicleta2 == chapeu2:
        return False

    if bicicleta1 == bicicleta2 or chapeu1 == chapeu2:
        return False

    return True

def make_constraint_graph():
    return { (X,Y):bicicleta_constraint for X in amigos for Y in amigos if X != Y}

amigos = ["Andre", "Bernardo", "Claudio"]

def make_domains():
    return { amigo:[(bicicleta, chapeu) for bicicleta in amigos for chapeu in amigos] for amigo in amigos}

cs = ConstraintSearch(make_domains(),make_constraint_graph())

print(cs.search())

