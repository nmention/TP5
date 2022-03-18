import math
import random
from networkx import *
from classes.Edge import Edge
from classes.Vertex import Vertex


class Graphe2:
    def __init__(self,vertices: list,edges: list):
        self.vertices = []
        self.edges = []

        edgesGraphes = []
        verticesGraphes = [] 

        for i in range(len(vertices)):
           self.vertices.append(Vertex(vertices[i]))
           verticesGraphes.append(vertices[i])

        for i in range(len(edges)):
            self.edges.append(Edge(edges[i][0],edges[i][1]))
            edgesGraphes.append(edges[i][0])

        self.graph = Graph()
        self.graph.add_nodes_from(verticesGraphes)
        self.graph.add_edges_from(edgesGraphes)

    def display(self):
        print("Vertices : ",self.vertices)
        for i in self.vertices:
            i.display()

        print("Edges", self.edges)
        for i in self.edges:
            i.display()
            i.getAllVertices()


    @staticmethod
    def emptyGraph():
        graphe = Graphe2([],[])
        return graphe

    def addVertex(self, vertex:Vertex):
        self.vertices.append(vertex)

    def removeVertice(self, vertex:Vertex):
        self.vertices.remove(vertex)

    def getAllVertices(self):
        return self.vertices

    def addEdge(self,edge:Edge):
        self.edges.append(edge)

    def removeEdge(self,edge:Edge):
        self.edges.remove(edge)

    @staticmethod
    def randomGraphGenerator():
        nbOfVertices = 0
        while nbOfVertices == 1 or nbOfVertices == 0:
            nbOfVertices = random.randint(1, 9)  # pick random number for nb of Vertices
        print(nbOfVertices)

        edgesNumber = math.ceil(nbOfVertices * (nbOfVertices - 1) / 2)  # max number of edges for non-oriented graph
        print(edgesNumber)
        edgesNumber = random.randint(1,edgesNumber)  # pick rand num btw 1 and max
        graphe = Graphe2.emptyGraph()


        # Adding the Vertices
        for i in range(nbOfVertices):
            graphe.addVertex(Vertex(str(i)))

        # Adding the Edges
        for i in range(edgesNumber):
            weight = (int)(random.random()*10)  # pick random number for weight
            vertice1 = random.choice(graphe.getAllVertices())
            vertice2 = random.choice(graphe.getAllVertices())
            while vertice2 == vertice1 or (vertice1,vertice2) in [i.edge for i in graphe.edges] or (vertice2,vertice1) in [j.edge for j in graphe.edges]:
                vertice2 = random.choice(graphe.getAllVertices())
            graphe.addEdge(Edge((vertice1,vertice2),weight))

        return graphe

    def getAllNeighbors(self):
        """ Recupere tous les voisins de chaques sommet du graphe sous forme de tableau de tableau"""
        vertex = self.graph.nodes
        nodesConnected = []
        for i in range(len(vertex)): # pour chaque noeud dans le graphe
            nodesConnected.append(list(self.graph.neighbors(list(vertex)[i]))) # on recupere les voisins de CHAQUE noeuds
            nodesConnected[i].append(list(vertex)[i])

        return nodesConnected

