import character_creation as cc
import ingame_menu
import save_load

def main():
    print('What you can do in this version: ')
    print('Fight enemies using weapons and magic.')
    print('Level up to unlock new weapons, spells and boost stats.')
    print('Finish the game by beating Francis Faygo in a boss battle when your each level 100.')
    print('But before you can play, you need to make a character.')
    cc.fn()
    cc.ln()
    cc.gender_func()
    cc.age_func()
    cc.show_char()
    cc.confirm()
    answer = input('OK! '+cc.first_name+', are you ready to start your journey? (1.Yes or 2.No) ')
    if answer == '1':
        save_load.save()
        ingame_menu.main()
    elif answer =='2':
        print('leave then you idiot')
    while answer not in ['1','2']:
        print('Please enter a valid answer.')
