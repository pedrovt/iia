
from bayes_net import *

# Exemplo dos acetatos:

bn = BayesNet()

# bn.add('r',[],0.001)
# bn.add('t',[],0.002)

# bn.add('a',[('r',True ),('t',True )],0.950)
# bn.add('a',[('r',True ),('t',False)],0.940)
# bn.add('a',[('r',False),('t',True )],0.290)
# bn.add('a',[('r',False),('t',False)],0.001)

# bn.add('j',[('a',True )],0.900)
# bn.add('j',[('a',False)],0.050)

# bn.add('m',[('a',True )],0.700)
# bn.add('m',[('a',False)],0.100)

# conjunction = [('j',True),('m',True),('a',True),('r',False),('t',False)]

bn.add('ST', [], 0.60)
bn.add('UPAL', [], 0.65)

bn.add('CP', [('ST', True) , ('PA', False)], 0.01)
bn.add('CP', [('ST', True) , ('PA', True) ], 0.02)
bn.add('CP', [('ST', False), ('PA', False)], 0.001)
bn.add('CP', [('ST', False), ('PA', True) ], 0.011)

bn.add('CENL', [('ST', True) ], 0.9)
bn.add('CENL', [('ST', False)], 0.001)

bn.add('PA', [('UPAL', True) ], 0.25)
bn.add('PA', [('UPAL', False)], 0.1)

bn.add('FURE', [('UPAL', True) , ('PA', False)], 0.9)
bn.add('FURE', [('UPAL', True) , ('PA', True) ], 0.9)
bn.add('FURE', [('UPAL', False), ('PA', False)], 0.01)
bn.add('FURE', [('UPAL', False), ('PA', True) ], 0.1)

conjunction = [('ST', True), ('UPAL', True), ('CENL', False), ('CP', True), ('PA', True), ('FURE', False) ]
print(bn.jointProb(conjunction))
print(bn.dependencies)

