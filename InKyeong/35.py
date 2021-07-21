import numpy as np    
from itertools import *
import itertools  
import heapq
import copy
import time
import sys

counter = itertools.count()

def convert_matrix(matrix2D):
    matrix1D = list(chain.from_iterable(matrix2D)) 
    return matrix1D

def getInvCount(matrix1D,x):
    start = False
    count = 0
    for i in matrix1D:
        if (not start):
            if (i == x):
                start = True
        else:
            if (i<x): 
                count +=1
    return count

def get_Blank_column (matrix1D):
    for i in range (0,16):
        if (matrix1D[i] == 0):
            return (i%4) 

def get_Blank_row (matrix1D):
    for i in range (0,16):
        if (matrix1D[i] == 0):
            return (i//4) 

def inBound(x,y):
    return (x>=0 and x<=3 and y>=0 and y<=3)


def is_solvable(matrix1D):
    X = 0
    total = 0
    x=get_Blank_column(matrix1D)
    y=get_Blank_row(matrix1D)
    for i in range(1,len(matrix1D)+1):
        temp = getInvCount(matrix1D,i)
        total = total + temp
    if ((x%2==0 and y%2==1) or (x%2==1 and y%2==0)):
        total +=1
    print("Inversion count :" + str(total))
    if (total % 2 == 0):
        return True
    else:
        return False

def calculate_cost(matrix2D,target):
    diff = 0
    for i in range (0,4):
        for j in range(0,4):
            if (matrix2D[i][j] != target[i][j]) and (matrix2D[i][j] != 0): 
                diff +=1
    return diff

def print_matrix(matrix2D):
    for i in range (0,4):
        for j in range(0,4):
            if (matrix2D[i][j] < 10):
                print(" ",end="")    
            print(matrix2D[i][j],end=" ")
        print()
    print("============")

def print_path(root):
    if (root.parent != None):
        print_path(root.parent)
    print_matrix(root.data)

class Node:
        def __init__(self,matrix2D,row,column,new_row,new_column,level,parent):
            self.data = copy.deepcopy(matrix2D)
            temp = self.data[new_row][new_column]
            self.data[new_row][new_column] = self.data[row][column]
            self.data[row][column] = temp
            self.row = new_row
            self.column = new_column
            self.level = level
            self.parent = parent

def is_contained(matrix2D,matrix3D):
    if matrix2D in matrix3D:
        return True
    else:
        return False

def solve(matrix2D,target,total_nodes):
    matrix1D = convert_matrix(matrix2D)
    if (is_solvable(matrix1D)):
        heap = []
        visited = []
        x_direction = [0,1,0,-1] 
        y_direction = [1,0,-1,0]
        column = get_Blank_column(matrix1D)         
        row = get_Blank_row(matrix1D)
        root = Node(matrix2D,row,column,row,column,0,None)
        cost = calculate_cost(matrix2D,target)
        heapq.heappush(heap,(cost,-next(counter),root))
        while heap:
            selected_cost,_,selected_node = heapq.heappop(heap)
            if (selected_node.data == target):
                print_path(selected_node)
                print("Reached final")
                break
            for i in range(0,4):
                new_column =selected_node.column + x_direction[i]
                new_row =selected_node.row + y_direction[i]
                if inBound(new_row,new_column):
                    child = Node(selected_node.data,selected_node.row,selected_node.column,new_row,new_column,selected_node.level+1,selected_node)
                    visited.append(selected_node.data)
                    if (not (is_contained(child.data,visited))):
                        total_nodes += 1
                        cost = calculate_cost(child.data,target) + child.level
                        heapq.heappush(heap,(cost,-next(counter),child))
                total_nodes +=1 
    else:
        print("Puzzle can not solve!!!")
    return total_nodes


initial  = [[10, 7, 3, 4], [5, 9, 0, 11], [6, 1, 2, 8], [13, 14, 15, 12]]
target = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]] 
print_matrix(initial)
total_nodes = solve(initial,target,0)

