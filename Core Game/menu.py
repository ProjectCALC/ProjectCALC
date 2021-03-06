import easygui
import sys
import time
import character_creation as cc
import character_movement


def game():
    image = "Image_P.gif"
    menu = easygui.buttonbox('Welcome to CalcRPG(ProjectCALC)',image=image,
                             choices = ['New Game','Load Game','Exit'] )

    if menu == 'New Game':
        print('Welcome to the multiverse that is CalcRPG.')
        time.sleep(1)
        print('You will meet a variety of different creatures, from humans to gods, from elves to dwarves, and many more interesting species.')
        time.sleep(3)
        print('To begin playing, please make your character.')
        time.sleep(1)
        cc.fn()
        cc.ln()
        cc.gender_func()
        cc.age_func()
        cc.class_func()
        cc.show_char()
        cc.confirm()
        print('Great! Now, it''s time for you to go. But be careful! Creatures roam the night, as well as the day, so be weary of where you''re going.')
        character_movement.main()
        sys.exit()
    elif menu == 'Load Game':
        print('Loading saved game...')
        time.sleep(2)
        cc.load()
        time.sleep(1)
        load_continue = input('Continue?(Yes or No) ')
        if load_continue == 'No' or load_continue == 'no' or load_continue == 'n':
            game()
        elif load_continue == 'Yes' or load_continue == 'yes' or load_continue == 'y':
            character_movement.main()
            sys.exit()        
    else:
        sys.exit()
game()
