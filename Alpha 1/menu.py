import pickle
import save_load
import ingame_menu
import new_game
import sys
import init


def main():
    print('Welcome to ProjectCALC')
    print('Version: Alpha 1')
    answer = input('What would you like to do? (1.New Game, 2.Load Game or 3.Exit) ')
    if answer == '1':
            new_game.main()
            save_load.save()
            ingame_menu.main()
    elif answer == '2':
        try:
            save_load.load()
            ingame_menu.main()
            print('')
            print('')
            print('')
        except FileNotFoundError:
            print('You do not have a savefile. Please create one from the menu.')
            print('')
            print('')
            print('')
            main()
    elif answer == '3':
        sys.exit()
    while answer not in ['1','2','3']:
        print('Please enter a valid answer')
        answer = input('What would you like to do? (1.New Game, 2.Load Game or 3.Exit) ')
main()
