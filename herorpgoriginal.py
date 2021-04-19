# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print("{} does damage to the {}.".format(self.name, enemy.name))
        if enemy.health <= 0:
            print("The {} is dead.".format(enemy.name))

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

class Hero(Character):
    pass

class Goblin(Character):
    pass

#class Zombie(Character):
 #   pass

def main():

    hero = Hero("Hero", 10, 5)
    goblin = Goblin("Goblin", 6, 2)
    #zombie = Zombie("Zombie", 100, 70)

    while hero.alive():# or zombie.alive() and hero.alive():
        hero.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. fight hero")
        print("3. hero fight's zombie")
        print("4. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(goblin)
        elif raw_input == "2":
            goblin.attack(hero)
            #hero.print_status()
            #goblin.print_status()
        elif raw_input == "3":
            pass
            #zombie.attack(hero)
            #zombie.print_status()
            #hero.print_status()
        elif raw_input == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

main()