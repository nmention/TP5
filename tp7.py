from classes.Graphe import Graphe
import time


vertices = ['A','B','C','D']

listEdges = [ [ (1,2),5], [(1,3),8 ], [(1,4),12],[ (2,3),7],[(2,4),2 ], [(3,4),3] ]
listEdges2 = [ [ (1,2),5], [(1,3),8 ] ]

graphe = Graphe(vertices, listEdges)
#Graphe = Graphe(vertices, listEdges2)



#print(graphe.noeudLePlusProche(graphe.getAllVertices()[0])[0].name)

#print(algoGlouton[0],algoGlouton[1])
#graphe.display()
#graphe.printMarquage()

print(graphe.isConnexe())
#print(Graphe.isConnexe())

def measureTime(fct):
    start_time = time.time()
    print(start_time)
    fct()
    end_time = time.time()
    print(end_time)
    exec_time = current_nano_time(end_time - start_time)
    print("Le temps d'exécution est de %s ns"%exec_time)

def current_nano_time(nb):
    return nb * 1000000000

#print(graphe.disjkstra())

#print(graphe.matrice2d())

sommets = ['A','B','C','D','E','F','G','H','I','J']
edges = []
graphe3 = Graphe([],[])
graphe3.generateGrapheCompletAleatoire(sommets)
graphe3.display()

dijsktra = graphe3.disjkstra


measureTime(dijsktra)

#graphe.printMarquage()