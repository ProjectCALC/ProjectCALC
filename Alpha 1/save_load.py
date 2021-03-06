import pickle
import inventory
import sys

def load():
    savefile = pickle.load(open('savefile.pkl','rb'))
    first_name = savefile[0]
    last_name = savefile[1]
    gender = savefile[2]
    age = savefile[3]
    inventory = savefile[4]
    magic = savefile[5]
    weapons = savefile[6]
    level = savefile[7]
    old_level = savefile[8]    
    magic_level = savefile[9]
    xp = savefile[10]
    wcounter = savefile[11]
    wvar = savefile[12]
    mcounter = savefile[13]
    health = savefile[14]
    print('Your character: ')
    print(''+first_name+' '+last_name+'')
    print('Gender: '+gender+'')
    print('Age: '+age+'')
    print('Level: '+str(level)+'')
    print('Magic Level: '+str(magic_level)+'')
    answer = input('Load this save? (1.Yes or 2.No) ')
    if answer == '1':
        print('Game loaded.')
    elif answer == '2':
        print('See you later.')
        sys.exit()
    while answer not in ['1','2']:
        print('Please enter a valid answer.')
        answer = input('Load this save? (1.Yes or 2.No) ')
    

def save():
    temp_ = pickle.load(open('temp.pkl', 'rb'))
    import level_module
    import magic
    import weapons
    savefile_import = open('savefile.pkl','rb')
    savefile_r = pickle.load(savefile_import)
    savefile_w = open('savefile.pkl','wb')
    first_name = savefile_r[0]
    last_name = savefile_r[1]
    gender = savefile_r[2]
    age = savefile_r[3]
    inventory_ = inventory.inventory_list
    magic_ = magic.magic_list
    weapons_ = weapons.weapon_list
    level_ = temp_[7]
    old_level_ = temp_[8]
    magic_level_ = temp_[9]
    xp_ = temp_[10]
    wcounter = temp_[11]
    wvar = temp_[12]
    mcounter = temp_[13]
    health = temp_[14]
    save_list = [first_name, last_name, gender, age, inventory_, magic_, weapons_, level_, old_level_, magic_level_, xp_, wcounter, wvar, mcounter, health]
    pickle.dump(save_list, savefile_w)
    savefile_w.close()
    savefile_import.close()
    print('Game saved.')

def temp(level, old_level, magic_level, xp, wvar, wcounter, mcounter, health):
    temp_ = pickle.load(open('temp.pkl','rb'))
    tempw = open('temp.pkl','wb')
    temp = temp_
    del temp[7]
    del temp[7]
    del temp[7]
    del temp[7]
    del temp[7]
    del temp[7]
    del temp[7]
    del temp[7]
    temp_list = [int(level), int(old_level), int(magic_level), int(xp), int(wvar), int(wcounter), int(mcounter), int(health)]
    temp.extend(temp_list)
    pickle.dump(temp, tempw)
    tempw.close()







    
