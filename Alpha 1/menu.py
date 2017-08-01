import init
init.main()
import time
import save_load
import ingame_menu
import new_game
import sys
import os
from pathlib import Path


def main():
    print('Welcome to ProjectCALC')
    print('Version: Alpha 1')
    answer = input('What would you like to do? (1.New Game, 2.Load Game or 3.Exit) ')
    if answer == '1':
        my_file = Path("savefile.pkl")
        if my_file.is_file():
            deleteSave = input('You already have a safefile. Are you sure you want to delete it and make a new one? (1.Yes or 2.No) ')
            if deleteSave == '1':
                os.remove("savefile.pkl")
                os.remove("inventory.pkl")
                print("Savefile deleted!")
                time.sleep(2)
                new_game.main()
                save_load.save()
                ingame_menu.main()
            elif deleteSave == '2':
                print("Savefile not deleted.")
                main()


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
