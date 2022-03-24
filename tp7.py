from classes.Graphe2 import Graphe2


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
print(graphe.disjkstra2())

arrayTotal =[]
verticesGraphe = graphe.getAllVertices()

#graphe.printMarquage()