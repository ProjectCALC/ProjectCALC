import level_module
import pickle
import random

weapon_names = ['Sword','Super Sword','Hyper Sword','Mega Blade','Bow','Super Bow','Hyper Bow','Mega Bow']
pickle.dump( weapon_names, open( "weapons.txt", "wb" ) )
def main():
    sword = 5 + 0,5 * level_module.level
    super_sword = 5 + 1 * level_module.level
    hyper_sword = 5 + 1.5 * level_module.level
    mega_blade = 5 + 2 * level_module.level
    
    bow_random = random.randint(5,8)
    
    bow = bow_random + 0,5 * level_module.level
    super_bow = bow_random + 1 * level_module.level
    hyper_bow = bow_random + 1,5 * level_module.level
    mega_bow = bow_random + 2 * level_module.level
    
    
    
    
    

