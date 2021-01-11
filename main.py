from random import randint


censored_words = ["blah", "blah blah", "player", "unknown"]

class Character:
    #character object
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventoryPack = self.inventory()
        self.alive = True
        self.defence = randint(3, 10)
        self.damage = randint(3, 10)
        self.playerDamage = []
        self.playerDefence = []

    def __str__(self):
        return f"{self.name}, HP: {self.health}, items: {self.inventoryPack}"

    #This is so player can see whats in the inventory and it will be numbered aswell
    def Player_Pack_Check(self):
        for counter, item in enumerate(self.inventoryPack):
            print(counter, item)

    #to check how much health is left after a attack
    def Player_Health_Check(self):
        print("{} has {} health left".format(self.name, self.health))

    #to check is player is alive
    def isAlive(self):
        if self.health > 0:
            self.Player_Health_Check()
        else:
            self.alive = False
    #randomizes the inventory for each player, also removes item that is already been selected
    def inventory(self):
        inventory_to_use = []
        items = ["Apple", "Sword", "Shield", "Dagger"]

        for item_in_items in range(2):
            if item_in_items <= 2:
                index = randint(0, len(items))-1
                inventory_to_use.append(items[index])
                del items[index]
        return inventory_to_use
    #when am item is used to then get the corrisponding action for the item, basic layout
    def item_usage(item, self):
        if item == "Apple":
            self.health += 20
            self.inventoryPack.remove(item)
            print(f"{self.name} used the {item}")
        elif item == "Sword":
            self.damage += 10
            self.inventorypack.remove(item)
            print(f"{self.name} used the {item}")
        elif item == "Shield":
            self.defence += 10
            self.inventorypack.remove(item)
            print(f"{self.name} used the {item}")
        elif item == "Dagger":
            self.damage += 5
            self.inventorypack.remove(item)
            print(f"{self.name} used the {item}")


    #for game analysis at the end
    def Player_report(self, randdamage, enemy):
        self.playerDamage.append(self.damage + randdamage)
        self.playerDefence.append(enemy.defence)

playeroneTurn = True

playerOne = Character("")
playerTwo = Character("")

#define platers name
def player_name(player):
    while player.name == "":
        playerName = str(input("please enter player one's name: "))
        for i in censored_words:
            if playerName == i:
                print("please choose another name")
                playerName = ""
                break
            elif playerName == playerTwo.name or playerName == playerOne.name:
                print("please choose another name")
                playerName = ""
                break
            else:
                player.name = playerName


player_name(playerOne)
player_name(playerTwo)

#this is the random for the attacking
def attack(playerA, playerB):
    randomdamage = randint(0, 10)
    print(f"random damage: {randomdamage}")
    if playerB.defence > (playerA.damage + randomdamage):
        print(f"{playerB.name} defence over powered {playerA.damage}'s attack")
    else:
        playerB.health -= (playerA.damage - playerB.defence) + randomdamage
    playerB.isAlive()
    playerA.Player_report(randomdamage, playerB)

#starting of game, if both are alive
while playerOne.alive and playerTwo.alive:
    print(f"Welcome Player One: {playerOne.name} and Player Two: {playerTwo.name}")
    if playeroneTurn:
        playeroneTurn = False
        print(f"{playerOne}")
        print(f"{playerOne.name}'s turn")
        if playerOne.inventoryPack:
            playerOne.Player_Pack_Check()
            userPlayerOne = "no"
            #uncomment this line to enable the player to choose which item to use
            #input("do you want to use an item?  yes or no").lower()
            if userPlayerOne == "yes":
                itemtouse = int(input("which item do you want to use, please enter the number"))
                for i in range(len(playerOne.inventoryPack)):
                    if i == itemtouse:
                        playerOne.item_usage(playerOne.inventoryPack[i])
                        break
                    else:
                        print("ERROR: you entered a invalid number")
            else:
                attack(playerOne, playerTwo)
        else:
            attack(playerOne, playerTwo)
    else:
        playeroneTurn = True
        print(f"{playerTwo}")
        print(f"{playerTwo.name}'s turn")
        if playerTwo.inventoryPack:
            playerTwo.Player_Pack_Check()
            userPlayerTwo = "no"
            # uncomment this line to enable the player to choose which item to use
            #input("do you want to use an item?  yes or no").lower()
            if userPlayerTwo == "yes":
                itemtouse = int(input("which item do you want to use, please enter the number"))
                for i in range(len(playerTwo.inventoryPack)):
                    if i == itemtouse:
                        playerTwo.item_usage(playerTwo.inventoryPack[i])
                        break
                    else:
                        print("ERROR: you entered a invalid number")
            else:
                attack(playerTwo, playerOne)
        else:
            attack(playerTwo, playerOne)
            

def gameCondictionCheck():
    if playerOne.isAlive():
        print(f"{playerOne.name} has won, with {playerOne.health} health left")
    elif playerTwo.isAlive():
        print(f"{playerTwo.name} has won, with {playerTwo.health} health left")
    else:
        print("ERROR: run game again")
        
        
gameCondictionCheck()

print("analysis of the game")
"""
for i in playerOne.playerDamage:
    print(i)
for i in playerTwo.playerDefence:
    print(i)
"""

import matplotlib.pyplot as plt

plt.plot(playerOne.playerDamage, playerTwo.playerDefence)
plt.show()

