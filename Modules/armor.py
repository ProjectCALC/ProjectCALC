import level_module
import pickle
import random

armor_names = ['Wooden Shield','Iron Shield','Magical Shield','Helmet','Chestplate','Pants','Boots']
armor_names_lower = ['wooden shield','iron shield','magical shield','helmet','chestplate','pants','boots']
pickle.dump(armor_names, open("armors.txt", "wb"))
pickle.dump(armor_names_lower, open("armor_lower.txt", "wb"))

helmet = damage - 2 * level_module.level
chestplate = damage - 10 * level_module.level
pants = damage - 7 * level_module.level
boots = damage - 5 * level_module.level

if 'fullset' in open('inventory.txt').read():
    damage -20 * level_module.level
elif
    break

wooden_shield = damage - 1(random.uniform(0, damage))
iron_shield = damage - 1.5(random.uniform(0, damage))
magical_shield = damage - 2(random.uniform(0, damage))

# Need specification
wooden_shield_duration = 20
iron_shield_duration = 100
magical_shield_duration = 200
helmet_duration = 80
chestplate_duration = 120
pants_duration = 100
boots_duration = 90
