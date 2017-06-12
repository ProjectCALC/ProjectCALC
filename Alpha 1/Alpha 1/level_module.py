import random
import pickle

tempr = pickle.load(open('temp.pkl','rb'))
xp = tempr[0]
level = tempr[1]
old_level = tempr[2]
magic_level = tempr[3]


def main(xp, level, old_level, magic_level, savefile):
    tempr = pickle.load(open('temp.pkl','rb'))
    newxp = xp
    newlevel = level   
    newold_level = old_level
    newmagic_level = magic_level
    if level == 100:
        pass
    else:
        add = random.randint(1, 20)
        intxp = int(xp)
        newxp = intxp + add
        if intxp < 100:
            pass
        elif intxp == 100 or intxp > 100:
            if newlevel > 91:
                pass
            elif newlevel < 91:
                newxp = 0
                newlevel += 1
                print('Congrats! You''ve leveled up to level ' + newlevel + '!')
                if newlevel == newold_level+9:
                    newmagic_level += 1
                    newold_level += 9
                    print('Good job! Your magic level is now ' + magic_level + '!')
            while newlevel != newold_level + 9:
                pass
        temp = open('temp.pkl','wb')
        temp_list = [newxp, newlevel, newold_level, newmagic_level]
        pickle.dump(temp_list, temp)
        temp.close()
