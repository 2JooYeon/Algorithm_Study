from heapq import heapify, heappush, heappop
from copy import deepcopy
from enum import Enum


class Direction(Enum):
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)
    UP = (-1, 0)


class Node:
    grid = []
    empty = (0, 0)
    size = (0, 0)
    cost = 0
    parent = None

    def __init__(self, grid, empty, parent, movement=(0, 0)):
        self.grid = deepcopy(grid)
        self.empty = deepcopy(empty)
        self.size = (len(self.grid), len(self.grid[0]))
        self.parent = parent
        if self.parent is None:
            self.cost = self.calcCost()
        else:
            self.cost = self.parent.cost
        self.move(movement[0], movement[1])

    def calcCost(self):
        ans = 0
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.grid[i][j] != self.toOneDim(i, j) and self.grid[i][j] != 0:
                    ans += 1
        return ans

    def move(self, x, y):
        if not (x == 0 and y == 0):
            self.grid[self.empty[0]][self.empty[1]], self.grid[self.empty[0] + x][self.empty[1] + y] = self.grid[self.empty[0] + x][self.empty[1] + y], self.grid[self.empty[0]][self.empty[1]]
            if not self.isRightPosition(self.empty[0], self.empty[1]):
                self.cost += 2
            self.empty = (self.empty[0] + x, self.empty[1] + y)

    def isRightPosition(self, x, y):
        return self.grid[x][y] == self.toOneDim(x, y)

    def print(self):
        print("board size:", self.size)
        print("empty at:", self.empty)
        print("cost is:", self.cost)
        self.print_board()

    def print_board(self):
        mx = len(str(self.size[0] * self.size[1])) + 1
        print("┌", end="")
        for j in range(self.size[1]):
            print("─" * mx, end="┬" if j != self.size[1] - 1 else "┐")
        print()

        for i in range(self.size[0]):
            line = self.grid[i]
            for ch in line:
                print("|", end="")
                print(ch, end=" " * (mx - len(str(ch))))
            print("│", end="\n" + ("├" if i != self.size[0] - 1 else "└"))

            for j in range(self.size[1]):
                print("─" * mx, end=("┼" if j != self.size[1] - 1 else "┤") if i != self.size[0] - 1 else ("┴" if j != self.size[1] - 1 else "┘"))
            print()

    def toOneDim(self, x, y):
        return x * self.size[0] + y + 1


class Board:
    nodes = []
    r, c = 0, 0
    curNode = None
    activeNode = []
    answer = []
    heapify(activeNode)

    def __init__(self, config=[]):
        grid = []

        self.r, self.c = map(int, config[0].split())
        del config[0]
        for line in config:
            grid.append(list(map(int, line.strip().split())))
        for i in range(self.r):
            for j in range(self.c):
                if grid[i][j] == 0:
                    self.nodes.append(Node(grid, (i, j), None))
                    self.curNode = self.nodes[0]
                    return

    def solvable(self, output=False):
        tot = self.sigmaKurang(output)
        X = (self.curNode.empty[0] + self.curNode.empty[1]) % 2
        if output:
            print("Total Kurang:", tot)
            print("Total Kurang + X:", tot + X)
            print()
        return (tot + X) % 2 == 0

    def sigmaKurang(self, output=False):
        tot = 0
        for i in range(self.r):
            for j in range(self.c):
                x = self.toOneDim(i, j)
                y = self.kurang(x)
                tot += y
                if output:
                    print("Kurang(" + str(x) + "):", y)
        return tot

    def kurang(self, x):
        ans = 0
        for i in range(self.r):
            for j in range(self.c):
                y = self.toOneDim(i, j)
                if y < x and self.posisi(y) > self.posisi(x):
                    ans += 1
        return ans

    def posisi(self, x):
        # empty cell = 0
        x %= self.r * self.c
        for i in range(self.r):
            for j in range(self.c):
                if self.curNode.grid[i][j] == x:
                    return self.toOneDim(i, j)

    def solve(self):
        heappush(self.activeNode, (self.curNode.cost, len(self.nodes) - 1))
        print("Time needed to run ", end="")
        if self.solveUtil():
            while self.curNode is not None:
                self.answer.append(self.curNode)
                self.curNode = self.curNode.parent
            print()

            self.printAnswer()
            print()

    

    def isSolved(self):
        return self.sigmaKurang() == 0

    def toOneDim(self, x, y):
        return x * self.c + y + 1

    def isValidMove(self, x, y):
        empty = self.curNode.empty
        return self.isValidCell(empty[0] + x, empty[1] + y)

    def isValidCell(self, x, y):
        return 0 <= x < self.r and 0 <= y < self.c

    def hasNode(self, test):
        for node in self.nodes:
            if node.grid == test:
                return True
        return False

    def printAnswer(self):
        print("========= Steps =========")
        for i in range(len(self.answer)):
            print("Step {}:".format(i))
            node = self.answer[-i - 1]
            node.print_board()
            print()
        print(len(self.nodes), "nodes generated to solve the puzzle")