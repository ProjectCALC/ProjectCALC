import pickle

global inventory_list
inventory_list = pickle.load(open('inventory.pkl','rb'))


def display():
    print('Inventory: ')
    for i in inventory_list:
        print (i)
    print('')
    print('')
    print('')
    
    
