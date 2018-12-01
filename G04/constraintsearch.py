# Pesquisa para resolucao de problemas de atribuicao
# 
# Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2016
#


class ConstraintSearch:

    # domains é um dicionário com o domínio de cada variável;
    # constaints e' um dicionário com a restrição aplicável a cada aresta;
    def __init__(self,domains,constraints):
        self.domains = domains
        self.constraints = constraints


    # domains é um dicionário com os domínios actuais
    # de cada variável
    # ( ver acetato "Pesquisa com propagacao de restricoes
    #   em problemas de atribuicao - algoritmo" )
    def search(self,domains=None):
        
        if domains==None:
            domains = self.domains

        # se alguma variavel tiver lista de valores vazia, falha
        if any([lv==[] for lv in domains.values()]):
            return None

        # se nenhuma variavel tiver mais do que um valor possivel, sucesso
        if all([len(lv)==1 for lv in list(domains.values())]):
            # se valores violam restricoes, falha
            # ( verificacao desnecessaria se for feita a propagacao
            #   de restricoes )
            for (var1,var2) in self.constraints:
                constraint = self.constraints[var1,var2]
                if not constraint(var1,domains[var1][0],var2,domains[var2][0]):
                    return None 
            return { v:lv[0] for (v,lv) in domains.items() }
       
        # continuação da pesquisa
        # ( falta fazer a propagacao de restricoes )
        for var in domains.keys():
            if len(domains[var])>1:
                for val in domains[var]:
                    newdomains = dict(domains)  #cópia
                    newdomains[var] = [val]

                    #remove repeated eelements
                    for other_var in [v for v in domains if v != var]:
                        if val in newdomains[other_var]:
                            newdomains[other_var] = [v for v in newdomains[other_var] if v != val]   
                        for other_val in newdomains[other_var]:
                            newdomains[other_var] = [other_val for other_val in newdomains[other_var] if self.constraints[var, other_var](var,newdomains[var][0], other_var, other_val) ]                
                    # (ALMOST) A SOLUTION
                    # for var_ in newdomains:
                    #     if (var_ != var):
                    #         print(var_)
                    #         print(newdomains[var_])
                    #         print(set(newdomains[var_]))
                    #         print(set([val]))
                    #         print(set(newdomains[var_]) - set([val]))
                    #         print("\n\n\n")
                    #         newdomains[var_] = [set(newdomains[var_]) - set([val])]
                    solution = self.search(newdomains)
                    if solution != None:
                        return solution
        return None


