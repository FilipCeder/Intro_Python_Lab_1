from math import sin,cos,radians
import random



""" This is the model of the game"""
class Game:
    def __init__(self, cannonSize, ballSize):
        #initialize both players
        self.player0 = Player(self, "blue", -90, cannonSize, ballSize, False)
        self.player1 = Player(self, "red", 90, cannonSize, ballSize, True)
        self.currentPlayer = self.player0
        self.wind = 0

    def getPlayers(self): #Get a list of all players
        return [self.player0, self.player1]

    def getCannonSize(self): #Get the cannonsize assuming that both players have the same cannonsize
        return self.player0.cannonSize  #

    def getBallSize(self): #Get the ballsize assuming that both players have the same ballsize
        return self.player0.ballSize  

    def getCurrentPlayer(self): 
        return self.currentPlayer

    def getOtherPlayer(self): #Get the player that isnot the current player
        return self.player1 if self.currentPlayer == self.player0 else self.player0

    def getCurrentPlayerNumber(self): #Get the number of the current player
        return 0 if self.currentPlayer == self.player0 else 1

    def nextPlayer(self): #Change which player is the current player
        self.currentPlayer = self.getOtherPlayer()

    def setCurrentWind(self, wind):
        self.wind = wind

    def getCurrentWind(self):
        return self.wind

    def newRound(self): #Sets the wind to a random number between -10 and 10 on round start
        self.setCurrentWind(random.randint(-10, 10))

""" Models a player """
class Player:
    def __init__(self, game, color, posx, cannonSize, ballSize, isReversed):
        #initializes all elements of a player
        self.game = game
        self.color = color
        self.posx = posx
        self.cannonSize = cannonSize
        self.ballSize = ballSize
        self.angle = 45
        self.velocity = 40
        self.score = 0
        self.isReversed = isReversed

    def fire(self, angle, velocity):
        self.angle = angle  #Updates the angle
        if self.isReversed: #Reverse the angle if the player shoots to the left
            self.angle = 180 - angle  
        self.velocity = velocity  #Updates the velocity
        projectile = Projectile(self.angle, self.velocity, self.game.getCurrentWind(), self.posx, 5, -110, 110) #Runs the projectile class
        return projectile

    def projectileDistance(self, proj):
        playerCenter = self.posx
        projectileCenter = proj.getX()
        #Checks if the distance shoud be calculated to the right or left player and calculates the distance from the cannon to the ball
        if projectileCenter - playerCenter < 0:
            distance = projectileCenter - playerCenter + (self.cannonSize / 2 + self.ballSize)
        else:
            distance = projectileCenter - playerCenter - (self.cannonSize / 2 + self.ballSize)
        if abs(distance) <= (self.cannonSize / 2 + self.ballSize): #Returns distance 0 if a hit
            return 0
        return distance


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
        #Initializes all elements of the projectile
        self.yPos = yPos
        self.xPos = xPos
        self.xLower = xLower
        self.xUpper = xUpper
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)
        self.wind = wind

    def update(self, time):
        yvel1 = self.yvel - 9.8 * time #Sets the verical velocity of the projectile
        xvel1 = self.xvel + self.wind * time #Sets the Horizontal velocity of the projectile

        #Calculates the position of the projectile
        self.xPos = self.xPos + time * (self.xvel + xvel1) / 2.0 
        self.yPos = self.yPos + time * (self.yvel + yvel1) / 2.0

        self.yPos = max(self.yPos, 0) #Projectiles y position can not go below 0
        self.xPos = max(self.xPos, self.xLower) #Projectiles x position can not go outside the predifined scope
        self.xPos = min(self.xPos, self.xUpper)

        #Updates the vertical and horizontal velocity of the projectile
        self.yvel = yvel1
        self.xvel = xvel1

    def isMoving(self):
        return 0 < self.getY() and self.xLower < self.getX() < self.xUpper

    def getX(self):
        return self.xPos

    def getY(self):
        return self.yPos

