#Test
from platform import node
from re import T
from networkx import *
import matplotlib.pyplot as plt
from itertools import combinations
import numpy as np

liste = []

def readFile():
    file = open("data/graph","r")
    print(file.read())
    file.close()
readFile()

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

B = Graphe()
B.addNodes([1, 2, 3,4,5])
B.addEdges([(2,3),(1,4),(1,5)])

print(B.isConnexe())