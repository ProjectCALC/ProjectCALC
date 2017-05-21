import fighting
import inventory
import save_load
import magic
import sys

def main():
    answer = input('What would you like to do? (1.Go to next fight, 2.Inventory, 3.Spells, 4.Save or 5.Exit) ')
    if answer == '1':
        fighting.main()
    elif answer == '2':
        inventory.display()
        main()
    elif answer == '3':
        magic.display()
        main()
    elif answer == '4':
        save_load.save()
        main()        
    elif answer == '5':
        sys.exit()
    while answer not in ['1','2','3','4','5']:
        print('Please enter a valid answer.')

    
