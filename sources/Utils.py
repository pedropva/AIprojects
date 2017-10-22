from Node import Node

class Utils:
    """description of class"""
    @staticmethod
    def isInList(list, obj):
        for item in list:
            if item[0] == obj:##testing two nodes, i use [0] because every traveled node is a list with the node itself and the string with the path to him
                return True
        return False

    @staticmethod
    def insertPriorityHeuristics(queue,node):
        if(queue):
            x = 0
            for q in queue:
                if(node[2]+node[0].getExpectation() < q[2]):
                    queue.insert(x,node)
                    return
                x += 1
        queue.append(node)
        return

    @staticmethod
    def insertPriority(queue,node):
        if(queue):
            x = 0
            for q in queue:
                if(node[2] < q[2]):
                    queue.insert(x,node)
                    return
                x += 1
        queue.append(node)
        return