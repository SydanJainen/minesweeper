import model as game
import random


class mineSweeperAgent:

    def __init__(self):
        self.game = game.Minesweeper()
        self.knowledge = set()
        self.actionFlag = set()
        self.actionExploreCell = set()

    def strategySelector(self):
        # prima faccio le mosse banali. quelle che non comportano knowledge
        self.actionExploreCell, self.actionFlag = self.trivialStrategy()
        if self.actionExploreCell or self.actionFlag:
            if self.actionFlag:
                return self.actionFlag.pop()  # il pop in un set ritorna un random
            else:
                return self.actionExploreCell.pop()  # possibile raffinamento

        # combino le informazioni che ho e trovo un set di azioni da fare
        self.actionExploreCell, self.actionFlag = self.nontrivialStrategy()
        if self.actionExploreCell or self.actionFlag:
            if self.actionFlag:
                return self.actionFlag.pop()  # il pop in un set ritorna un random
            else:
                return self.actionExploreCell.pop()  # possibile raffinamento

        # ragiono a probabilita
        self.actionExploreCell, self.actionFlag = self.leastChanceStrategy()
        if self.actionFlag:
            return self.actionFlag.pop()  # il pop in un set ritorna un random
        else:
            return self.actionExploreCell.pop()  # possibile raffinamento

    def trivialStrategy(self, ):
        pass

    def nontrivialStrategy(self, ):
        pass

    def leastChanceStrategy(self, ):
        pass

    def randomStart(self):
        row = random.randint(0, self.game.row - 1)
        col = random.randint(0, self.game.col - 1)
        return row, col

    def play(self):
        pass
