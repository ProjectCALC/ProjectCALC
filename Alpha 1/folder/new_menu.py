import new_game
import save_load
import sys
import ingame_menu

print('Welcome to ProjectCALC')
print('Version: Alpha 1')
answer = input('What would you like to do? (1.New Game, 2.Load Game or 3.Exit) ')
if answer == '1':
    new_game.main()
elif answer == '2':
    print('')
    print('')
    print('')
    print('')
    print('')
    save_load.load()
    ingame_menu.main()
elif answer == '3':
    sys.exit()
while answer not in ['1','2','3']:
    print('Please enter a valid answer')
    answer = input('What would you like to do? (1.New Game, 2.Load Game or 3.Exit) ')
