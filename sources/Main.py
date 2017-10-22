import os
from Node import Node
from Search import Search
from Data import Data

cities = Data.cities()

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
            print('3-Chicken, Fox and Wheat')
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
                    Node.printNodes(cities)
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
                    print("Result:",result[1])
                    input()
                elif(option1 == 2):
                    start = input("Departure:").title()
                    finish = input("Destination:").title()
                    result = Search.djikstra(cities[start],cities[finish])
                    print("Result:",result[1],' with cost: ', result[2])
                    input()
                elif(option1 == 3):
                    start = input("Departure:").title()
                    print("Only destination is avaliable bucharest, no heuristics data for the other ones")
                    result = Search.aStar(cities[start],cities['Bucareste'])
                    print("Result:",result[1],' with cost: ', result[2])
                    input()
                else:
                    print('Invalid input!')
        elif(option == 2):
            option=0
            os.system('cls')
        elif(option == 3):
            option=0
            os.system('cls')
        elif(option == 4):
            option=0
            os.system('cls')
        elif(option == 5):
            break
        else:
            print('Invalid input!')

Main()
'''


def nosso_in(elemento,L):
    presente = False
    for i in range(len(L)):
        if elemento == L[i][0][-1]:
            presente = True
            break
    return presente

def objetivo(estado):
    return estado=='Bucareste'

def meu_criterio(x):
    return x[1]

estado_inicial = [['Arad'],0]

B = [] #fila
E = []

B.append(estado_inicial)
achei = False
while not achei:
  if (len(B)==0):
    break
  #B = sorted(B,key=meu_criterio)
  no = B[0][:]
  del B[0]
  E.append(no[0][-1])
  
  for vizinho in vizinhos[no[0][-1]]:
      if not nosso_in(vizinho,B) and not vizinho in E:
          e = vizinhos[no[0][-1]].index(vizinho)
          d = distancias[no[0][-1]][e]  
          if objetivo(vizinho):
            no[0].append(vizinho)
            no[1] += d
            achei = True
            break
          B.append([ no[0] + [vizinho], no[1]+ d  ])
          
  
if achei: 
  print(no)
else:
  print('Nao achei.')
'''