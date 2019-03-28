import random

class Qtable:
    def __init__(self):
        self.table = [[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
                      [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
                      [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
                      [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
                      [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]]

        self.alpha = 0
        self.gamma = 0


    # set alpha value for Q value calculation
    def setalpha(self, value):
        self.alpha = value

    # get alpha value
    def getalpha(self):
        return self.alpha


    # set gamma value for Q value calculation
    def setgamma(self, value):
        self.gamma = value

    # get gamma value
    def getgamma(self):
        return self.gamma


        # to set a q value in the table
        # i, j provide location in the world
        # k value:
        # 0 - North
        # 1 - South
        # 2 - East
        # 3 - West
        # 4 - Pickup
        # 5 - Dropoff
    def setqvalue(self, i, j, k, value):
        self.table[i][j][k] = value


    # to retrieve a value from the table
        # i, j provide location in the world
        # k value:
        # 0 - North
        # 1 - South
        # 2 - East
        # 3 - West
        # 4 - Pickup
        # 5 - Dropoff
    def get(self, i, j, k):
        return self.table[i][j][k]


    # this can be used to determine the next move when using P-Exploit/P-Greedy policies
    # returns value 0-3 for north, south, east, west
    # I didn't include values for pickup/dropoff because I believe these actions happen automatically when applicable
    def maxdirection(self, i, j):
        max = self.get(i,j,0)
        direction = 0
        for k in range(1,5):
            value = self.get(i,j,k)

            if (value > max):
                max = value
                direction = k

            # if the values are the same, choose randomly
            elif (value == max):
                if (random.random() > 0.5):
                    max = value
                    direction = k
                else:
                    max = max

        return direction


    # used to update Q values in the table
    # avatar is was previously in state (i, j, k), and is now in (iprime, jprime, kprime),
    # where (i, j)/(iprime, jprime) are positions in the world, k is the last move performed,
    # and kprime is the next move about to be performed
        # k/kprime values:
        # 0 - North
        # 1 - South
        # 2 - East
        # 3 - West
        # 4 - Pickup
        # 5 - Dropoff
    def updateSARSA(self, i, j, k, iprime, jprime, kprime):
        alpha = self.getalpha()
        gamma = self.getgamma()

        # if the previous action was pickup of dropoff, set reward to 13, otherwise set to -1
        if (k == 5 or k == 6):
            reward = 13
        else:
            reward = -1

        # Update formula:
        # Q(i,j,k) <- (1-alpha) * Q(i,j,k) + alpha * [Reward(k) + gamma * Q(iprime, jprime, kprime)]
        # Q(i,j,k) is the previous state to be updated
        # Q(iprime, jprime, kprime) is the current state with the next action chosen as kprime

        newvalue = ((1-alpha) * self.get(i,j,k)) + alpha * (reward + gamma * self.get(iprime, jprime, kprime))
        self.setqvalue(i,j,k, newvalue)

    # Copy/pasted from updateSARSA, except this does not include the kprime argument, as this value is chosen based
    # the maximum known value, not what move is actually being taken
    def updateQLEARN(self, i, j, k, iprime, jprime):
        alpha = self.getalpha()
        gamma = self.getgamma()

        kprime = self.maxdirection(iprime, jprime)

        # if the previous action was pickup of dropoff, set reward to 13, otherwise set to -1
        if (k == 4 or k == 5):
            reward = 13
        else:
            reward = -1

        # Update formula:
        # Q(i,j,k) <- (1-alpha) * Q(i,j,k) + alpha * [Reward(k) + gamma * maxQ(iprime, jprime, kprime)]
        # Q(i,j,k) is the previous state to be updated
        # Q(iprime, jprime, kprime) is the current state with the next action chosen as kprime
        newvalue = ((1-alpha) * self.get(i,j,k)) + alpha * (reward + gamma * self.get(iprime, jprime, kprime))
        self.setqvalue(i,j,k, newvalue)


    def print(self):
        print("Current Q Table -- Alpha =", self.getalpha(), ", Gamma =", self.getgamma())
        for i in range(5):
            for j in range(5):
                print(self.table[i][j], end=", ")
            print()
        print()


### TESTING ###

table = Qtable()
table.print()

table.setalpha(0.5)
table.setgamma(0.5)

table.updateQLEARN(0,0,2, 0,1)
table.print()

table.updateQLEARN(0,1,4, 0,1)
table.print()
