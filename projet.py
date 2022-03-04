#Test
from networkx import *
liste = []

def readFile():
    file = open("data/graph","r")
    print(file.read())
    file.close()
readFile()

class Graphe:
    def __init__(self,nodes):
        self.nodes = nodes()
        self.graph = Graph(nodes)

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
        return len(self.graph.nodes()) == len(self.CC(self.graph,list(self.graph.nodes())[0]).nodes())