from Utils import Utils

class Node:
    """description of class"""
    objective = None ##shared objective to all nodes
    def __init__(self,name,expectation):
        self.name = name
        self.expectation = expectation
        self.neighbors = [] # creates a new empty list for each node

    def addNeighbor(self, node,distance):
        self.neighbors.append([node,distance])

    def setName(self, name):
        self.name = name
    
    def setObjective(self, objective):
        self.objective = objective

    def setExpectation(self, expectation):
        self.expectation = expectation

    def getName(self):
        return self.name

    def getObjective(self):
        return self.objective

    def getExpectation(self):
        return self.expectation

    def getNeighbors(self):
        if(not isinstance(self.name, list)):##testing if the name is a matrix, so its the number puzzle 
            return self.neighbors
        else:
            neighborNodes = []
            for i in Utils.getMatrixNeighbors(self.name):
                newNode = Node(i,1)
                if(newNode.getObjective() == None and self.objective != None):##if objective not set then set
                    newNode.setObjective(self.objective)
                #print('no: ',i,' objetivo: ',newNode.getObjective())
                newNode.setExpectation(Utils.getExpectationOfMatrix(i,newNode.getObjective()))
                #print('expectation: ',newNode.getExpectation())
                neighborNodes.append([newNode,1])##COST OF EACH PATH IS HERE
            return neighborNodes
    
    def getNeighbor(self,node):
        for neighbor in self.neighbors:
            if neighbor[0] == node:
                return neightbor[1]
        return -1

    @staticmethod
    def printNodes(listOfNodes):
        for node in listOfNodes.values():
            print('Node Name:',node.getName())
            print('Expectation: ',node.getExpectation())
            print('Neighbors: ')
            for neighbor in node.getNeighbors():
                print('Node: ' , neighbor[0].getName() , ' Wheight:', neighbor[1])
            print()


