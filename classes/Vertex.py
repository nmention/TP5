class Vertex:
    def __init__(self,name: str):
        self.name = name

    def display(self):
        print("Name",self.name)

    def getName(self):
        return self.name
