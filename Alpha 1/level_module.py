import random
import pickle
import save_load
import time



temp = pickle.load(open('temp.pkl','rb'))
level = temp[7]
old_level = temp[8]
magic_level = temp[9]
xp = temp[10]
wvar = temp[11]
wcounter = temp[12]
mcounter = temp[13]


def main():
    temp = pickle.load(open('temp.pkl', 'rb'))
    level = temp[7]
    old_level = temp[8]
    magic_level = temp[9]
    xp = temp[10]
    wvar = temp[11]
    wcounter = temp[12]
    mcounter = temp[13]
    if level == 100:
        pass
    else:
        add = random.randint(1, 20)
        intxp = int(xp)
        xp = intxp + add
        if xp < 100:
            pass
        elif xp == 100 or xp > 100:
            if level > 91:
                pass
            elif level < 91:
                xp = 0
                level += 1
                print("Congrats! You've leveled up to level " + str(level) + "!")
                time.sleep(2)
                if level == old_level + 9:
                    magic_level += 1
                    old_level += 9
                    print('Good job! Your magic level is now ' + str(magic_level) + '!')
                    time.sleep(2)
                elif level != old_level + 9:
                    pass
        level = level
        old_level = old_level
        magic_level = magic_level
        xp = xp
        wvar = wvar
        wcounter = wcounter
        mcounter = mcounter
        save_load.temp(level, old_level, magic_level, xp, wvar, wcounter, mcounter)
        


        
