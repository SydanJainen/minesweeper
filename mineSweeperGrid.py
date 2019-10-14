import random
from termcolor import cprint
import numpy
import mineSweeperCell

""" in knowngrid  9 sta per 0 esplorato. 0 sta per 0 non esplorato. -1 bomba. -2 flag """
class Minesweeper:
    bombSignature = -1
    markSignature = -2

    def __init__(self, row=9, col=9, nBomb=10):
        self.row = row
        self.col = col
        self.nBomb = nBomb
        self.grid = numpy.zeros([self.row, self.col], dtype=int)
        self.knowngrid = numpy.zeros([self.row, self.col], dtype=int)
        self.unexplored = self.row * self.col
        self.flagnumber = 0

        for r in range(0, self.row):
            for c in range(0, self.col):
                self.knowngrid[r][c] = 0

        print("setting bombs...")
        for n in range(0, self.nBomb):
            self.placebomb()

        print("updating value...")
        for r in range(0, self.row):
            for c in range(0, self.col):
                if self.grid[r][c] == self.bombSignature:
                    self.updatevalue(r, c)


    def placebomb(self):
        r = random.randint(0, self.row - 1)
        c = random.randint(0, self.col - 1)
        if self.grid[r][c] == 0:
            self.grid[r][c] = self.bombSignature
        else:
            self.placebomb()

    def updatevalue(self, r, c):
        # dx
        if r + 1 < self.row:
            if self.grid[r + 1][c] != self.bombSignature:
                self.grid[r + 1][c] += 1
        # sx
        if r - 1 > -1:
            if self.grid[r - 1][c] != self.bombSignature:
                self.grid[r - 1][c] += 1
        # down
        if c + 1 < self.col:
            if self.grid[r][c + 1] != self.bombSignature:
                self.grid[r][c + 1] += 1
        # up
        if c - 1 > -1:
            if self.grid[r][c - 1] != self.bombSignature:
                self.grid[r][c - 1] += 1

        # dx && up
        if c - 1 > -1 and r + 1 < self.row:
            if self.grid[r + 1][c - 1] != self.bombSignature:
                self.grid[r + 1][c - 1] += 1

        # dx && down
        if c + 1 < self.col and r + 1 < self.row:
            if self.grid[r + 1][c + 1] != self.bombSignature:
                self.grid[r + 1][c + 1] += 1

        # sx && up
        if r - 1 > -1 and c - 1 > -1:
            if self.grid[r - 1][c - 1] != self.bombSignature:
                self.grid[r - 1][c - 1] += 1

        # sx && down
        if r - 1 > -1 and c + 1 < self.col:
            if self.grid[r - 1][c + 1] != self.bombSignature:
                self.grid[r - 1][c + 1] += 1

    # 0 for solution
    # 1 for known
    def printBoard(self, typeOfGrid):
        if typeOfGrid == 0 or typeOfGrid == 1:
            # prima riga
            outergrid =" ╔═════╦"
            interlinea =" ╠═════╬"
            outergridD = " ╚═════╩"
            for n in range(0, self.row-2):
                outergrid += "═════╦"
                interlinea += "═════╬"
                outergridD += "═════╩"
            outergrid += "═════╗\n"
            interlinea += "═════╣\n"
            outergridD += "═════╝"
            #centro
            for c in range(0, self.col):
                outergrid += str(c)+"║ "
                for r in range(0, self.row):
                    if typeOfGrid == 0:
                        if self.grid[r][c] == self.bombSignature:
                            outergrid += " *  ║ "
                        else:
                            outergrid += " "+str(self.grid[r][c])+"  ║ "
                    else:
                        if self.knowngrid[r][c] == self.bombSignature:
                            outergrid += " *  ║ "
                        elif self.knowngrid[r][c] == self.markSignature:
                                outergrid += " ⚐ ║ "
                        else:
                            if self.knowngrid[r][c] == 0:
                                outergrid += " X  ║ "
                            elif self.knowngrid[r][c] == 9:
                                outergrid += " 0  ║ "
                            else:
                                outergrid += " " + str(self.knowngrid[r][c]) + "  ║ "
                if c == self.col-1:
                    outergrid += "\n"
                else:
                    outergrid += "\n"+interlinea
            outergrid += outergridD
            print(outergrid)
        else:
            print("Error:\n The parameter of printBoard function must be 0 for solution or 1 for known grid")

    def explore(self, r, c):
        if self.grid[r][c] == 0 and self.knowngrid[r][c] != 9:
            self.knowngrid[r][c] = 9
            self.unexplored -= 1
        elif self.grid[r][c] > 0:
            self.knowngrid[r][c] = self.grid[r][c]
            self.unexplored -= 1
        # dx
        if r + 1 < self.row:
            if self.grid[r + 1][c] == 0 and self.knowngrid[r + 1][c] != 9:
                self.knowngrid[r + 1][c] = 9
                self.explore(r + 1, c)
                self.unexplored -= 1
            elif self.grid[r + 1][c] > 0:
                self.knowngrid[r + 1][c] = self.grid[r + 1][c]
                self.unexplored -= 1
        # sx
        if r - 1 > -1:
            if self.grid[r - 1][c] == 0 and self.knowngrid[r - 1][c] != 9:
                self.knowngrid[r - 1][c] = 9
                self.explore(r - 1, c)
                self.unexplored -= 1
            elif self.grid[r - 1][c] > 0:
                self.knowngrid[r - 1][c] = self.grid[r - 1][c]
                self.unexplored -= 1
        # down
        if c + 1 < self.col:
            if self.grid[r][c + 1] == 0 and self.knowngrid[r][c + 1] != 9:
                self.knowngrid[r][c + 1] = 9
                self.explore(r, c + 1)
                self.unexplored -= 1
            elif self.grid[r][c + 1] > 0:
                self.knowngrid[r][c + 1] = self.grid[r][c + 1]
                self.unexplored -= 1
        # up
        if c - 1 > -1:
            if self.grid[r][c - 1] == 0 and self.knowngrid[r][c - 1] != 9:
                self.knowngrid[r][c - 1] = 9
                self.explore(r, c - 1)
                self.unexplored -= 1
            elif self.grid[r][c - 1] > 0:
                self.knowngrid[r][c - 1] = self.grid[r][c - 1]
                self.unexplored -= 1

    def toggleMine(self, r, c):
        if self.knowngrid[r][c] != self.markSignature:
            self.knowngrid[r][c] = self.markSignature
            self.flagnumber += 1
        else:
            self.knowngrid[r][c] = 0
            self.flagnumber -= 1

    def isMine(self, r, c):
        if self.grid[r][c] == -1:
            return True
        else:
            return False

    def play(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        # Loop in case of invalid entry.
        while True:
            chosen = input('Choose a square (eg. E4) or place a marker (eg. mE4): ').lower()
            if len(chosen) == 3 and chosen[0] == 'm' and chosen[1] in letters and chosen[2] in numbers:
                r, c = (ord(chosen[1])) - 97, int(chosen[2])
                self.toggleMine(r, c)
                self.printBoard(1)
            elif len(chosen) == 2 and chosen[0] in letters and chosen[1] in numbers:
                if self.isMine(int(chosen[1]), (ord(chosen[0])) - 97) == True:
                    print("You Lose !")
                    self.printBoard(0)
                    break
                else:
                    self.explore(int(chosen[1]),(ord(chosen[0])) - 97)
                    self.printBoard(1)
                    if (self.unexplored - self.flagnumber == 0 and self.flagnumber == self.nBomb) or self.unexplored == self.nBomb:
                        print(" You Win !")
                        break

            else:
                print("input not valid")

