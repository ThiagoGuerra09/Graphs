"""Entrada nome do arquivo e e o numero do vertice do grafo"""

"""Saida: 
-grau de saida(todos as arestas que saem do vertice)
-grau de entrada(todas as arestas que saem do vertice)
-sucessores(vertices para qual são os destinos das relações)
-predecessores(vertices para qual representam o começo da relação)
"""
import re
arq = input("Digite o nome do arquivo:\n")
entrada = input('Digite o numero do vertice\n')
file = open(arq,"r")
lista = (file.readlines())
del lista[0]
lista1=[] 
lista2=[]    
grausaida=0
grauentrada=0
#sucessores
for i in lista:
    i=i.strip('\n').strip(' ')
    i=re.sub(r"\s+", " ", i)
    i=i.split(' ')
    if i[0] == entrada:
        lista1.append(i[1])
        grausaida+=1
#predecessor
for n in lista:
    n=n.strip('\n').strip(' ')
    n=re.sub(r"\s+", " ", n)
    n=n.split(' ')
    if n[1]== entrada:
        lista2.append(n[0])
        grauentrada+=1
print(f'O grau de saida é {grausaida}')
print(f'O grau de entrada é: {grauentrada}')
print(f'Os predecessores são:{lista2}')
print(f'Os sucessores são:{lista1}')
