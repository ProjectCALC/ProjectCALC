import random
import sys
import level_module
import weapons
import pickle
import decimal
import magic
import inventory
import save_load
import ingame_menu
import os

temp = pickle.load(open('temp.pkl', 'rb'))

global level
inventory_list = inventory.inventory_list
level = temp[7]
old_level = temp[8]
magic_level = temp[9]
xp = temp[10]
wcounter = temp[11]
wvar = temp[12]
mcounter = temp[13]
weapon_list = weapons.weapon_list
magic_list = magic.magic_list
savefile = pickle.load(open('savefile.pkl', 'rb'))
temp = pickle.load(open('temp.pkl', 'rb'))


def drop ():
    item_list = ['Paper', 'Cardboard']
    item_number = random.randint(0, 1)
    dropped_item = item_list[item_number]
    print('You picked up a ' + dropped_item.lower() + '!')
    put_in_inventory = input('Place in inventory? (1. Yes or 2. No) ')
    if put_in_inventory == '1':
        inventory_list.append(dropped_item)
        inventory_save = open('inventory.pkl', 'wb')
        pickle.dump(inventory_list, inventory_save)
        inventory_save.close()
    elif put_in_inventory == '2':
        print('Not placed in inventory.')


def main ():
    class Character:
        def __init__ (self, health):
            self.health = health

    class Player(Character):
        def __init__ (self, health=100):
            super().__init__(health)

        def attack (self, other):
            num = 0
            answer = input("What would you like to do? (1. Fight or 2. Magic) ")
            if answer.lower() in ['1', '2', '3']:
                if answer.lower() == '1':
                    for i in weapon_list:
                        num = num + 1
                        print('' + str(num) + '. ' + i + '')
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
                        other.health -= (mega_blade * int(decimal.Decimal(random.uniform(1, 1.4))))
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
                    m_num = 0
                    for i in magic_list:
                        m_num = m_num + 1
                        print('' + str(m_num) + '. ' + i + '')
                    magic_choice = input('What would you like to cast? ')
                    if magic_choice == '1':
                        fireball = int(decimal.Decimal(magic.fireball))
                        other.health -= (fireball * int(decimal.Decimal(random.uniform(1, 1.4))))
                    elif magic_choice == '2':
                        heal = int(decimal.Decimal(magic.heal))
                        self.health += (heal * int(decimal.Decimal(random.uniform(1, 1.4))))
                    elif magic_choice == '3':
                        tornado = int(decimal.Decimal(magic.tornado))
                        other.health -= (tornado * int(decimal.Decimal(random.uniform(1, 1.4))))
                    else:
                        print('Please choose a valid spell to cast.')

            while answer not in ['1', '2']:
                print('Please enter a valid option.')
                answer = input("What would you like to do? (1. Fight or 2. Magic) ")
    global Enemy
    class Enemy(Character):
        def __init__ (self, name, strength, defense, health):
            super().__init__(health)
            self.name = name
            self.strength = strength
            self.defense = defense

        def attack (self, other):
            print("The {0.name} attacks...".format(self))
            other.health -= int(self.strength * random.uniform(0.1, 1.4))

    def battle (player, enemy):
        print("An enemy {0.name} appears!".format(enemy))
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
            level_module.main()
            drop()
            enemyd()
        if player.health > 0 and level == 100:
            print('You killed Francis Faygo! You win!')
            print('Take a screenshot and send it to me at noah.hourdebaigt@gmail.com.')
            done = input('When you are ready to exit, type 1.')
            if done == '1':
                save_load.save()
                sys.exit()
            while done != '1':
                print('Ok then...')
                done = input('When you are ready to exit, type 1.')
        elif enemy.health > 0:
            print("The {0.name} killed you.".format(enemy))
            ingame_menu.main()

    def enemyd ():
        temp = pickle.load(open('temp.pkl', 'rb'))
        level = temp[7]
        global enemies
        enemies = [Enemy("Goblin", 1, 5, 10), Enemy("Skeleton", 3, 7, 10), ]
        enemies_w = open('enemies.pkl','wb')
        if int(level) == 2:
            if Enemy("Soldier", 5, 8, 10) not in enemies:
                enemies.extend((Enemy("Soldier", 5, 8, 10), Enemy("Orc", 6, 9, 20)))
                print(
                    'Enemies Soldier and Orc have been added to your enemy list. You can now encounter them in battle!')
        elif level in range(10, 14):
            if Enemy("Dwarf", 7, 9, 20) not in enemies:
                enemies.extend(Enemy("Dwarf", 7, 9, 20), Enemy("Spider", 5, 8, 20))
                print(
                    'Enemies Dwarf and Spider have been added to your enemy list. You can now encounter them in battle!')
        elif level in range(15, 19):
            if Enemy("Elf", 9, 11, 30) not in enemies:
                enemies.extend(Enemy("Elf", 9, 11, 30), Enemy("Super Soldier", 10, 14, 25))
                print(
                    'Enemies Elf and Super Soldier have been added to your enemy list. You can now encounter them in battle!')
        elif level in range(20, 24):
            if Enemy("Demon", 11, 12, 40) not in enemies:
                enemies.extend(Enemy("Demon", 11, 12, 40), Enemy("Fairy", 35, 3, 40))
                print(
                    'Enemies Demon and Fairy have been added to your enemy list. You can now encounter them in battle!')
        elif level in range(25, 29):
            if Enemy("Goblin King", 20, 15, 50) not in enemies:
                enemies.extend(Enemy("Goblin King", 20, 15, 50), Enemy("Skeleton Lord", 25, 17, 50))
                print(
                    'Enemies Goblin King and Skeleton Lord have been added to your enemy list. You can now encounter them in battle!')
        elif level in range(30, 34):
            if Enemy("Giant Spider", 27, 19, 60) not in enemies:
                enemies.extend(Enemy("Giant Spider", 27, 19, 60), Enemy("Orc Leader", 31, 20, 60))
                print(
                    'Enemies Giant Spider and Orc Leader have been added to your enemy list. You can now encounter them in battle!')
        elif level in range(35, 39):
            if Enemy("Dwarf King", 32, 21, 60) not in enemies:
                enemies.extend(Enemy("Dwarf King", 32, 21, 60), Enemy("Grand Elf", 34, 22, 70))
                print(
                    'Enemies Dwarf King and Grand Elf have been added to your enemy list. You can now encounter them in battle!')
        elif level in range(40, 44):
            if Enemy("Demon Lord", 36, 24, 100) not in enemies:
                enemies.extend(Enemy("Demon Lord", 36, 24, 100), Enemy("Fairy God", 65, 18, 100))
                print(
                    'Enemies Demon Lord and Fairy God have been added to your enemy list. You can now encounter them in battle!')
        elif level == 100:
            enemies = [Enemy('Francis Faygo, 100, 100, 100')]
        pickle.dump(enemies, enemies_w)
        enemies_w.close()

    enemyd()
    battle(Player(), random.choice(enemies))
