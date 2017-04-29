import level_module
import pickle

def main():


    weapon_names = ['Sword','Super Sword','Hyper Sword','Mega Blade','Bow','Super Bow','Hyper Bow','Mega Bow']
    pickle.dump( weapon_names, open( "weapons.txt", "wb" ) )

    sword = 5 + 0,5 * level_module.level
    super_sword = 5 + 1 * level_module.level
    hyper_sword = 5 + 1.5 * level_module.level
    mega_blade = 5 + 2 * level_module.level
    

