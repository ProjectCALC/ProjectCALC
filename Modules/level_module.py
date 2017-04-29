import random
global level
level = 1
global xp
xp = 0

def main():
    while xp != 100:
        break
    while xp == 100 or xp > 100:
        level +=1
        print('Congrats! You''ve leveled up to level '+level+'!')

def add_xp(xp):
    xp_add = random.randint(1,20)
    xp = xp+xp_add
    main()
