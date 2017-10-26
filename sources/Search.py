from Node import Node
from Utils import Utils
from Data import Data
import copy

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
            if queue[0][0] == final:##if the node we are exploring is the one we are looking for then just stop and return the search data
                return traveled[-1]
            for i in queue[0][0].getNeighbors():## in each neighbor there is a list with the node itself and the distance
                if not Utils.isInList(traveled,i[0]):##tests if the neighbor isnt in the traveled or in the queue before adding it to the queue
                    if not Utils.isInList(queue,i[0]):## if it isnt in the next one to be traveled then you can add it in the queue
                        queue.append([i[0],queue[0][1]+','+i[0].getName()])
            queue.pop(0)##we are done exploring this node and he is already in the traveled list then pop it
        return False

    @staticmethod
    def djikstra(initial, final):
        traveled = [] ##traveled nodes, [node,string with the path traveled to that node,cost to get there]
        queue = [[initial,initial.getName()+'',0]] ##nodes in queue to be traveled, [node,string with the path traveled to that node,cost to get there]
        exploring = None ##holds the node we are currently exploring
        while queue:
            if not Utils.isInList(traveled,queue[0][0]):##tests again if the node to be explored is not already in the traveled list, because i could not be in the list when it was put in the queue but could be when in the traveled list when got to be explored
                    traveled.append(queue[0][:]) ##travel the first node in the queue
                    if queue[0][0] == final:##if the node we are exploring is the one we are looking for then just stop and return the search data
                        return traveled[-1]
                    exploring = queue.pop(0) ##make a copy of the first node on queue and remove it from queue
                    for i in exploring[0].getNeighbors():## in each neighbor there is a list with the node itself and the distance
                        if not Utils.isInList(traveled,i[0]):##test if the neighbor to be added isnt in the traveled list,if it is then its the best possible path to it was already been found and no need to search to a better one
                            Utils.insertPriority(queue,[i[0],exploring[1]+','+i[0].getName(),exploring[2]+i[1]])## inseting in the priority list, nodes with lower weights come first than nodes with higher weights
            else:
                queue.pop(0)##if the node that was going to be explored is already in the traveled then the best path to it was already discovered and we dont to look further in other paths
        return False
    
    @staticmethod
    def aStar(initial, final):
        traveled = [] ##traveled nodes, [node,string with the path traveled to that node,cost to get there]
        queue = [[initial,str(initial.getName()),0]] ##nodes in queue to be traveled, [node,string with the path traveled to that node,cost to get there]
        exploring = None
        while queue:
            if not Data.isInList(traveled,queue[0][0]):## in each neighbor there is a list with the node itself and the distance
                    traveled.append(copy.deepcopy(queue[0])) ##travel the first node in the queue
                    if queue[0][0].getName() == final.getName():
                        return traveled[-1]
                    exploring = queue.pop(0) ##make a copy of the first node on queue and remove it from queue
                    for i in exploring[0].getNeighbors():
                        if not Data.isInList(traveled,i[0]):## in each neighbor there is a list with the node itself and the distance
                            new = [i[0],exploring[1]+','+str(i[0].getName()),exploring[2]+i[1]] ##remove the .append('a') to make it run!
                            Data.insertPriorityHeuristics(queue,new)
            else:
                queue.pop(0)
        return False
            