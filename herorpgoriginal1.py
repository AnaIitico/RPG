# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
import random

class Character:
    def __init__(self, health, power, armor, dodge, coinBalance):
        # self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        self.dodge = dodge
        self.coinBalance = coinBalance
    
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Hero(Character):
    def __init__(self, health, power, armor, dodge, coinBalance):
        self.character_name = "Hero"
        super(Hero, self).__init__(health, power, armor, dodge, coinBalance)

    def attack(self, enemy):           
        if self.armor > 0:
            self.health += self.armor
            print("Armor activated")
        if enemy.character_name != "Zombie" and enemy.character_name != "Shadow":
            if random.randint(0,100) < 20:
                selfpower = self.power * 2
                enemy.health -= self.power
                print(f"You do 2X damage to the {enemy.character_name}.")
            else:
                enemy.health -= self.power
        elif enemy.character_name == "Shadow":
            if random.randint(0,100) < 10:
                enemy.health -= self.power
                print("You hit Shadow!")

    def store(self):
        go_back = 0
        while go_back != 4:
            hero.print_status()
            choice = input("""
    Choose a Store Item!
    1) SuperTonic restores 10 Health points
        5 Coins
    2) Armor will add 2 Armor points
        7 Coins
    3) Evade will add 1 Evade points/coin
        2 Points = 10% probability of dodging attack
        4 Points = 15% probability of dodging attack
        6 Points = 20% probability of dodging attack
    4) Return to Store
    """ )
            if choice == "1":
                if self.coinBalance < 5:
                    print("You need at least 5 Coins!")

                else:
                    buy = input("Enter Y to pay 5 Coins for the SuperTonic>> ")
                    if buy == "y":
                        self.health += 10
                        self.coinBalance -= 5
                    else:
                        print("Invalid input {}".format(buy))
                        # continue
            if choice == "2":
                if self.coinBalance < 7:
                    print("You need at least 7 Coins!")

                else:
                    buy = input("Enter Y to pay 7 Coins for the Armor>> ")
                    if buy == "y":
                        self.armor += 2
                        self.coinBalance -= 7
                    else:
                        print("Invalid input {}".format(buy))
                # continue
            if choice == "3":
                coins = 1
                while coins != 0:
                    print("Enter the number of Evade Points you want to buy")
                    print("Enter 0 to return to Store")
                    coins = int(input())
                    #continue
                    if coins == 2 or coins == 4 or coins == 6:
                        self.dodge += coins
                        self.coinBalance -= coins
                        hero.print_status()
                    else:
                        print("Invalid input {}".format(coins))
                        continue
            if choice == "4":
                go_back = 4
            else:
                print("Invalid input {}".format(choice))

    def evade(self, enemy):
        r = range(2, 3)
        r1 = range(4, 5)
        r2 = range(6, 100)
        if self.dodge in r:
            if random.randint(0,100) < 10:
                print("Evade activated")
        elif self.dodge in r1:
            if random.randint(0,100) < 15:
                print("Evade activated")
        elif self.dodge in r2:
            if random.randint(0,100) < 20:
                print("Evade activated")
        else:
            print("No Evade available")

    def print_status(self):
        print("You have {} health, {} power, {} armor, {} dodge, and {} coins.".format(self.health, self.power, self.armor, self.dodge, self.coinBalance))
            
class Goblin(Character):
    def __init__(self, health, power, armor, dodge, coinBalance):
        self.character_name = "Goblin"
        super(Goblin, self).__init__(health, power, armor, dodge, coinBalance)

    def attack(self, enemy):
        #hero.evade()
        enemy.health -= self.power
        print("The Goblin does {} damage to you.".format(self.power))
        
    def print_status(self):
        print("The Goblin has {} health, {} power, {} armor, {} dodge, and {} coins.".format(self.health, self.power, self.armor, self.dodge, self.coinBalance))

class Medic(Character):
    def __init__(self, health, power, armor, dodge, coinBalance):
        self.character_name = "Medic"
        super(Medic, self).__init__(health, power, armor, dodge, coinBalance)

    def attack(self, enemy):
        enemy.health -= self.power
        print("The Medic does {} damage to you.".format(self.power))
        if random.randint(0,100) < 20:
            self.health = self.health + 2
            print("The Medic gained 2 points of extra health")
        
    def print_status(self):
        print("The Medic has {} health, {} power, {} armor, {} dodge, and {} coins.".format(self.health, self.power, self.armor, self.dodge, self.coinBalance))

class Shadow(Character):
    def __init__(self, health, power, armor, dodge, coinBalance):
        self.character_name = "Shadow"
        super(Shadow, self).__init__(health, power, armor, dodge, coinBalance)
        
    def attack(self, enemy):
        enemy.health -= self.power
        print("Shadow does {} damage to you.".format(self.power))
        
    def print_status(self):
        print("The Shadow has {} health, {} power, {} armor, {} dodge, and {} coins.".format(self.health, self.power, self.armor, self.dodge, self.coinBalance))

class Zombie(Character):
    def __init__(self, health, power, armor, dodge, coinBalance):
        self.character_name = "Zombie"
        super(Zombie, self).__init__(health, power, armor, dodge, coinBalance)

    def attack(self, enemy):
        enemy.health -= self.power
        print("The Zombie does {} damage to you.".format(self.power))
        
    def print_status(self):
        print("The Zombie has {} health, {} power, {} armor, {} dodge, and {} coins.".format(self.health, self.power, self.armor, self.dodge, self.coinBalance))

class TechnicalBoy(Character):
    def __init__(self, health, power, armor, dodge, coinBalance):
        self.character_name = "Technical Boy"
        super(TechnicalBoy, self).__init__(health, power, armor, dodge, coinBalance)

    def attack(self, enemy):
        enemy.health -= self.power
        print("Technical Boy does {} damage to you.".format(self.power))

    def print_status(self):
        print("Technical Boy has {} health, {} power, {} armor, {} dodge, and {} coins.".format(self.health, self.power, self.armor, self.dodge, self.coinBalance))

class MrWednesday(Character):
    def __init__(self, health, power, armor, dodge, coinBalance):
        self.character_name = "Mr. Wednesday"
        super(MrWednesday, self).__init__(health, power, armor, dodge, coinBalance)

    def attack(self, enemy):
        enemy.health -= self.power
        print("Mr. Wednesday does {} damage to you.".format(self.power))
        
    def print_status(self):
        print("Mr. Wednesday has {} health, {} power, {} armor, {} dodge, and {} coins.".format(self.health, self.power, self.armor, self.dodge, self.coinBalance))

dodger = False
hero = Hero(10, 5, 2, 4, 2)
goblin = Goblin(6, 2, 0, 0, 2)
medic = Medic(7, 4, 0, 0, 2)
shadow = Shadow(1, 3, 0, 0, 2)
zombie = Zombie(7, 4, 0, 0, 2)
technicalBoy = TechnicalBoy(7, 3, 0, 0, 2)
mrWednesday = MrWednesday(9, 3, 0, 0, 2)

def main():
    while hero.alive():
        print()
        print("You are the Hero in this game")
        print("What do you want to do?")
        print(f"1. fight an enemy")
        print("2. go to the store")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            print("Choose an enemy?")
            print(f"""
    1 = Goblin
    2 = Medic
    3 = Shadow
    4 = Zombie
    5 = Technical Boy
    6 = Mr. Wednesday
""")
            print("> ", end=' ')
            choice = input()
            if choice == "1":
                hero.print_status()
                goblin.print_status()
                hero.attack(goblin)
                if goblin.alive():
                    hero.evade(Goblin)
                    if hero.evade(Goblin):
                        print("Evade activated" + str(dodger))
                    else:
                        #print("This is line 252 not Dodger")
                        goblin.attack(hero)
                if not goblin.alive():
                    print("The Goblin is dead.")
                    break
            elif choice == "2":
                hero.print_status()
                medic.print_status()
                hero.attack(medic)
                if medic.alive():
                    medic.attack(hero)
                if not hero.alive():
                    print("You are dead.")
                if not hero.alive():
                    print("You are dead.")
                if not medic.alive():
                    print("The Medic is dead.")
                    break
            elif choice == "3":
                hero.print_status()
                shadow.print_status()
                hero.attack(shadow)
                if shadow.alive():
                    shadow.attack(hero)
                if not hero.alive():
                    print("You are dead.")
                if not shadow.alive():
                    print("The Shadow is dead.")
                    break
            elif choice == "4":
                 hero.print_status()
                 zombie.print_status()
                 hero.attack(zombie)
                 if zombie.alive():
                    zombie.attack(hero)
                 if not hero.alive():
                    print("You are dead.")
                 if not zombie.alive():
                    print("The Zombie is dead.")
            elif choice == "5":
                 hero.print_status()
                 technicalBoy.print_status()
                 hero.attack(technicalBoy)
                 if technicalBoy.alive():
                    technicalBoy.attack(hero)
                 if not hero.alive():
                    print("You are dead.")
                 if not technicalBoy.alive():
                    print("Technical Boy is dead.")
            elif choice == "6":
                 hero.print_status()
                 mrWednesday.print_status()
                 hero.attack(mrWednesday)
                 if mrWednesday.alive():
                    mrWednesday.attack(hero)
                 if not hero.alive():
                    print("You are dead.")
                 if not mrWednesday.alive():
                    print("Mr. Wednesday is dead.")
            else:
                print("Invalid input {}".format(choice))
        
        elif raw_input == "2":
            if hero.coinBalance < 2:
                print("You need at least 2 Coins!")
                print("Win a battle, earn 2 Coins!")
                continue
                #main
            goBack = 1
            while goBack != 0:
                print(f"""
    1 = Hero Store
    0 to go back
""")
                print("> ", end=' ')
                choose = input()
                if choose == "1":
                    #print("Line 278 executed")
                    hero.store()
                if choose == "0":
                    #print("Line 281 worked")
                    goBack = 0
                else:
                    print("Invalid input {}".format(choose))
        elif raw_input == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid input {}".format(raw_input)) 

main()