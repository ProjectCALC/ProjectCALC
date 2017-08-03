import random
import pickle
temp = pickle.load(open('temp.pkl','rb'))

mcounter = temp[13]

unlockable_spells = ['Light Sword','Light Bow','Dark Sword','Dark Bow','Ultra Black Hole']

#list of spells that you can cast
global magic_list
magic_list = pickle.load(open('magic_list.pkl','rb'))
magic_list_w = open('magic_list.pkl','wb')

#adds a spell to magic_list for every magic level-up
def main(mcounter, magic_level):
    if magic_level < 2:
        pass
    elif magic_level == 2 or magic_level > 2:
        if magic_level == 2:
          magic_list.append('Light Sword')
          mcounter += 1
        elif magic_level == 3:
          magic_list.append('Light Bow')
          mcounter += 1
        elif magic_level == 4:
          magic_list.append('Dark Sword')
          mcounter += 1
        elif magic_level == 5:
          magic_list.append('Dark Bow')
          mcounter += 1
        elif magic_level == 6:
          magic_list.append('Ultra Black Hole')
          mcounter += 1
        print('Congrats! You''ve just unlocked the ' + unlockable_spells[int(mcounter) - 1] + ' spell!')
        pickle.dump(magic_list, magic_list_w)
        magic_list_w.close()

#damage
fireball = 10 * int(temp[9]) * random.uniform(1,1.4)
tornado = 12 * int(temp[9]) * random.uniform(1,1.4)
light_sword = 10 * int(temp[9]) * random.uniform(1,1.4)
light_bow = 10 * int(temp[9]) * random.uniform(1,1.4)
dark_sword = 10 * int(temp[9]) * random.uniform(1,1.4)
dark_bow = 10 * int(temp[9]) * random.uniform(1,1.4)
ultra_black_hole = 10 * int(temp[9]) * random.uniform(1,1.4)
heal = 6 * int(int(temp[9])) * random.uniform(1,1.4)

def display():
    magic_list = pickle.load(open('magic_list.pkl','rb'))
    print('Your spells: ')
    for i in magic_list:
        print(i)
    print('')
    print('')
    print('')
  
