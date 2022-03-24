from classes.Graphe2 import Graphe2
import time


vertices = ['A','B','C','D']

listEdges = [ [ (1,2),5], [(1,3),8 ], [(1,4),12],[ (2,3),7],[(2,4),2 ], [(3,4),3] ]
listEdges2 = [ [ (1,2),5], [(1,3),8 ] ]

graphe = Graphe2(vertices, listEdges)
graphe2 = Graphe2(vertices, listEdges2)



#print(graphe.noeudLePlusProche(graphe.getAllVertices()[0])[0].name)

#print(algoGlouton[0],algoGlouton[1])
#graphe.display()
#graphe.printMarquage()

print(graphe.isConnexe())
print(graphe2.isConnexe())
def measureTime(graphe):
    start_time = time.time()
    graphe.disjkstra2()
    end_time = time.time()
    exec_time = current_nano_time(end_time - start_time)
    print("Le temps d'exécution est de %s ns"%exec_time)

def current_nano_time(nb):
    return nb * 1000000000

measureTime(graphe)
print(graphe.disjkstra2())


arrayTotal =[]
verticesGraphe = graphe.getAllVertices()
for i in range(len(verticesGraphe)):
    ligne = []
    for j in range(len(verticesGraphe[i].matrice)):
        vertex,weight = verticesGraphe[i].matrice[j][0].name,verticesGraphe[i].matrice[j][1]
        ligne.append((vertex,weight))
    arrayTotal.append(ligne)

print(arrayTotal)

#graphe.printMarquage()