'''
Joseph Erwin
Internship Game Project
'''

class Power(object):
    # Assign description to object
    def __init__(self, description):
        self.__powerDescription = description

    # Return description for string method
    def __str__(self):
        return self.__powerDescription

    # Return name of class
    def getName(self):
        return self.__class__.__name__

    # Function to indicate that the power has been used
    def use(self):
        return "Power superclass has been used"

    def fight(self,otherPower):
        return 0

class Flight(Power):
    # Initialize object with description specified
    def __init__(self):
        Power.__init__(self, "Flight")

    # Return description of action
    def use(self):
        return "flies into the air!"

    # Fight other power and determine if other power will win
    def fight(self, otherPower):
        resDict = {"Flight":0,"Gadgets":-1,"Intelligence":1,"Laser":-1,"Nationalism":1,"Strength":1}
        oPower = otherPower.getName()

        # Returns 1 for win, -1 for loss or 0 for tie
        outcome = resDict[oPower]

        # Tells the user who won
        if outcome == 1:
            print(self.getName() + " wins!")
        elif outcome == -1:
            print(otherPower.getName() + " wins!")

        # Return the outcome
        return outcome

class Gadgets(Power):
    def __init__(self):
        Power.__init__(self, "Gadgets")
    def use(self):
        return "engages manifestations of material wealth and extreme, prolonged ingenuity!"
    def fight(self, otherPower):
        resDict = {"Flight":1,"Gadgets":0,"Intelligence":-1,"Laser":1,"Nationalism":1,"Strength":-1}
        oPower = otherPower.getName()

        outcome = resDict[oPower]

        if outcome == 1:
            print(self.getName() + " wins!")
        elif outcome == -1:
            print(otherPower.getName() + " wins!")

        return outcome

class Intelligence(Power):
    def __init__(self):
        Power.__init__(self, "Intelligence")
    def use(self):
        return "seriously considers the situation!"
    def fight(self, otherPower):
        resDict = {"Flight":-1,"Gadgets":1,"Intelligence":0,"Laser":-1,"Nationalism":1,"Strength":1}
        oPower = otherPower.getName()

        outcome = resDict[oPower]

        if outcome == 1:
            print(self.getName() + " wins!")
        elif outcome == -1:
            print(otherPower.getName() + " wins!")

        return outcome

class Laser(Power):
    def __init__(self):
        Power.__init__(self, "Laser")
    def use(self):
        return "emits amplified light!"
    def fight(self, otherPower):
        resDict = {"Flight":1,"Gadgets":-1,"Intelligence":1,"Laser":0,"Nationalism":1,"Strength":-1}
        oPower = otherPower.getName()

        outcome = resDict[oPower]

        if outcome == 1:
            print(self.getName() + " wins!")
        elif outcome == -1:
            print(otherPower.getName() + " wins!")

        return outcome

class Nationalism(Power):
    def __init__(self):
        Power.__init__(self, "Nationalism")
    def use(self):
        return "states the pledge of allegiance!"
    def fight(self, otherPower):
        resDict = {"Flight":-1,"Gadgets":-1,"Intelligence":-1,"Laser":-1,"Nationalism":0,"Strength":-1}
        oPower = otherPower.getName()

        outcome = resDict[oPower]

        if outcome == 1:
            print(self.getName() + " wins!")
        elif outcome == -1:
            print(otherPower.getName() + " wins!")

        return outcome

class Strength(Power):
    def __init__(self):
        Power.__init__(self, "Strength")
    def use(self):
        return "does something violent with greater-than-average force!"
    def fight(self, otherPower):
        resDict = {"Flight":-1,"Gadgets":1,"Intelligence":-1,"Laser":1,"Nationalism":1,"Strength":0}
        oPower = otherPower.getName()

        outcome = resDict[oPower]

        if outcome == 1:
            print(self.getName() + " wins!")
        elif outcome == -1:
            print(otherPower.getName() + " wins!")

        return outcome

class SquirrelTalk(Power):
    def __init__(self):
        Power.__init__(self, "Squirrel-Talk")
    def use(self):
        return "summons a squirrel army!"
    def fight(self,otherPower):
        resDict = {"Flight":-1,"Gadgets":-1,"Intelligence":-1,"Laser":-1,"Nationalism":1,"Strength":1}
        oPower = otherPower.getName()

        outcome = resDict[oPower]

        if outcome == 1:
            print(self.getName() + " wins!")
        elif outcome == -1:
            print(otherPower.getName() + " wins!")

# Function to create objects based on input
def powerFactory(powerName):
    if powerName == "flight":
        return Flight()
    elif powerName == "gadget":
        return Gadgets()
    elif powerName == "intel":
        return Intelligence()
    elif powerName == "laser":
        return Laser()
    elif powerName == "national":
        return Nationalism()
    elif powerName == "strength":
        return Strength()
    elif powerName == "squirrel-talk":
        return SquirrelTalk()
    else:
        return