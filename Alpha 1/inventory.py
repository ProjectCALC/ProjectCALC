import pickle

global inventory_list
inventory_list = open('inventory.pkl','wb')
pickle.dump(['Inventory: '], inventory_list)
inventory_list.close()
inventory_list = pickle.load(open('inventory.pkl','rb'))

def display():
    for i in inventory_list:
        print (i)
    print('')
    print('')
    print('')
    
    
