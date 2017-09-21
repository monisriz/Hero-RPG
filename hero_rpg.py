#!/usr/bin/env python

# Hero RPG
# In this simple RPG game, the hero fights the goblin. He has the options to:
# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        enemy.health -= self.power
        print("{} inflicted {} damage to {}.".format(self.name, self.power, enemy.name))
        if enemy.health <= 0:
            print("{} is dead.".format(enemy.name))

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

class Hero(Character):
    pass

class Goblin(Character):
    pass

class Zombie(Character):
    pass

def main():
    hero = Hero(10, 5, 'Heera')
    goblin = Goblin(6, 2, 'Gobby')
    zombie = Zombie(100, 100, 'Zoomba')

    menuchoice = input("Press 1 or 2 to choose your opponent: \n1. Gobby\n2. Zoomba:\n")

    if menuchoice == "1":
        enemy = goblin

    if menuchoice == "2":
        enemy = zombie

    print("\n{} v/s {}\n".format(hero.name.upper(), enemy.name.upper()))

    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. Fight {}".format(enemy.name))
        print("2. Do nothing")
        print("3. Run away")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(enemy)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("{} ran away!".format(hero.name))
            break
        else:
            print("Invalid input {}".format(raw_input))
        if enemy.alive():
            enemy.attack(hero)

main()
