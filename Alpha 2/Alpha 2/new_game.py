import character_creation as cc
import time
import sys


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
    answer = input('OK! ' + cc.first_name + ', are you ready to start your journey? (1.Yes or 2.No) ')
    if answer == '1':
        print('Then here we go!')
        time.sleep(1)
    elif answer == '2':
        print('leave then you idiot')
        sys.exit()
    while answer not in ['1', '2']:
        print('Please enter a valid answer.')
        answer = input('OK! ' + cc.first_name + ', are you ready to start your journey? (1.Yes or 2.No) ')
