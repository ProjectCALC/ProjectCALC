import random

xp = 0
level = 1
old_level = 0
magic_level = 1


def main(xp, level, old_level, magic_level):
    if level == 100:
        pass
    else:
        add = random.randint(1, 20)
        xp += add
        if xp < 100:
            pass
        elif xp == 100 or xp > 100:
            if level > 91:
                print('')
            elif level == old_level + 9:
                level += 1
                print('Congrats! You''ve leveled up to level ' + level + '!')
                magic_level += 1
                old_level += 9
                print('Good job! Your magic level is now ' + magic_level + '!')
            while level != old_level + 9:
                print('')
                pass
