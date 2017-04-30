import level_module
import pickle
import random

weapon_names = ['Sword','Super Sword','Hyper Sword','Mega Blade','Bow','Super Bow','Hyper Bow','Mega Bow']
weapon_names_lower = ['sword','super sword','hyper sword','mega blade','bow','super bow','hyper bow','mega bow']
pickle.dump(weapon_names, open("weapons.txt", "wb"))
pickle.dump(weapon_names_lower, open("weapons_lower.txt", "wb"))


sword = 5 + 0.5 * level_module.level
super_sword = 5 + 1 * level_module.level
hyper_sword = 5 + 1.5 * level_module.level
mega_blade = 5 + 2 * level_module.level
bow_random = random.randint(5,8) * level_module.level
bow = random.randint(5,8) + 0.5 * level_module.level
super_bow = random.randint(5,8) + 1 * level_module.level
hyper_bow = random.randint(5,8) + 1,5 * level_module.level
mega_bow = random.randint(5,8) + 2 * level_module.level
    
    
    
    

