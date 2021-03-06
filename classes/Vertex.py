class Vertex:
    def __init__(self,name: str):
        self.name = name
        self.neighbors = []
        self.matrice = [0]

    def display(self):
        print("Name",self.name)
        [print(i.name) for i in self.neighbors]

    def getName(self):
        return self.name

    def addNeighbor(self,vertex):
        self.neighbors.append(vertex)

    def removeNeighbor(self,vertex):
        self.neighbors.remove(vertex)
