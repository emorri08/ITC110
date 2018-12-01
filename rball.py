#rball.py
# simulation of a racketball game

from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

def printIntro():
    print("This program simulates a game of racquetball between")
    print("two players, A and B. Each player's ability is")
    print("indicated by a probability that the player wins")
    print("the point when serving. Player A always serves first")

def getInputs():
    a = float(input("What is the probability of player A to win a serve? "))
    b = float(input("What is the probability of player B to win a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    # simulate n games between players
    # return the number of wins for A and B
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else: winsB += 1
    return winsA, winsB

def simOneGame(probA, probB):
    # simulate single game and return final scores for A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a,b):
    #A and B are the scores
    #return true if the game is over, false otherwise
    return a == 15 or b == 15

def printSummary(winsA, winsB):
    n = winsA + winsB
    print("Games simulated", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__ == '__main__': main()