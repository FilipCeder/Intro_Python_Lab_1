from math import sin,cos,radians
import random

#TODO: Deal with all TODOs in this file and also remove the TODO and HINT comments.

""" This is the model of the game"""
class Game:
    def __init__(self, cannonSize, ballSize):
        self.player0 = Player(self, "blue", -90, cannonSize, ballSize)
        self.player1 = Player(self, "red", 90, cannonSize, ballSize)
        self.currentPlayer = self.player0
        self.wind = 0

    def getPlayers(self):
        return [self.player0, self.player1]

    def getCannonSize(self):
        return self.player0.cannonSize  # Assuming both players have the same cannon size

    def getBallSize(self):
        return self.player0.ballSize  # Assuming both players have the same ball size

    def getCurrentPlayer(self):
        return self.currentPlayer

    def getOtherPlayer(self):
        return self.player1 if self.currentPlayer == self.player0 else self.player0

    def getCurrentPlayerNumber(self):
        return 0 if self.currentPlayer == self.player0 else 1

    def nextPlayer(self):
        self.currentPlayer = self.getOtherPlayer()

    def setCurrentWind(self, wind):
        self.wind = wind

    def getCurrentWind(self):
        return self.wind

    def newRound(self):
        self.setCurrentWind(random.randint(-10, 10))

""" Models a player """
class Player:
    def __init__(self, game, color, posx, cannonSize, ballSize):
        self.game = game
        self.color = color
        self.posx = posx
        self.cannonSize = cannonSize
        self.ballSize = ballSize
        self.angle = 45
        self.velocity = 40
        self.score = 0

    def fire(self, angle, velocity):
        projectile = Projectile(self.angle, self.velocity, self.game.getCurrentWind(), self.posx, 5, -self.game.getCannonSize() / 2, self.game.getCannonSize() / 2)
        return projectile

    def projectileDistance(self, proj):
        distance = proj.getX() - self.posx - (self.cannonSize + self.ballSize) / 2
        return max(distance, 0)  # Ensure the distance is non-negative

    def getScore(self):
        return self.score

    def increaseScore(self):
        self.score += 1

    def getColor(self):
        return self.color

    def getX(self):
        return self.posx

    def getAim(self):
        return self.angle, self.velocity

    # Implement other methods as per your game logic


""" Models a projectile (a cannonball, but could be used more generally) """
class Projectile:
    def __init__(self, angle, velocity, wind, xPos, yPos, xLower, xUpper):
        self.yPos = yPos
        self.xPos = xPos
        self.xLower = xLower
        self.xUpper = xUpper
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)
        self.wind = wind

    def update(self, time):
        yvel1 = self.yvel - 9.8 * time
        xvel1 = self.xvel + self.wind * time

        self.xPos = self.xPos + time * (self.xvel + xvel1) / 2.0
        self.yPos = self.yPos + time * (self.yvel + yvel1) / 2.0

        self.yPos = max(self.yPos, 0)
        self.xPos = max(self.xPos, self.xLower)
        self.xPos = min(self.xPos, self.xUpper)

        self.yvel = yvel1
        self.xvel = xvel1

    def isMoving(self):
        return 0 < self.getY() and self.xLower < self.getX() < self.xUpper

    def getX(self):
        return self.xPos

    def getY(self):
        return self.yPos
