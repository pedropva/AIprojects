import os
from Node import Node
from Search import Search
from Data import Data
from Utils import Utils

cities = Data.cities()
situations = Data.cfg()
def Main():
    option = 0
    option1 = 0
    start = None
    finisht = None
    while True:
        os.system('cls')
        if(option == 0):
            option=0
            print('{:=^15}'.format(' Menu '))
            print('What do you want to do?')
            print('1-List Data from nodes')
            print('2-Path to City')
            print('3-Chicken, Fox and Grains')
            print('4-Puzzle with numbers')
            print("5-Exit")
            option = int(input("Option:"))

        elif(option == 1):
            option=0
            while True:
                os.system('cls')
                print('Choose the data to be shown:')
                print('0-return to menu')
                print('1-Cities')
                print('2-Chicken, Fox and Wheat')
                print('3-Puzzle with numbers')
                option1 = int(input("Option: "))
                if(option1 == 0):
                    break
                elif(option1 == 1):
                    Node.printNodes(cities)
                    input()
                elif(option1 == 2):
                    Node.printNodes(situations)
                    input()
                elif(option1 == 3):
                    Node.printNodes(cities)
                    input()
                else:
                    print('Invalid input!')
        elif(option == 2):
            option=0
            while True:
                os.system('cls')
                print('Choose algorithm:')
                print('0-return to menu')
                print('1-BFS')
                print('2-Djikstra')
                print('3-A*')
                option1 = int(input("Option:"))
                if(option1 == 0):
                    break
                elif(option1 == 1):
                    start = input("Departure:").title()
                    finish = input("Destination:").title()
                    result = Search.bfs(cities[start],cities[finish])
                    if result != False:
                        print()
                        print("Result:",result[1])
                    else:
                        print('Found no path')
                    input()
                elif(option1 == 2):
                    start = input("Departure:").title()
                    finish = input("Destination:").title()
                    result = Search.djikstra(cities[start],cities[finish])
                    if result != False:
                        print()
                        print("Result:",result[1],' with cost: ', result[2])
                    else:
                        print('Found no path')
                    input()
                elif(option1 == 3):
                    start = input("Departure:").title()
                    print("Only destination is avaliable bucharest, no heuristics data for the other ones")
                    result = Search.aStar(cities[start],cities['Bucareste'])
                    if result != False:
                        print()
                        print("Result:",result[1],' with cost: ', result[2])
                    else:
                        print('Found no path')
                    input()
                else:
                    print('Invalid input!')
        elif(option == 3):
            option=0
            os.system('cls')
            print('Insert the desired starting and final states,use the first caracther of each word, and put them separated by a comma and separating left and right side of the river by a |')
            print("boatman = 'b', chicken = 'c', fox = 'f' and grains = 'g'")
            print('Example of state: b,c,f|g')
            print()
            start = input("Starting state:").lower()
            finish = input("Final state:").lower()
            start=Data.cfgCode(start)
            finish=Data.cfgCode(finish)
            if(start != False and finish != False and Utils.isInList(situations.keys(),start) and Utils.isInList(situations.keys(),finish)):
                result = Search.bfs(situations[start],situations[finish])##checks if those are valid states and if they are then search best path
                if result != False:
                    print()
                    print("Result:")
                    Data.cfgDecode(result[1])
                    print('With cost: ', result[2])
                else:
                    print('Found no path')
            else:
                print('Invalid State!')
            input()
        elif(option == 4):
            option=0
            os.system('cls')
            print('Fill the intial matrix:')
            '''
            start = [[int(input("[Line 1 column 1]: ")),
                    int(input("[Line 1 column 2]: ")),
                    int(input("[Line 1 column 3]: "))],
                    [int(input("[Line 2 column 1]: ")),
                    int(input("[Line 2 column 2]: ")),
                    int(input("[Line 2 column 3]: "))],
                    [int(input("[Line 3 column 1]: ")),
                    int(input("[Line 3 column 2]: ")),
                    int(input("[Line 3 column 3]: "))]]
            '''
            finish = [[0,1,2],[3,4,5],[6,7,8]]
            start = Data.puzzle([[8,7,6],[5,4,3],[2,1,0]],finish)##Data.puzzle(start,finish)##creating the node with the matrix itself and the objective matrix
            finish = Data.puzzle(finish,finish)
            if(start and finish):
                result = Search.aStar(start,finish)
                if result != False:
                    print()
                    print("Result:")
                    Data.puzzleDecode(result[1])
                else:
                    print('Found no path')
            input()    
        elif(option == 5):
            break
        else:
            print('Invalid input!')

Main()