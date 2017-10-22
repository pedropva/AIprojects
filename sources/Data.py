from Node import Node

class Data:
    """description of class"""
    def __init__(self):
    	pass

    @staticmethod
    def cities():
    	neighbors = {'Arad':('Sibiu','Timisoara','Zerind'),'Zerind':('Arad','Oradea'),'Oradea':('Sibiu','Zerind'),'Timisoara':('Arad','Lugoj'),'Lugoj':('Mehadia','Timisoara'),'Mehadia':('Drobeta','Lugoj'),'Drobeta':('Craiova','Mehadia'),'Craiova':('Drobeta','Pitesti','Rimnicu'),'Sibiu':('Arad','Fagaras','Oradea','Rimnicu'),'Fagaras':('Bucareste','Sibiu'),'Rimnicu':('Craiova','Pitesti','Sibiu'),'Pitesti':('Bucareste','Craiova','Rimnicu'),'Neamt':('Iasi',),'Iasi':('Neamt','Vaslui'),'Vaslui':('Iasi','Urziceni'),'Bucareste':('Fagaras','Giurgiu','Pitesti','Urziceni'),'Giurgiu':('Bucareste',),'Urziceni':('Bucareste','Hirsova','Vaslui'),'Hirsova':('Eforie','Urziceni'),'Eforie':('Hirsova',)}
    	distances = {'Arad':(140,118,75),'Zerind':(75,71),'Oradea':(151,71),'Timisoara':(118,111),'Lugoj':(70,111),'Mehadia':(75,70),'Drobeta':(120,75),'Craiova':(120,138,146),'Sibiu':(140,99,151,80),'Fagaras':(211,99),'Rimnicu':(146,97,80),'Pitesti':(101,138,97),'Neamt':(87,),'Iasi':(87,92),'Vaslui':(92,142),'Bucareste':(211,90,101,85),'Giurgiu':(90,),'Urziceni':(85,98,142),'Hirsova':(86,98),'Eforie':(86,)}
    	namesOfCities = ['Arad','Zerind','Oradea','Timisoara','Lugoj','Mehadia','Drobeta','Craiova','Sibiu','Fagaras','Rimnicu','Pitesti','Neamt','Iasi','Vaslui','Bucareste','Giurgiu','Urziceni','Hirsova','Eforie']
    	expectations ={"Arad" : 366,"Bucareste" : 0,"Craiova" : 160,"Drobeta" : 242,"Eforie" : 161,"Fagaras" : 176,"Giurgiu" : 77,"Hirsova" : 151,"Iasi" : 226,"Lugoj" : 244,"Mehadia" : 241,"Neamt" : 234,"Oradea" : 380,"Pitesti" : 100,"Rimnicu" : 193,"Sibiu" : 253,"Timisoara" : 329,"Urziceni" : 80,"Vaslui" : 199,"Zerind" : 374}
    	cities= {}
    	for i in namesOfCities:
    		cities[i] = Node(i,0)
    	for city in cities.keys():
    		cities[city].setExpectation(expectations[city])
    		for neighbor in neighbors[city]:
    			cities[city].addNeighbor(cities[neighbor],distances[city][neighbors[city].index(neighbor)])

    	return cities