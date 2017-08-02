import pickle
import random

# temp = open('temp.pkl','wb')
# pickle.dump('default', temp)
# temp.close()
temp = pickle.load(open('temp.pkl','rb'))

wcounter = temp[12]
wvar = temp[11]
weapon_list = ['Sword','Bow']
unlockable_weapons = ['Super Sword','Super Bow','Hyper Sword','Hyper Bow','Mega Blade','Mega Bow']
if temp[7] == 48 or int(temp[7]) > 48:
    pass
elif temp[7] == int(temp[11]) + 8:
    wvar +=8
    temp[12] +=1
    if int(temp[12]) in [1,3,5]:
        del weapon_list[0]
        weapon_list.insert(0, unlockable_weapons[wcounter-1])
        print('Congrats! You''ve unlocked the '+weapon_list[0]+'!')
    elif temp[12] in [2,4,8]:
        del weapon_list[1]
        weapon_list.insert(1, unlockable_weapons[wcounter-1])
        print('Congrats! You''ve unlocked the '+weapon_list[1]+'!')
        


sword = 5 + 0.5 * int(temp[7])
super_sword = 5 + 1 * int(temp[7])
hyper_sword = 5 + 1.5 * int(temp[7])
mega_blade = 5 + 2 * int(temp[7])
bow_random = random.randint(5,8) * int(temp[7])
bow = random.randint(5,8) + 0.5 * int(temp[7])
super_bow = random.randint(5,8) + 1 * int(temp[7])
hyper_bow = random.randint(5,8) + 1,5 * int(temp[7])
mega_bow = random.randint(5,8) + 2 * int(temp[7])
    
    
    
    

