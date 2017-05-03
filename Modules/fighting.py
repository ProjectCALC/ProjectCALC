import random
import time
import sys
import level_module
import weapons
import pickle
import decimal
global weapon_list
global xp
xp = level_module.xp
weapon_list = pickle.load(open("weapons.txt", "rb"))
weapon_list_lower = pickle.load(open("weapons_lower.txt", "rb"))

def main():
    class Character:

        def __init__(self, health):
            self.health = health
        def attack(self, other):     
            raise NotImplementedError

    class Player(Character):

        def __init__(self, health=100):

            super().__init__(health)

        def attack(self, other):
            answer = input("What would you like to do? (Fight, Magic or Item) ")
            if answer.lower() in ['fight','magic','item']:
                if answer.lower() == 'fight':
                    for i in weapon_list:
                        print (i)
                    weapon_choice = input('Which weapon would you like to use? ')
                    while weapon_choice not in weapon_list_lower:
                        print('Please enter a valid weapon name.')
                        weapon_choice = input('Which weapon would you like to use? ')
                    if weapon_choice == 'sword':
                        sword = int(decimal.Decimal(weapons.sword))
                        other.health -= (sword * int(decimal.Decimal(random.uniform(0.1, 1.4))))
                    elif weapon_choice == 'super sword':
                        super_sword = (int(decimal.Decimal(weapons.super_sword)))
                        other.health -= (super_sword * int(decimal.Decimal(random.uniform(0.1, 1.4))))
                    elif weapon_choice == 'hyper sword':
                        hyper_sword = (int(decimal.Decimal(weapons.hyper_sword)))
                        other.health -= (hyper_sword * int(decimal.Decimal(random.uniform(0.1, 1.4))))
                    elif weapon_choice == 'mega blade':
                        mega_blade = (int(decimal.Decimal(weapons.mega_blade)))
                        other.health -= (mega_blade* int(decimal.Decimal(random.uniform(0.1, 1.4))))
                    elif weapon_choice == 'bow':
                        bow = (int(decimal.Decimal(weapons.bow)))
                        other.health -= (bow * int(decimal.Decimal(random.uniform(0.1, 1.4))))
                    elif weapon_choice == 'super bow':
                        super_bow = (int(decimal.Decimal(weapons.super_bow)))
                        other.health -= (super_bow * int(decimal.Decimal(random.uniform(0.1, 1.4))))
                    elif weapon_choice == 'hyper bow':
                        hyper_bow = (int(decimal.Decimal(weapons.hyper_bow)))
                        other.health -= (hyper_bow * int(decimal.Decimal(random.uniform(0.1, 1.4))))
                    elif weapon_choice == 'mega bow':
                        mega_bow = (int(decimal.Decimal(weapons.mega_bow)))
                        other.health -= (mega_bow * int(decimal.Decimal(random.uniform(0.1, 1.4))))   
                elif answer.lower() == 'magic':
                    for i in magic_list:
                        print(i)
                    magic_choice = input('What would you like to cast?')
            while answer.lower() not in ['fight','magic','item']:
                print('Please enter a valid option.')
                answer = input("What would you like to do? (Fight, Magic or Item) ")
                

    class Enemy(Character):

        def __init__(self, name, strength, defense, health):
            super().__init__(health)
            self.name = name
            self.strength = strength
            self.defense = defense

        def attack(self, other):
            print("The {0.name} attacks...".format(self))
            other.health -= int(self.strength * random.uniform(0.1, 1.4))

    def battle(player, enemy):
        print ("An enemy {0.name} appears!".format(enemy))
        print("{0.name} = {0.health} HP".format(enemy))
        print("Your health = {0.health} HP".format(player))
        # Combat loop
        while player.health > 0 and enemy.health > 0:
            player.attack(enemy)
            print("The health of the {0.name} is now {0.health}.".format(enemy))
            if enemy.health <= 0:
                break
            enemy.attack(player)
            print("Your health is now {0.health}.".format(player))
        # Display outcome
        if player.health > 0:
            print("You killed the {0.name}.".format(enemy))
            level_module.add_xp(xp)
            randomizer()
        elif enemy.health > 0:
            print("The {0.name} killed you.".format(enemy))
            continue_ = input('Continue? (y/n)')
            if continue_ == 'y':
                randomizer()
            elif continue_ == 'n':
                sys.exit()
            while continue_ not in ['y','n']:
                print('Please enter a valid answer.')
                continue_ = input('Continue? (y/n)')
                

    

    if __name__ == '__main__':
        enemies = [Enemy("Goblin", 1, 5, 10), Enemy("Skeleton", 3, 7, 10),
                   Enemy("Spider", 5, 8, 20), Enemy ("Orc", 6, 9, 20), 
                   Enemy ("Dwarf", 7, 9, 20), Enemy("Elf", 9, 11, 30), 
                   Enemy ("Demon", 11, 12, 40), Enemy("Goblin King", 20, 15, 50), 
                   Enemy("Skeleton Lord", 25, 17, 50), Enemy("Giant Spider", 27, 19, 60),
                   Enemy("Orc Leader", 31, 20, 60), Enemy("Dwarf King", 32, 21, 60),
                   Enemy("Grand Elf", 34, 22, 70), Enemy("Demon Lord", 36, 24, 100), 
                   Enemy("Soldier", 5, 8, 10), Enemy("Super Soldier", 10, 14, 25), 
                   Enemy("Healer", 3, 27, 20), Enemy("Wizard", 64, 12, 50), 
                   Enemy("Fairy", 35, 3, 50), Enemy("Fairy God", 65, 18, 100)]
        battle(Player(), random.choice(enemies))

def randomizer():
    number = random.randint(1, 100)
    while number > 45:
        number = random.randint(1, 100)
    if number < 45:
        main()

