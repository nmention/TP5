import math
import random
from tkinter import N
from networkx import *
from random import choice
from classes.Edge import Edge
from classes.Vertex import Vertex


class Graphe2:
    def __init__(self,vertices: list,edges: list):
        self.vertices = []
        self.edges = []

        edgesGraphes = []
        verticesGraphes = [] 

        if vertices != []:
            for i in range(len(vertices)):
                self.vertices.append(Vertex(vertices[i]))
                verticesGraphes.append(vertices[i])
        if edges != []:
            for i in range(len(edges)):
                nbVertex1,nbVertex2 = edges[i][0]
                vertex1 = self.vertices[nbVertex1-1]
                vertex2 = self.vertices[nbVertex2-1]
                self.edges.append(Edge((vertex1,vertex2),edges[i][1]))
                edgesGraphes.append((vertex1.name,vertex2.name))

        self.graph = Graph()
        self.graph.add_nodes_from(verticesGraphes)
        self.graph.add_edges_from(edgesGraphes)

    def display(self):
        vertices = []
        edges = []
        for i in self.vertices:
            vertices.append([i.name])

        for i in self.edges:
            edges.append((i.edge[0].name,i.edge[1].name))

        print("Sommets :" ,vertices)
        print("Aretes : " ,edges)

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


    def randomGraphGenerator(self):
        graphe = Graphe2.emptyGraph()
        graphe = self.remplirSommetsAleatoire(graphe)
        graphe = self.remplirAretesAleatoire(graphe)
        graphe.display()
        return graphe


    def getAllNeighbors(self):
        """ Recupere tous les voisins de chaques sommet du graphe sous forme de tableau de tableau"""
        vertex = self.graph.nodes
        #print( vertex)
        nodesConnected = []
        for i in range(len(vertex)): # pour chaque noeud dans le graphe
            nodesConnected.append(list(self.graph.neighbors(list(vertex)[i]))) # on recupere les voisins de CHAQUE noeuds
            nodesConnected[i].append(list(vertex)[i])

        return nodesConnected



    def remplirSommetsAleatoire(self,graphe):
        nbOfVertices = random.randint(2, 9)  # pick random number for nb of Vertices
        for i in range(nbOfVertices):
            i+=1 ## simplement pour afficher un chiffre different de 0 , pas important
            graphe.addVertex(Vertex(str(i))) # on creer i noeuds ( valeurs croissantes : 1 � i)

        return graphe

    def remplirAretesAleatoire(self,graphe):
        vertices = graphe.getAllVertices()
        tailleGraphe = len(vertices)
        nbMaxArete = math.ceil(tailleGraphe * (tailleGraphe - 1) / 2)
        for i in range(random.randint(0, nbMaxArete)):
            weight = random.randint(0,100) # on genere le poid aleatoire de  1 a 100
            ## partie de la liaison des sommets :
            random1 = random.randint(0,tailleGraphe-1)
            random2 = choice([i for i in range(tailleGraphe) if i not in [random1]]) # on prend un random en EXCLUANT le 1er pou rne pas avoir 2 fois le meme sommet
            sommet1 = vertices[random1]
            sommet2 = vertices[random2]
            if ( self.isInEdges(sommet1,sommet2,graphe) == False): # si le tuple n'est pas deja dans les edges du graphes
                graphe.addEdge(Edge([sommet1,sommet2],weight))
        return graphe

    def isInEdges(self,sommet1,sommet2,graphe):
        for i in graphe.edges:
            if (sommet1.name,sommet2.name) == (i.edge[0].name,i.edge[1].name): return True
            if (sommet1.name,sommet2.name) == (i.edge[1].name,i.edge[0].name): return True
        return False

    def nbVertices(self):
        return len(self.vertices)

    def getAllEdgesByVertex(self,vertex):
        routes = []
        for i in self.edges:
            if vertex == i.edge[0] or vertex == i.edge[1]:
                routes.append(i.edge)
        return routes

    def getAllNeighborsVertices(self,vertex):
        vertices = []
        for i in self.getAllEdgesByVertex(vertex):
            if vertex == i.edge[0]:
                vertices.append(i.edge[1])
            if vertex == i.edge[1]:
                vertices.append(i.edge[0])
        return vertices




    def disjkstra(self):
        exclusionList = []
        for i in range(self.nbVertices()):
            currentVertice = self.vertices[i]
            currentNeighbors = self.getAllEdgesByVertex(currentVertice)
            verticesNeighbors = self.getAllNeighborsVertices(currentVertice)
            for j,k in currentNeighbors,verticesNeighbors:
                if j.weight < k.marquage and k not in exclusionList:
                    k.marquage = j.weight
            exclusionList.append(currentVertice)












