import random
import pickle
global xp
global level
global old_level
global skill_t
global magic_level
xp = 100
level = 1
old_level = 0
skill_t = 0
magic_level = 1

def main(xp):
    add = random.randint(1,20)
    xp += add
    if xp != 100:
        pass
    elif xp == 100 or xp > 100:
            if level > 91:
                print('')
            elif level == old_level + 9:
                level +=1
                print('Congrats! You''ve leveled up to level '+level+'!')
                magic_level +=1
                skill_t +=1
                old_level +=9
                print('Good job! Your magic level is now '+magic_level+'!')
            while level != old_level + 9:
                print('')
