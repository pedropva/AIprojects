class Node:
    """description of class"""
    def __init__(self,name,expectation):
        self.name = name
        self.expectation = expectation
        self.neighbors = [] # creates a new empty list for each node

    def addNeighbor(self, node,distance):
        self.neighbors.append([node,distance])
    
    def setName(self, name):
        self.name = name
    
    def setExpectation(self, expectation):
        self.expectation = expectation

    def getName(self):
        return self.name

    def getExpectation(self):
        return self.expectation

    def getNeighbors(self):
        return self.neighbors
    
    def getNeighbor(self,node):
        for neighbor in self.neighbors:
            if neighbor[0] == node:
                return neightbor[1]
        return -1