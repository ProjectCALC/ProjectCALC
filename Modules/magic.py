import random
import level_module

#list of spells that you can cast
magic_list = ['Fireball','Heal','Tornado','Teleport']

#adds a spell to magic_list for every magic level-up
if magic_level == 2:
  magic_list.append('Summon')
elif magic_level == 3:  
  magic_list.append('Light Sword')
elif magic_level == 4:  
  magic_list.append('Light Bow')
elif magic_level == 5:   
  magic_list.append('Dark Sword')
elif magic_level == 6:
  magic_list.append('Dark Bow')
elif magic_level == 7:
  magic_list.append('Fairy Call')
elif magic_level == 8:
  magic_list.append('Demon Call')
elif magic_level == 9:
  magic_list.append('Ultra Black Hole')


#damage
fireball = 10(magic_level) * random.uniform(1,1)
tornado = 10(magic_level) * random.uniform(1,1.5)
light_sword = 10(magic_level) * random.uniform(1,2)
light_bow = 10(magic_level) * random.uniform(1,3)
dark_sword = 10(magic_level) * random.uniform(1,4.5)
dark_bow = 10(magic_level) * random.uniform(1,5)
ultra_black_hole = 10(magic_level) * random.uniform(1,10)
  
