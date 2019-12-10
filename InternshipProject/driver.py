'''
Joseph Erwin
Internship Game Project
'''

from hero import Hero
from os import path, chdir

def selectHero(heroList, prompt):
    # Ask the user to provide input based on the prompt
    heroNum = int(input(prompt))

    # Return the hero at the input index
    return heroList[heroNum]

def heroCombat(heroes):

    # List all heroes and their indices
    print("Here are the heroes and their indices:")
    for i in range(len(heroes)):
        print("{}: {}".format(i,heroes[i].getName()))

    # Prompt the user for a selection of the heroes
    print("-"*50)

    # Ensure input is valid
    while True:
        try:
            hero1 = selectHero(heroes, "Select your first hero: ")
            hero2 = selectHero(heroes, "Select your second hero: ")
            break
        except:
            continue

    print("-" * 50)

    # Fight while at least one of the heroes has greater than 0 health
    while hero1.getHealth() > 0 and hero2.getHealth() > 0:
        # Print the health for each hero
        print("{} has {} health".format(hero1.getName(), hero1.getHealth()))
        print("{} has {} health".format(hero2.getName(), hero2.getHealth()))

        # Generate random powers for each hero
        h1Power = hero1.useRandomPower()
        h2Power = hero2.useRandomPower()

        # Determine winner of fight
        outcome = h1Power.fight(h2Power)

        # Depending upon outcome, inflict damage on heroes
        if outcome == 1:
            hero2.takeDamage()
        elif outcome == -1:
            hero1.takeDamage()
        else:
            hero1.takeDamage()
            hero2.takeDamage()
        print("-"*50)

    # Print out the result of the round
    if hero1.getHealth() > hero2.getHealth():
        print(hero1.getName() + " WINS!")
    else:
        print(hero2.getName() + " WINS!")

def main():
    heroes = []

    print("Welcome to the hero fighter!")
    print("-"*50)
    while True:
        print()
        printMenu()

        # Ask user for a selection
        choice = input("> ")

        # Ensure selection is an integer
        try:
            choice = int(choice)
        except:
            return

        # Load file if choice is 1
        heroes = loadHeroes("heroes.txt")

        # Print roster of all heroes if choice is 2
        if choice == 1:
            # Print roster of all loaded heroes
            printRoster(heroes)

        # Print a message to built excitement in the user's heart
        elif choice == 2:
            heroCombat(heroes)
        else:
            print("Quitting...")
            break

def loadHeroes(fileName):
    # List to store lines of input file
    heroes = []

    while True:
        # Ensure file name is valid; if not, request a valid one
        try:
            # Open file
            with open(fileName,"r") as file:
                # Iterate through file and append each line to the list
                for line in file:
                    hero = Hero(line.strip())

                    heroes.append(hero)
            break
        except:
            fileDirec = input("Please input the correct path for the heroes.txt file: ")
            chdir(fileDirec)
            continue


    # return the hero list
    return heroes

def printRoster(heroes):
    # tell the user how many heroes are loaded
    print("The following {} heroes are loaded...".format(str(len(heroes))))

    # Print all heroes
    for i in heroes:
        print("*" * 50)
        print(i)

    print("*" * 50)


def printMenu():
    # Show options to user
    print("Choose an option:\n1. Print Hero Roster\n2. Hero Fight!\n3. Quit")

main()