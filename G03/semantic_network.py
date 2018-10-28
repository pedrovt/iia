

# Guiao de representacao do conhecimento
# -- Redes semanticas
# 
# Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2018
# v1.8 - 2018/10/22
#


# Classe Relation, com as seguintes classes derivadas:
#     - Association - uma associacao generica entre duas entidades
#     - Subtype     - uma relacao de subtipo entre dois tipos
#     - Member      - uma relacao de pertenca de uma instancia a um tipo
#

class Relation:
    def __init__(self,e1,rel,e2):
        self.entity1 = e1
#       self.relation = rel  # obsoleto
        self.name = rel
        self.entity2 = e2
    def __str__(self):
        return self.name + "(" + str(self.entity1) + "," + \
               str(self.entity2) + ")"
    def __repr__(self):
        return str(self)


# Subclasse Association
class Association(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,e2)

#   Exemplo:
#   a = Association('socrates','professor','filosofia')

# Subclasse Subtype
class Subtype(Relation):
    def __init__(self,sub,super):
        Relation.__init__(self,sub,"subtype",super)


#   Exemplo:
#   s = Subtype('homem','mamifero')

# Subclasse Member
class Member(Relation):
    def __init__(self,obj,type):
        Relation.__init__(self,obj,"member",type)

#   Exemplo:
#   m = Member('socrates','homem')

# classe Declaration
# -- associa um utilizador a uma relacao por si inserida
#    na rede semantica
#
class Declaration:
    def __init__(self,user,rel):
        self.user = user
        self.relation = rel
    def __str__(self):
        return "decl("+str(self.user)+","+str(self.relation)+")"
    def __repr__(self):
        return str(self)

#   Exemplos:
#   da = Declaration('descartes',a)
#   ds = Declaration('darwin',s)
#   dm = Declaration('descartes',m)

# classe SemanticNetwork
# -- composta por um conjunto de declaracoes
#    armazenado na forma de uma lista
#
class SemanticNetwork:
    def __init__(self,ldecl=[]):
        self.declarations = ldecl
    def __str__(self):
        return my_list2string(self.declarations)
    def insert(self,decl):
        self.declarations.append(decl)
    def query_local(self,user=None,e1=None,rel=None,e2=None):
        self.query_result = \
            [ d for d in self.declarations
                if  (user == None or d.user==user)
                and (e1 == None or d.relation.entity1 == e1)
                and (rel == None or d.relation.name == rel)
                and (e2 == None or d.relation.entity2 == e2) ]
        return self.query_result
    def show_query_result(self):
        for d in self.query_result:
            print(str(d))
   
    def get_assoc_names(self):
        all_relations      = set(self.query_local())
        members_relations  = set(self.query_local(rel="member")) 
        subtypes_relations = set(self.query_local(rel="subtype"))
        assocs_relations = list(all_relations - members_relations - subtypes_relations)
        return list(set(declaration.relation.name for declaration in assocs_relations))

        # or using a set comprehension
    
    def get_objects(self):
        return list(set(declaration.relation.entity1 for declaration in self.query_local(rel="subtype")))

    def get_users(self):
        return list(set(declaration.user for declaration in self.query_local()))

    def get_types(self):
        entity1s = [declaration.relation.entity1 for declaration in self.query_local(rel="subtype") ]
        entity2s = [declaration.relation.entity1 for declaration in self.declarations if declaration.relation.name in ["member", "subtype"]]
        return list(set(entity1s + entity2s))
        
        # NOT return list(set(declaration.relation.entity2 for declaration in self.query_local(rel="subtype")))
    
    # Exercise 5
    def get_local_assoc_names(self, entity=None):
        return list(set(declaration.relation.name for declaration in self.query_local() if declaration.relation.name not in ["member", "subtype"] and (declaration.relation.entity1 == entity or declaration.relation.entity2 == entity)))

    # Exercise 6 
    def get_user_decl_names(self, user):
        return list(set([declaration.relation.name for declaration in self.query_local()
                         if declaration.user == user]))

    # Exercise 7
    def get_user_decl_number(self, user):
        return len(set(declaration.relation.name for declaration in self.query_local(user=user) if declaration.relation.name not in ["member", "subtype"]))

    # Exercise 8
    def get_local_assoc_user(self, entity):
        return declaration.relation.name, declaration.user for declaration in self.query_local()
# Funcao auxiliar para converter para cadeias de caracteres
# listas cujos elementos sejam convertiveis para
# cadeias de caracteres
def my_list2string(list):
   if list == []:
       return "[]"
   s = "[ " + str(list[0])
   for i in range(1,len(list)):
       s += ", " + str(list[i])
   return s + " ]"
    

