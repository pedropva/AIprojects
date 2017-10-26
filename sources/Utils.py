class Utils:
    """description of class"""
    @staticmethod
    def insertPriority(queue,node): ##inserting in a normal priority queue, used for djisktra search
        if(queue):
            x = 0
            for q in queue:
                if(node[2] < q[2]):
                    queue.insert(x,node)
                    return
                x += 1
        queue.append(node)
        return

    @staticmethod
    def getMatrixNeighbors(matrix):
        maxLen = len(matrix) - 1
        possibilities = []
        x = 0;
        found = False;
        for line in matrix:
            y = 0;
            for number in line:
                if(number == 0):
                    if(not x == 0):
                        newState = Utils.copyMatrix(matrix)
                        newState[x][y], newState[x-1][y] = newState[x-1][y], newState[x][y]
                        possibilities.append(newState)
                    if(not x == maxLen):
                        newState = Utils.copyMatrix(matrix)
                        newState[x][y], newState[x+1][y] = newState[x+1][y], newState[x][y]
                        possibilities.append(newState)
                    if(not y == 0):
                        newState = Utils.copyMatrix(matrix)
                        newState[x][y], newState[x][y-1] = newState[x][y-1], newState[x][y]
                        possibilities.append(newState)
                    if(not y == maxLen):
                        newState = Utils.copyMatrix(matrix)
                        newState[x][y], newState[x][y+1] = newState[x][y+1], newState[x][y]
                        possibilities.append(newState)     
                    found = True;
                if(found): break;
                y += 1
            if(found): break;
            x += 1

        return possibilities

    def getExpectationOfMatrix(matrix,objective):
        expectation = 0
        x = 0
        for l in matrix:
            y = 0
            for n in l:
                if n != 0:
                    idealLine, idealColumn = Utils.getIdealPosition(n,objective)
                    expectation += (abs( x - idealLine) + abs(y - idealColumn))
                y = y + 1
            x = x + 1
        return expectation

    @staticmethod
    def getIdealPosition(n,objective):
        x = 0
        for l in objective:
            y = 0
            for numbero in l:
                if(numbero == n):
                    return x,y
                y += 1
            x += 1


    @staticmethod
    def getNeighborMatrixes(matrix):
        neighborNodes = []
        for i in Utils.getMatrixNeighbors(matrix):
            newNode = Data.puzzle(i)
            neighborNodes.append(newNode)
        return neighborNodes

    @staticmethod
    def copyMatrix(matrix):
        newMatrix = []
        for l in matrix:
            newMatrix.append(l[:])
        return newMatrix

    @staticmethod
    def isInList(list, obj):
        for item in list:
            if item == obj:##testing two nodes, i use [0] because every traveled node is a list with the node itself and the string with the path to him
                return True
        return False
