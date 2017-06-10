import level_module
import pickle
import random

weapon_list = ['Sword','Super Sword','Hyper Sword','Mega Blade','Bow','Super Bow','Hyper Bow','Mega Bow']


sword = 5 + 0.5 * int(level_module.level)
super_sword = 5 + 1 * int(level_module.level)
hyper_sword = 5 + 1.5 * int(level_module.level)
mega_blade = 5 + 2 * int(level_module.level)
bow_random = random.randint(5,8) * int(level_module.level)
bow = random.randint(5,8) + 0.5 * int(level_module.level)
super_bow = random.randint(5,8) + 1 * int(level_module.level)
hyper_bow = random.randint(5,8) + 1,5 * int(level_module.level)
mega_bow = random.randint(5,8) + 2 * int(level_module.level)
    
    
    
    

