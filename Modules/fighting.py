import random
import time
import sys
import level_module 	
import weapons
import pickle
import decimal
import magic
import inventory
global weapon_list
global magic_list
global xp
global inventory_list
inventory_load = pickle.load(open('inventory.txt','rb'))
inventory_list = inventory_load
xp = level_module.xp
weapon_list = pickle.load(open("weapons.txt", "rb"))
weapon_list_lower = pickle.load(open("weapons_lower.txt", "rb"))
magic_list = pickle.load(open("magic_list.txt", "rb"))

def main():
    class Character:

        def __init__(self, health):
            self.health = health
        def attack(self, other):     
            raise NotImplementedError

    class Player(Character):

        def __init__(self, health=100):
            self.shield = 'False'
            super().__init__(health)

        def attack(self, other):
            answer = input("What would you like to do? (1. Fight, 2. Magic or 3. Item) ")
            if answer.lower() in ['1','2','3']:
                if answer.lower() == '1':
                    for i in weapon_list:
                        print (i)
                    weapon_choice = input('Which weapon would you like to use? ')
                    if weapon_choice == '1':
                        sword = int(decimal.Decimal(weapons.sword))
                        other.health -= (sword * int(decimal.Decimal(random.uniform(1, 1.4))))
                    elif weapon_choice == '2':
                        super_sword = (int(decimal.Decimal(weapons.super_sword)))
                        other.health -= (super_sword * int(decimal.Decimal(random.uniform(1, 1.4))))
                    elif weapon_choice == '3':
                        hyper_sword = (int(decimal.Decimal(weapons.hyper_sword)))
                        other.health -= (hyper_sword * int(decimal.Decimal(random.uniform(1, 1.4))))
                    elif weapon_choice == '4':
                        mega_blade = (int(decimal.Decimal(weapons.mega_blade)))
                        other.health -= (mega_blade* int(decimal.Decimal(random.uniform(1, 1.4))))
                    elif weapon_choice == '5':
                        bow = (int(decimal.Decimal(weapons.bow)))
                        other.health -= (bow * int(decimal.Decimal(random.uniform(1, 1.4))))
                    elif weapon_choice == '6':
                        super_bow = (int(decimal.Decimal(weapons.super_bow)))
                        other.health -= (super_bow * int(decimal.Decimal(random.uniform(1, 1.4))))
                    elif weapon_choice == '7':
                        hyper_bow = (int(decimal.Decimal(weapons.hyper_bow)))
                        other.health -= (hyper_bow * int(decimal.Decimal(random.uniform(1, 1.4))))
                    elif weapon_choice == '8':
                        mega_bow = (int(decimal.Decimal(weapons.mega_bow)))
                        other.health -= (mega_bow * int(decimal.Decimal(random.uniform(1, 1.4))))
                        
                elif answer.lower() == '2':
                    for i in magic_list:
                        print(i)					
                    magic_choice = input('What would you like to cast? ')
                    if magic_choice.lower() == '1':
                        fireball = int(decimal.Decimal(magic.fireball))
                        other.health -= (fireball * int(decimal.Decimal(random.uniform(1, 1.4))))
                    elif magic_choice.lower() == '2':
                        heal = int(decimal.Decimal(magic.heal))
                        self.health += (heal * int(decimal.Decimal(random.uniform(1, 1.4))))
                    elif magic_choice.lower() == '3':
                        tornado = int(decimal.Decimal(magic.tornado))
                        other.health -= (tornado * int(decimal.Decimal(random.uniform(1, 1.4))))
                    else:
                        print('Please choose a valid spell to cast.')
                        
            while answer.lower() not in ['1','2','3']:
                print('Please enter a valid option.')
                answer = input("What would you like to do? (1. Fight, 2. Magic or 3. Item) ")
                

    class Enemy(Character):


        def __init__(self, name, strength, defense, health):
            super().__init__(health)
            self.name = name
            self.strength = strength
            self.defense = defense

        def attack(self, other):
            print("The {0.name} attacks...".format(self))
            shield_block()
            armour_block()

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
            drop()
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

def drop():
    item_list = ['Paper','Cardboard']
    item_number = random.randint(0,1)
    dropped_item = item_list[item_number]
    print('You picked up a '+dropped_item.lower()+'!')
    put_in_inventory = input('Place in inventory? (1. Yes or 2. No) ')
    if put_in_inventory == '1':
        inventory_list.append(dropped_item)
        inventory_save = open('inventory.txt','wb')
        pickle.dump(inventory_list, inventory_save)
        inventory_save.close()
        
        
def shield_block():
    if self.shield == 'True':
        block = random.randint(1,10)
        if block < 4:
            print('You blocked the attack!')
            damage = 0
            shield_type_duration -= 2
        elif block > 4 and block < 9:
            print('You did not block the attack!')
            self.health -= 
            
