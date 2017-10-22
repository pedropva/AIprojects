from Node import Node
from Utils import Utils

class Search:
    """description of class"""
    def init(self):
        pass

    @staticmethod
    def bfs(initial, final):
        traveled = [] ##traveled nodes, [node,string with the path traveled to that node]
        queue = [[initial,initial.getName()+'']] ##nodes in queue to be traveled, [node,string with the path traveled to that node]
        while queue:
            traveled.append(queue[0][:]) ##travel the first node in the queue
            ##print(queue[0][0].getName())
            if queue[0][0] == final:
                return traveled[-1]
            for i in queue[0][0].getNeighbors():
                if not Utils.isInList(traveled,i[0]):## in each neighbor there is a list with the node itself and the distance
                    if not Utils.isInList(queue,i[0]):## if it isnt in the next one to be traveled then you can add it in the queue
                        queue.append([i[0],queue[0][1]+','+i[0].getName()])
            queue.pop(0)
        return False

    @staticmethod
    def djikstra(initial, final):
        traveled = [] ##traveled nodes, [node,string with the path traveled to that node,cost to get there]
        queue = [[initial,initial.getName()+'',0]] ##nodes in queue to be traveled, [node,string with the path traveled to that node,cost to get there]
        exploring = None
        while queue:
            if not Utils.isInList(traveled,queue[0][0]):## in each neighbor there is a list with the node itself and the distance
                    traveled.append(queue[0][:]) ##travel the first node in the queue
                    if queue[0][0] == final:
                        return traveled[-1]
                    exploring = queue.pop(0) ##make a copy of the first node on queue and remove it from queue
                    for i in exploring[0].getNeighbors():
                        if not Utils.isInList(traveled,i[0]):## in each neighbor there is a list with the node itself and the distance
                            Utils.insertPriority(queue,[i[0],exploring[1]+','+i[0].getName(),exploring[2]+i[1]])
            else:
                queue.pop(0)
        return False
    
    @staticmethod
    def aStar(initial, final):
        traveled = [] ##traveled nodes, [node,string with the path traveled to that node,cost to get there]
        queue = [[initial,initial.getName()+'',0]] ##nodes in queue to be traveled, [node,string with the path traveled to that node,cost to get there]
        exploring = None
        while queue:
            if not Utils.isInList(traveled,queue[0][0]):## in each neighbor there is a list with the node itself and the distance
                    traveled.append(queue[0][:]) ##travel the first node in the queue
                    if queue[0][0] == final:
                        return traveled[-1]
                    exploring = queue.pop(0) ##make a copy of the first node on queue and remove it from queue
                    for i in exploring[0].getNeighbors():
                        if not Utils.isInList(traveled,i[0]):## in each neighbor there is a list with the node itself and the distance
                            Utils.insertPriorityHeuristics(queue,[i[0],exploring[1]+','+i[0].getName(),exploring[2]+i[1]])
            else:
                queue.pop(0)
        return False
             
            