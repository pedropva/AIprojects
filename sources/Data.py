from Node import Node
from Utils import Utils
class Data:
    """description of class"""
    def __init__(self):
    	pass

    @staticmethod
    def cities():
    	neighbors = {'Arad':('Sibiu','Timisoara','Zerind'),'Zerind':('Arad','Oradea'),'Oradea':('Sibiu','Zerind'),'Timisoara':('Arad','Lugoj'),'Lugoj':('Mehadia','Timisoara'),'Mehadia':('Drobeta','Lugoj'),'Drobeta':('Craiova','Mehadia'),'Craiova':('Drobeta','Pitesti','Rimnicu'),'Sibiu':('Arad','Fagaras','Oradea','Rimnicu'),'Fagaras':('Bucareste','Sibiu'),'Rimnicu':('Craiova','Pitesti','Sibiu'),'Pitesti':('Bucareste','Craiova','Rimnicu'),'Neamt':('Iasi',),'Iasi':('Neamt','Vaslui'),'Vaslui':('Iasi','Urziceni'),'Bucareste':('Fagaras','Giurgiu','Pitesti','Urziceni'),'Giurgiu':('Bucareste',),'Urziceni':('Bucareste','Hirsova','Vaslui'),'Hirsova':('Eforie','Urziceni'),'Eforie':('Hirsova',)}
    	distances = {'Arad':(140,118,75),'Zerind':(75,71),'Oradea':(151,71),'Timisoara':(118,111),'Lugoj':(70,111),'Mehadia':(75,70),'Drobeta':(120,75),'Craiova':(120,138,146),'Sibiu':(140,99,151,80),'Fagaras':(211,99),'Rimnicu':(146,97,80),'Pitesti':(101,138,97),'Neamt':(87,),'Iasi':(87,92),'Vaslui':(92,142),'Bucareste':(211,90,101,85),'Giurgiu':(90,),'Urziceni':(85,98,142),'Hirsova':(86,98),'Eforie':(86,)}
    	expectations ={"Arad" : 366,"Bucareste" : 0,"Craiova" : 160,"Drobeta" : 242,"Eforie" : 161,"Fagaras" : 176,"Giurgiu" : 77,"Hirsova" : 151,"Iasi" : 226,"Lugoj" : 244,"Mehadia" : 241,"Neamt" : 234,"Oradea" : 380,"Pitesti" : 100,"Rimnicu" : 193,"Sibiu" : 253,"Timisoara" : 329,"Urziceni" : 80,"Vaslui" : 199,"Zerind" : 374}
    	cities= {}
    	for i in neighbors.keys():
    		cities[i] = Node(i,0)
    	for city in cities.keys():
    		cities[city].setExpectation(expectations[city])
    		for neighbor in neighbors[city]:
    			cities[city].addNeighbor(cities[neighbor],distances[city][neighbors[city].index(neighbor)])

    	return cities

    @staticmethod
    def cfg():
        states ={"bcfg|":("fg|bc","cfg|b"),"cfg|b":("bcfg|",),"fg|bc":("bfg|c","bcfg|"),"bfg|c":("g|bcf","f|bcg","fg|bc"),"g|bcf":("bfg|c","bcg|f"),"bcg|f":("c|bfg","g|bcf"),"f|bcg":("bcf|g","bfg|c"),"bcf|g":("c|bfg","f|bcg"),"c|bfg":("bc|fg","bcf|g","bcg|f"),"bc|fg":("|bcfg","c|bfg"),"|bcfg":("bc|fg","b|cfg"),"b|cfg":("|bcfg",)}
        situations = {}
        for i in states.keys():
            situations[i] = Node(i,0)
        for s in states.keys():
            for neighbor in states[s]:
                situations[s].addNeighbor(situations[neighbor],1)
        return situations

    @staticmethod
    def puzzle(matrix,objective):
        puzzle = Node(matrix,1)
        if(puzzle.getObjective() == None and objective != None):##if objective not set then set
            puzzle.setObjective(objective)
        puzzle.setExpectation(Utils.getExpectationOfMatrix(matrix,puzzle.getObjective()))
        return puzzle

    @staticmethod
    def cfgDecode(path):
        ##separate left and right
        count = 0
        current = ""
        while (count < len(path)):
            current = path[count]
            if(current == 'b') : print("Boatman",end = ' ')
            elif(current == 'g') : print("Grains",end = ' ')
            elif(current == 'c') : print("Chicken",end = ' ')
            elif(current == 'f') : print("Fox",end = ' ')
            elif(current == ',') : print()
            else: print(current,end = '')
            count += 1

        
    @staticmethod
    def cfgCode(state):
        for i in state:
                if(not((i == 'b') or (i == 'c') or (i == 'f') or (i == 'g') or (i == '') or (i == '|') or (i == ','))):return False
        state = state.split('|')
        if(state[0] and state[1]):
            l = state[0][:]
            r = state[1][:]
        else:
            return False
        l = sorted(l.split(','))
        r = sorted(r.split(','))    
        if(l and r):    
           return ''.join(l) +'|'+ ''.join(r)
        return False
##b,c,g,f|
    @staticmethod
    def puzzleDecode(path):
        path = path.split('],[')
        for l in path:
                l = l.split('], [')
                for r in l:
                    r = r.replace("]", "")
                    r = r.replace("[", "")
                    print(r)
                print()

    @staticmethod
    def insertPriorityHeuristics(queue,node):##inserting in a priority queue comparing their wheights and their heuristics, used for aStar search
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
    def isInList(list, obj):
        for item in list:
            if item[0].getName() == obj.getName():##testing two nodes, i use [0] because every traveled node is a list with the node itself and the string with the path to him
                return True
        return False

    @staticmethod
    def isAValidMAtrix(matrix):
        maxN = len(matrix) * len(matrix[0])
        minN = 0
        numbers= []
        for l in matrix:
            for r in l:
                if r > maxN or r < minN:
                    return False
                if r not in numbers:
                    numbers.append(r)
                else:
                    return False
        return True