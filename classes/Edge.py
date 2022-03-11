class Edge:
    def __init__(self,edge: tuple,weight: int):
        self.edge = edge
        self.weight = weight

    def display(self):
        print("Edge :",self.edge)
        print("Weight : ",self.weight)