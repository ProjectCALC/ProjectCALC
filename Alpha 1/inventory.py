import pickle

global inventory_list
inventory_list = open('inventory.pkl','wb')
pickle.dump('default', inventory_list)
inventory_list.close()
inventory_list = pickle.load(open('inventory.pkl','rb'))


def display():
    print('Inventory: ')
    for i in inventory_list:
        print (i)
    print('')
    print('')
    print('')
    
    
