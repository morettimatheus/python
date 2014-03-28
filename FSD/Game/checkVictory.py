import screenprint

class checkVictory:
    def __init__(self, gameplay, rows):
        self.gameplay = gameplay
        self.rows = rows

    def check(self, gameplay, rows):
        no_crosses = 0
        no_noughts = 0
        for i in range(rows):
            for j in range(rows):
                if gameplay[i][j] == 1: #if the result is a X
                    no_crosses += 1
                    print("adding 1 to no crosses")

                elif gameplay [i][j] == 2:
                    no_noughts += 1
                    print("adding 1 to no noughts")

                if no_noughts == rows:
                    #return noughts
                    print("O winner")

                elif no_crosses == rows:
                    print("X winner")
                    #return crosses

            no_noughts = 0
            no_crosses = 0