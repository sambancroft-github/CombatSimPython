from random import randint


class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventoryPack = self.inventory()
        self.alive = True
        self.defence = randint(3, 10)
        self.damage = randint(3, 10)
        self.playerDamage = []
        self.playerDefence = []

    def Player_Pack_Check(self):
        for counter, item in enumerate(self.inventoryPack):
            print(counter, item)

    def Player_Health_Check(self):
        print("{} has {} health left".format(self.name, self.health))

    def isAlive(self):
        if self.health > 0:
            self.Player_Health_Check()
        else:
            self.alive = False

    def inventory(self):
        inventory_to_use = []
        items = ["Apple", "Sword", "Shield", "Dagger"]

        for item_in_items in range(2):
            if item_in_items <= 2:
                index = randint(0, len(items))-1
                inventory_to_use.append(items[index])
                del items[index]
        return inventory_to_use

    def item_usage(item, self):
        if item == "Apple":
            self.health += 20
            self.inventoryPack.remove(item)
            print("{} used the {}".format(self.name, item))
        elif item == "Sword":
            self.damage += 10
            self.inventorypack.remove(item)
            print("{} used the {}".format(self.name, item))
        elif item == "Shield":
            self.defence += 10
            self.inventorypack.remove(item)
            print("{} used the {}".format(self.name, item))
        elif item == "Dagger":
            self.damage += 5
            self.inventorypack.remove(item)
            print("{} used the {}".format(self.name, item))

    def Player_report(self, randdamage, enemy):
        self.playerDamage.append(self.damage + randdamage)
        self.playerDefence.append(enemy.defence)


playeroneTurn = True

playerOne = Character("sam")
playerTwo = Character("james")


def attack(playerA, playerB):
    randomdamage = randint(0, 10)
    print("rnadom damage {}".format(randomdamage))
    if playerB.defence > (playerA.damage + randomdamage):
        print("{} defence over powered {}'s attack".format(playerB.name, playerA.damage))
    else:
        playerB.health -= (playerA.damage - playerB.defence) + randomdamage
    playerB.isAlive()
    playerA.Player_report(randomdamage, playerB)


while playerOne.alive and playerTwo.alive:
    if playeroneTurn:
        playeroneTurn = False
        print("{}'s turn".format(playerOne.name))
        if playerOne.inventoryPack:
            playerOne.Player_Pack_Check()
            userPlayerOne = "no" #input("do you want to use an item?  yes or no").lower()
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
        print("{}'s turn".format(playerTwo.name))
        if playerTwo.inventoryPack:
            playerTwo.Player_Pack_Check()
            userPlayerTwo = "no" #input("do you want to use an item?  yes or no").lower()
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

if playerOne.health > 0:
    print("{} has won, with {} health left".format(playerOne.name, playerOne.health))
else:
    print("{} has won, with {} health left".format(playerTwo.name, playerTwo.health))

print("analysis of the game")
for i in playerOne.playerDamage:
    print(i)
for i in playerTwo.playerDefence:
    print(i)


import matplotlib.pyplot as plt

plt.plot(playerOne.playerDamage, playerTwo.playerDefence)
plt.show()

