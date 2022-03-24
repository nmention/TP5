from classes.Graphe import Graphe
import time

def readFile():
    vertex = []
    edge = []
    file = open("data/graph.txt", "r")
    # on recupere toutes les lignes 1 par 1 dans un tableau
    data = file.read().split("\n")
    for line in data:
        vertices = line.split("/")[0]
        edges = line.split("/")[1]
        poid = line.split("-")[0]
        fusionArrayEdges(edge, edges, poid)
        fusionArrayVertex(vertex, vertices)

    return [vertex, edge]

def fusionArrayVertex(arrayDep, arrayComplement):
    for i in range(len(arrayComplement)):
        if (arrayComplement[i] != ","):
            if arrayComplement[i] not in arrayDep:
                arrayDep.append(arrayComplement[i])


def fusionArrayEdges(arrayDep, arrayComplement,poid):
    data = arrayComplement.split("*")
    if len(arrayComplement.split("-")) > 1:
        poid = arrayComplement.split("-")[1]
    for line in data:
        a = line.split("-")[0]
        c = a.split(",")[0]
        print(a)
        if (len(line.split(",")) >= 2):
            b = a.split(",")[1]
            tuples = (c, b)
            arrayDep.append([tuples, int(poid)])


def measureTime(fct):
    start_time = time.time()
    print(start_time)
    fct()
    end_time = time.time()
    print(end_time)
    exec_time = current_nano_time(end_time - start_time)
    print("Le temps d'exécution est de %s ns" %exec_time)


def current_nano_time(nb):
    return nb * 1000000000



vertices = ['A', 'B','C','D']

listEdges = [ [ (1, 2),5], [(1,3),8 ], [(1,4),12],[ (2,3),7],[(2,4),2 ], [(3,4),3] ]
listEdges2 = [ [ (1, 2),5], [(1,3),8 ] ]

graphe = Graphe(vertices, listEdges)

sommets = ['A', 'B','C','D','E','F','G','H','I','J']

sommets2 = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O']
sommets3 = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']
edges = []
graphe3 = Graphe([], [])
graphe4 = Graphe([], [])
graphe5 = Graphe([], [])
graphe3.generateGrapheCompletAleatoire(sommets)
graphe4.generateGrapheCompletAleatoire(sommets2)
graphe5.generateGrapheCompletAleatoire(sommets3)
graphe3.display()
graphe5.display()

dijsktra = graphe3.disjkstra
dijsktra2 = graphe4.disjkstra
dijsktra3 = graphe5.disjkstra


measureTime(dijsktra)
measureTime(dijsktra2)
measureTime(dijsktra3)

graphe4 = Graphe([], [])
data= readFile()
graphe5 = Graphe(data[0], data[1])

# graphe.printMarquage()
