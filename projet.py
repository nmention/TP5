#Test
import random
from platform import node
from re import T
from networkx import *
import matplotlib.pyplot as plt
from itertools import combinations
import numpy as np

def fusionArrayVertex(arrayDep, arrayComplement):
    for i in range(len(arrayComplement)):
        if (arrayComplement[i] != ","):
            if arrayComplement[i] not in arrayDep:
                arrayDep.append(arrayComplement[i])


def fusionArrayEdges(arrayDep, arrayComplement):
    data = arrayComplement.split("*")

    for line in data:
        a = line.split(",")[0]
        if (len(line.split(",")) >= 2):
            b = line.split(",")[1]
            tuples = (a,b)
            arrayDep.append(tuples)

def readFile():
    vertex = []
    edge = []
    file = open("data/graph.txt","r")
    data = file.read().split("\n")   # on recupere toutes les lignes 1 par 1 dans un tableau
    for line in data:
        vertices = line.split("/")[0]
        edges = line.split("/")[1]
        fusionArrayEdges(edge,edges)
        fusionArrayVertex(vertex,vertices)

    return [vertex,edge]

class Graphe:
    def __init__(self):
        self.graph = Graph()

    def getAllNeighbors(self):
        """ Recupere tous les voisins de chaques sommet du graphe sous forme de tableau de tableau"""
        vertex = self.graph.nodes
        nodesConnected = []
        for i in range(len(vertex)): # pour chaque noeud dans le graphe
            nodesConnected.append(list(self.graph.neighbors(list(vertex)[i]))) # on recupere les voisins de CHAQUE noeuds
            nodesConnected[i].append(list(vertex)[i])

        return nodesConnected


    def getAllNodeConnectedByIndex(self, nodesConnected,index):
        """ Recupere tous les voisins directe et lointain du """
        total = []
        i= 0
        j= 1
        while (True):
            firstGroup = nodesConnected[index]
            for j in range(len(nodesConnected)): ## pour chaque valeur de la liste principale
                for z in range(len(nodesConnected[j])): ## pour chaque voisin dans appartenant au sommet j
                    if self.isLinked(nodesConnected[j],firstGroup): # si le voisin z appartenant a j est dans les voisins de i (donc que le sommet i est lie au sommet j)
                        if nodesConnected[j][z] not in total: # et si on ne l'a pas deja compte
                            total.append(nodesConnected[j][z]) # alors on l'ajoute dans les sommets reliees
            i+=1
            if (i == len(list(nodesConnected[index]))):
                break
        print (total)
        return total


    def isLinked(self,group1, group2):
        """Permet de regarder si le sommetX est connexe avec le sommetY"""
        for i in range(len(group1)):
            if group1[i] in group2:
                return True
        return False


    def isConnexe(self):
        nodesConnected = self.getAllNeighbors()
        total = self.getAllNodeConnectedByIndex(nodesConnected,1)
        if len(self.graph.nodes()) == len(total) :
            return True
        return False

    def addNodes(self,nodes):
        self.graph.add_nodes_from(nodes)

    def addEdges(self,edges):
        self.graph.add_edges_from(edges)

data = readFile();
print(data[0])
print(data)

class Edge:
    def __init__(self,edge: tuple,weight: int):
        self.edge = edge
        self.weight = weight

    def display(self):
        print("Edge :",self.edge)
        print("Weight : ",self.weight)

class Vertice:
    def __init__(self,name: str):
        self.name = name

    def display(self):
        print("Name",self.name)

class Graphe2:
    def __init__(self,vertices: list,edges: list):
        self.vertices = vertices
        self.edges = edges

    def display(self):
        print("Vertices : ",self.vertices)
        print("Edges", self.edges)

    @staticmethod
    def emptyGraph():
        graphe = Graphe2([],[])
        return graphe

    def addVertice(self,vertex:Vertice):
        self.vertices.append(vertex)

    def removeVertice(self,vertex:Vertice):
        self.vertices.remove(vertex)

    @staticmethod
    def randomGraphGenerator():
        nbOfVertices = random.randint(1,9)
        graphe = Graphe2.emptyGraph()
        for i in range(nbOfVertices):
            graphe.addVertice(Vertice(str(random.randint(0,10))))




B = Graphe()


B.addNodes(data[0])
B.addEdges(data[1])

print(B.isConnexe())

listeVertices = []
vertice1 = Vertice("Paris")
vertice2 = Vertice("Lyon")
vertice3 = Vertice("Ajaccio")
listeVertices.append(vertice1)
listeVertices.append(vertice2)
listeVertices.append(vertice3)

listEdges = []
edge1 = Edge((vertice1,vertice2),5)
edge2 = Edge((vertice2,vertice3),2)
edge3 = Edge((vertice3,vertice1),1)
listEdges.append(edge1)
listEdges.append(edge2)
listEdges.append(edge3)

graphe2 = Graphe2(listeVertices,listEdges)
for i in graphe2.vertices:
    i.display()
for i in graphe2.edges:
    i.display()
graphe2.display()







