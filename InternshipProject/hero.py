'''
Joseph Erwin
Internship Game Project
'''

from powers import *
from random import choice

class Hero(object):
    def __init__(self,heroString):
        # Split string into list of 3 elements
        heroList = heroString.split("|")

        # Assign current health, max health, and name (elements 3 and 3)
        self.__maxHealth = int(heroList[2])
        self.__currHealth = int(heroList[2])

        # Create list of powers
        powersList = heroList[1].split(",")
        objectList = []

        # Create list of power objects
        for i in powersList:
            objectList.append(powerFactory(i))

        # Assign power objects list to private member variable powers
        self.__powers = objectList

        # Assign name to private member variable name
        self.__name = heroList[0]

    def getName(self):
        # Get the hero's name
        return self.__name

    def getHealth(self):
        # Get the current health of the hero
        return self.__currHealth

    def __str__(self):
        output = "{} has the following powers...".format(self.__name)

        #print(self.__powers)
        # Loop through and print each power in list
        for i in self.__powers:
            output += "\n\t" + str(i)
        return output

    def useRandomPower(self):
        powerUsed = choice(self.__powers)

        # Show name of hero and what power is being used
        print(self.__name + " " + powerUsed.use())

        # return the power being used
        return powerUsed

    def takeDamage(self):
        # Reduce hero's health by 1
        self.__currHealth -= 1

    def resetHealth(self):
        # Reset hero's health to original value
        self.__currHealth = self.__maxHealth