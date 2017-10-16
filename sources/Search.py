class Search:
    """description of class"""
    def init(self):
        pass

    @staticmethod
    def isInList(list, obj):
        for item in list:
            if item == obj:
                return True
        return False

    @staticmethod
    def BFS(initial, final):
        traveled = {} ##traveled nodes, {node,string with the path traveled to that node}
        queue = [] ##nodes in queue to be traveled
        queue.append(initial)
        while queue:
            traveled[queue[0]] =  ##travel the first node in the queue
            if queue[0] == final:
                return 
            for i in queue.pop(0).getNeighbors():
                if not Search.isInList(traveled.keys(),i[0]):
                    queue.append(i[0])

            
            