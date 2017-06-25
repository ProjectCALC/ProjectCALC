import random
import level_module
import pickle

#list of spells that you can cast
magic_list = ['Fireball','Heal','Tornado']

#adds a spell to magic_list for every magic level-up
if int(level_module.magic_level) == 2:
  magic_list.append('Light Sword')
  counter += 1
elif int(level_module.magic_level) == 3: 
  magic_list.append('Light Bow')
elif int(level_module.magic_level) == 4: 
  magic_list.append('Dark Sword')
elif int(level_module.magic_level) == 5:
  magic_list.append('Dark Bow')
elif int(level_module.magic_level) == 6:
  magic_list.append('Ultra Black Hole')


#damage
fireball = 10 * int(level_module.magic_level) * random.uniform(1,1.4)
tornado = 12 * int(level_module.magic_level) * random.uniform(1,1.4)
light_sword = 10 * int(level_module.magic_level) * random.uniform(1,1.4)
light_bow = 10 * int(level_module.magic_level) * random.uniform(1,1.4)
dark_sword = 10 * int(level_module.magic_level) * random.uniform(1,1.4)
dark_bow = 10 * int(level_module.magic_level) * random.uniform(1,1.4)
ultra_black_hole = 10 * int(level_module.magic_level) * random.uniform(1,1.4)
heal = 6 * int(int(level_module.magic_level)) * random.uniform(1,1.4)

def display():
  print('Your spells: ')
  for i in magic_list:
    print(i)
  print('')
  print('')
  print('')
  
