import inventory
import save_load
import sys
import pickle

def main():
    answer = input('What would you like to do? (1.Go to next fight, 2.Inventory, 3.Spells, 4.Show stats, 5.Save or 6.Exit) ')
    if answer == '1':
        import fighting
        fighting.main()
        main()
    elif answer == '2':
        inventory.display()
        main()
    elif answer == '3':
        import magic
        magic.display()
        main()
    elif answer == '4':
        temp = open('temp.pkl','rb')
        temp_load = pickle.load(temp)
        print('Your stats: ')
        print('XP: '+str(temp_load[0])+'')
        print('Level: '+str(temp_load[1])+'')
        print('Magic Level: '+str(temp_load[3])+'')
        print('')
        temp.close()
        main()
    elif answer == '5':
        save_load.save()
        main()
    elif answer == '6':
        sys.exit()
    while answer not in ['1','2','3','4','5']:
        print('Please enter a valid answer.')
        answer = input('What would you like to do? (1.Go to next fight, 2.Inventory, 3.Spells, 4.Save or 5.Exit) ')

    
