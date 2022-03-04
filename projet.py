#Test
from networkx import *
import matplotlib.pyplot as plt
from itertools import combinations

liste = []

def readFile():
    file = open("data/graph","r")
    print(file.read())
    file.close()
readFile()

class Graphe:
    def __init__(self):
        self.graph = Graph()

    def CC(self,sommet):
        cc = []
        aTraiter = [sommet]
        while aTraiter != []:
            for voisins in list(self.graph.neighbors(aTraiter[0])):
                if voisins not in cc and voisins not in aTraiter :
                    aTraiter.append(voisins)
            cc.append(aTraiter[0])
            aTraiter.remove(aTraiter[0])
            compo=Graph()
            compo.add_nodes_from(cc)
            for (a,b) in self.graph.edges():
                if a in cc : 
                    compo.add_edge(a,b) 
            return compo


    def isConnexe(self):
        return len(self.graph.nodes()) == len(self.CC(list(self.graph.nodes())[0]).nodes())

    def addNodes(self,nodes):
        self.graph.add_nodes_from(nodes)

    def addEdges(self,edges):
        self.graph.add_edges_from(edges)

B = Graphe()
B.addNodes([1, 2, 3])
B.addEdges([(2,3),(1,2)])

print(B.isConnexe())