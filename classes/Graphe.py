import math
import random
from networkx import *
from random import choice
from classes.Edge import Edge
from classes.Vertex import Vertex


class Graphe:
    def __init__(self, vertices: list, edges: list):
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
                nbVertex1, nbVertex2 = edges[i][0]
                vertex1 = self.vertices[nbVertex1 - 1]
                vertex2 = self.vertices[nbVertex2 - 1]
                self.edges.append(Edge((vertex1, vertex2), edges[i][1]))
                edgesGraphes.append((vertex1.name, vertex2.name))

        self.graph = Graph()
        self.graph.add_nodes_from(verticesGraphes)
        self.graph.add_edges_from(edgesGraphes)

    def display(self):
        vertices = []
        edges = []
        weight = []
        for i in self.vertices:
            vertices.append([i.name])

        for i in self.edges:
            edges.append((i.edge[0].name, i.edge[1].name))
            weight.append(i.weight)

        print("Sommets :", vertices)
        print("Aretes : ", edges)
        print("Weight : ", weight)

    @staticmethod
    def emptyGraph():
        graphe = Graphe([], [])
        return graphe

    def addVertex(self, vertex: Vertex):
        self.vertices.append(vertex)

    def removeVertice(self, vertex: Vertex):
        self.vertices.remove(vertex)

    def getAllVertices(self):
        return self.vertices

    def addEdge(self, edge: Edge):
        self.edges.append(edge)

    def removeEdge(self, edge: Edge):
        self.edges.remove(edge)

    def randomGraphGenerator(self):
        graphe = Graphe.emptyGraph()
        graphe = self.remplirSommetsAleatoire(graphe)
        graphe = self.remplirAretesAleatoire(graphe)
        graphe.display()
        return graphe

    def getAllNeighbors(self):
        """ Recupere tous les voisins de chaques sommet du graphe sous forme de tableau de tableau"""
        vertex = self.graph.nodes
        # print( vertex)
        nodesConnected = []
        for i in range(len(vertex)):  # pour chaque noeud dans le graphe
            nodesConnected.append(
                list(self.graph.neighbors(list(vertex)[i])))  # on recupere les voisins de CHAQUE noeuds
            nodesConnected[i].append(list(vertex)[i])

        return nodesConnected

    def remplirSommetsAleatoire(self, graphe):
        nbOfVertices = random.randint(2, 9)  # pick random number for nb of Vertices
        for i in range(nbOfVertices):
            i += 1  ## simplement pour afficher un chiffre different de 0 , pas important
            graphe.addVertex(Vertex(str(i)))  # on creer i noeuds ( valeurs croissantes : 1 � i)

        return graphe

    def remplirAretesAleatoire(self, graphe):
        vertices = graphe.getAllVertices()
        tailleGraphe = len(vertices)
        nbMaxArete = math.ceil(tailleGraphe * (tailleGraphe - 1) / 2)
        for i in range(random.randint(2, nbMaxArete)):
            weight = random.randint(0, 100)  # on genere le poid aleatoire de  1 a 100
            ## partie de la liaison des sommets :
            random1 = random.randint(0, tailleGraphe - 1)
            random2 = choice([i for i in range(tailleGraphe) if i not in [
                random1]])  # on prend un random en EXCLUANT le 1er pou rne pas avoir 2 fois le meme sommet
            sommet1 = vertices[random1]
            sommet2 = vertices[random2]
            if (self.isInEdges(sommet1, sommet2,
                               graphe) == False):  # si le tuple n'est pas deja dans les edges du graphes
                graphe.addEdge(Edge([sommet1, sommet2], weight))
        return graphe

    def isInEdges(self, sommet1, sommet2, graphe):
        for i in graphe.edges:
            if (sommet1.name, sommet2.name) == (i.edge[0].name, i.edge[1].name): return True
            if (sommet1.name, sommet2.name) == (i.edge[1].name, i.edge[0].name): return True
        return False

    def nbVertices(self):
        return len(self.vertices)

    def getAllEdgesByVertex(self, vertex):
        routes = []
        for i in self.edges:
            if vertex == i.edge[0] or vertex == i.edge[1]:
                routes.append(i)
        return routes

    def getAllNeighborsVertices(self, vertex):
        vertices = []
        for i in self.getAllEdgesByVertex(vertex):
            if vertex == i.edge[0]:
                vertices.append(i.edge[1])
            if vertex == i.edge[1]:
                vertices.append(i.edge[0])
        return vertices

    def noeudLePlusProche(self, vertex):
        neighbors = self.getAllEdgesByVertex(vertex)
        listPoidsVoisin = [i.weight for i in neighbors]

        poidVoisinLePlusProche = min(listPoidsVoisin)
        indexVoisinLePlusProche = listPoidsVoisin.index(
            poidVoisinLePlusProche)  # si il y a deux meme poid d'arrete, prend l'index le plus petit de la liste (0>2)

        sommet1 = neighbors[indexVoisinLePlusProche].edge[0]
        sommet2 = neighbors[indexVoisinLePlusProche].edge[1]
        if (vertex.name == sommet1.name):
            noeudLePlusProche = sommet2
        else:
            noeudLePlusProche = sommet1
        return ([noeudLePlusProche,
                 poidVoisinLePlusProche])  # on renvoie le sommet de l'arete different du sommet donne (car l'un de deux est forcement le sommet donnee)l'arete du voisin le plus proche


    def disjkstra(self):
        sommets = self.getAllVertices()  # récupération de tous les sommets du graphe
        matriceTotale = []
        # assignation des voisins et poids
        for j in range(len(sommets)):  # itération sur tous les sommets
            pointDeDepart = sommets[j]  # on récupère le sommet courant
            matrice2d = []
            voisins = self.getAllEdgesByVertex(pointDeDepart)  # on récupère toutes les arrêtes reliant le sommet
            for i in range(len(voisins)):  # on itère sur les voisins
                if (pointDeDepart.name != voisins[i].edge[0].name):  # on recupère le sommmet voisin
                    voisin = voisins[i].edge[0]
                else:
                    voisin = voisins[i].edge[1]
                matrice2d.append(
                    (voisin, voisins[i].weight))  # on ajoute à la matrice le voisins et et le poids de son arrête
            pointDeDepart.matrice = matrice2d  # on associe la matrice au sommet courant
            matriceTotale.append(matrice2d)  # on rajoute la matrice courante avec la matrice distance

        marque = []  # inutile
        marque.append(sommets[0])
        pointDeDepart = sommets[0]
        cheminFinal = []
        distances = []
        cheminFinal.append(pointDeDepart.name)
        poidTotal = 0
        while True:
            poidMini = 0
            voisins = pointDeDepart.matrice
            for i in range(len(voisins)):  # tant qu'il y a des voisins, pour tous les voisins
                if (voisins[i][0].name not in marque):
                    if poidMini == 0:  # on recupere celui avec le poid minimum
                        poidMini = voisins[i][1]
                        tupleResult = (voisins[i])
                    elif poidMini > voisins[i][1]:
                        poidMini = voisins[i][
                            1]  # si jamais le plus court chemin est inférieur à une autre connexion: on lui assigne le nouveau
                        tupleResult = (voisins[i])
            distances.append((pointDeDepart.name, poidMini))  #
            poidTotal += poidMini  # on ajoute le poids précédent d'un chemin
            cheminFinal.append(tupleResult[0].name)
            marque.append(tupleResult[0].name)
            pointDeDepart = tupleResult[0]
            if len(marque) == len(sommets):
                return [cheminFinal, poidTotal, distances]

    def isConnexe(self):
        nodesConnected = self.getAllNeighbors()  # on recupere tous les noeuds du graphe
        total = self.getAllNodeConnectedByIndex(nodesConnected, 1)  # on recupere tous les noeuds connecte au noeud 1
        if len(self.getAllVertices()) == len(total):
            return True
        return False

    def getAllNodeConnectedByIndex(self, nodesConnected, index):
        """ Recupere tous les voisins directe et lointain du """
        total = []
        i = 0
        j = 1
        while (True):
            firstGroup = nodesConnected[index]
            for j in range(len(nodesConnected)):  ## pour chaque valeur de la liste principale
                for z in range(len(nodesConnected[j])):  ## pour chaque voisin dans appartenant au sommet j
                    if self.isLinked(nodesConnected[j],
                                     firstGroup):  # si le voisin z appartenant a j est dans les voisins de i (donc que le sommet i est lie au sommet j)
                        if nodesConnected[j][z] not in total:  # et si on ne l'a pas deja compte
                            total.append(nodesConnected[j][z])  # alors on l'ajoute dans les sommets reliees
            i += 1
            if (i == len(list(nodesConnected[index]))):
                break
        print(total)
        return total

    def isLinked(self, group1, group2):
        """Permet de regarder si le sommetX est connexe avec le sommetY"""
        for i in range(len(group1)):
            if group1[i] in group2:
                return True
        return False

    def matrice2d(self):
        verticesGraphe = self.getAllVertices()
        if (len(verticesGraphe[0].matrice) == 0):
            return []
        arrayTotal = []
        for i in range(len(verticesGraphe)):
            ligne = []
            for j in range(len(verticesGraphe[i].matrice)):
                vertex, weight = verticesGraphe[i].matrice[j][0].name, verticesGraphe[i].matrice[j][1]
                ligne.append((vertex, weight))
            arrayTotal.append(ligne)

        return arrayTotal

    def generateGrapheCompletAleatoire(self, sommets):
        for i in range(len(sommets)):
            self.vertices.append(Vertex(sommets[i]))
        for i in range(len(self.vertices) - 1):
            self.edges.append(Edge((self.vertices[i], self.vertices[i + 1]), random.randint(1, 100)))

    def readFile(self):
        vertex = []
        edge = []
        file = open("data/graph.txt","r")
        data = file.read().split("\n")   # on recupere toutes les lignes 1 par 1 dans un tableau
        for line in data:
            vertices = line.split("/")[0]
            edges = line.split("/")[1]
            poid = line.split("-")[0]
            self.fusionArrayEdges(edge,edges,poid)
            self.fusionArrayVertex(vertex,vertices)

        return [vertex,edge]

    def fusionArrayVertex(self,arrayDep, arrayComplement):
        for i in range(len(arrayComplement)):
            if (arrayComplement[i] != ","):
                if arrayComplement[i] not in arrayDep:
                    arrayDep.append(arrayComplement[i])


    def fusionArrayEdges(self,arrayDep, arrayComplement,poid):
        data = arrayComplement.split("*")

        for line in data:
            a = line.split(",")[0]
            if (len(line.split(",")) >= 2):
                b = line.split(",")[1]
                tuples = (a,b)
                arrayDep.append([tuples,poid])