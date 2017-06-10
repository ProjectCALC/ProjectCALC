import random
import pickle

tempr = pickle.load(open('temp.pkl','rb'))
xp = tempr[0]
level = tempr[1]
old_level = tempr[2]
magic_level = tempr[3]


def main(xp, level, old_level, magic_level, savefile):
    tempr = pickle.load(open('temp.pkl','rb'))
    xp = tempr[0]
    level = tempr[1]
    old_level = tempr[2]
    magic_level = tempr[3]
    if level == 100:
        pass
    else:
        add = random.randint(1, 20)
        intxp = int(xp)
        xp = intxp + add
        if intxp < 100:
            pass
        elif intxp == 100 or intxp > 100:
            if level > 91:
                pass
            elif level < 91:
                xp = 0
                level += 1
                print('Congrats! You''ve leveled up to level ' + level + '!')
                if level == old_level+9:
                    magic_level += 1
                    old_level += 9
                    print('Good job! Your magic level is now ' + magic_level + '!')
            while level != old_level + 9:
                pass
        temp = open('temp.pkl','wb')
        temp_list = [xp, level, old_level, magic_level]
        pickle.dump(temp_list, temp)
        temp.close()
