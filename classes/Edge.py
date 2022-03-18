class Edge:
    def __init__(self,edge,weight: int):
        self.edge = edge
        self.weight = weight

    def display(self):
        print("---------------")
        print("Edge 1 :",self.edge[0].name)
        print("Edge 2 :",self.edge[1].name)
        print("Weight : ",self.weight)

    def getAllVertices(self):
        for i in self.edge:
            i.display()

    def getVertices(self):
        return [self.edge[0].name, self.edge[1].name]
