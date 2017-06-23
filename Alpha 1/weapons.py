import level_module
import pickle
import random

weapon_list = ['Sword','Bow']
unlockable_weapons = ['Super Sword','Super Bow','Hyper Sword','Hyper Bow','Mega Blade','Mega Bow']
if level_module.level == 48 or int(level_module.level) > 48:
    pass
elif level_module.level == int(level_module.wvar) + 8:
    wvar +=8
    level_module.wcounter +=1
    if int(level_module.wcounter) in [1,3,5]:
        del weapon_list[0]
        weapon_list.insert(0, unlockable_weapons[wcounter-1])
        print('Congrats! You''ve unlocked the '+weapon_list[0]+'!')
    elif level_module.wcounter in [2,4,8]:
        del weapon_list[1]
        weapon_list.insert(1, unlockable_weapons[wcounter-1])
        print('Congrats! You''ve unlocked the '+weapon_list[1]+'!')
        


sword = 5 + 0.5 * int(level_module.level)
super_sword = 5 + 1 * int(level_module.level)
hyper_sword = 5 + 1.5 * int(level_module.level)
mega_blade = 5 + 2 * int(level_module.level)
bow_random = random.randint(5,8) * int(level_module.level)
bow = random.randint(5,8) + 0.5 * int(level_module.level)
super_bow = random.randint(5,8) + 1 * int(level_module.level)
hyper_bow = random.randint(5,8) + 1,5 * int(level_module.level)
mega_bow = random.randint(5,8) + 2 * int(level_module.level)
    
    
    
    

