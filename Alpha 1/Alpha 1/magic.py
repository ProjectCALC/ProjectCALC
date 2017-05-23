import random
import level_module
import pickle

#list of spells that you can cast
magic_list = ['Fireball','Heal','Tornado']

#adds a spell to magic_list for every magic level-up
if level_module.magic_level == 2:
  magic_list.append('Summon')
elif level_module.magic_level == 3: 
  magic_list.append('Light Sword')
elif level_module.magic_level == 4: 
  magic_list.append('Light Bow')
elif level_module.magic_level == 5:
  magic_list.append('Dark Sword')
elif level_module.magic_level == 6:
  magic_list.append('Dark Bow')
elif level_module.magic_level == 7:
  magic_list.append('Fairy Call')
elif level_module.magic_level == 8:
  magic_list.append('Demon Call')
elif level_module.magic_level == 9:
  magic_list.append('Ultra Black Hole')


#damage
fireball = 10 * level_module.magic_level * random.uniform(1,1.4)
tornado = 12 * level_module.magic_level * random.uniform(1,1.4)
light_sword = 10 * level_module.magic_level * random.uniform(1,1.4)
light_bow = 10 * level_module.magic_level * random.uniform(1,1.4)
dark_sword = 10 * level_module.magic_level * random.uniform(1,1.4)
dark_bow = 10 * level_module.magic_level * random.uniform(1,1.4)
ultra_black_hole = 10 * level_module.magic_level * random.uniform(1,1.4)
heal = 6 * level_module.magic_level * random.uniform(1,1.4)

def display():
  print('Your spells: ')
  for i in magic_list:
    print(i)
  print('')
  print('')
  print('')
  
