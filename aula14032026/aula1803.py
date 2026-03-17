#LISTAS:
#índices:   0        1       2        3       4
nomes = ['Matheus','Alice','Caio','Larissa','Miguel']
print(nomes)

# print(nomes[0])

# #DONTPAD

# nomes = ['Matheus','Alice','Caio','Larissa','Miguel','Rafael']

# nome1 = nomes[0]

# print(nomes[-1])
# print(nomes[-2])
# print(nomes[-3])
# print(nomes[-4])
# print(nome1)

# primeira_parte=nomes[0:3]
# print(primeira_parte)
# segunda_parte=nomes[3:6]
# print(segunda_parte)

# print(len(nomes)) #saber a quantidade de elementos das listas

#lista1 = [] - mutavel
 #nomes = ['Matheus','Alice','Caio','Larissa','Miguel','Rafael']

#tupla1 = () - fixo
nomes_tupla=tuple(nomes)
print(nomes_tupla)

#set1 = () ou {} - mutavel e desordenado
nomes_set=set(nomes)
print(nomes_set)

#dict1 = {:} - elementos e seus significados
nomes_dict={'nome1':'Matheus',
            'nome2':'Alice',
            'nome3':'Caio',
            'nome4':'Larissa',
            'nome5':'Miguel',
            'nome6':'Rafael'} #podem ser associados apenas a números
print(nomes_dict)

