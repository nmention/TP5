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

    def addVertice(self, vertex:Vertex):
        self.vertices.append(vertex)

    def removeVertice(self, vertex:Vertex):
        self.vertices.remove(vertex)

    @staticmethod
    def randomGraphGenerator():
        nbOfVertices = random.randint(1,9)
        graphe = Graphe2.emptyGraph()
        for i in range(nbOfVertices):
            graphe.addVertice(Vertex(str(random.randint(0, 10))))