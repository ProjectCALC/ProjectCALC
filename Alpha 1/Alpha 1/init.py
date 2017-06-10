import pickle

savefile = open('savefile.pkl','wb')
save_list = ['first_name', 'last_name', 'gender', 'age', 'inventory', 'magic', 'weapons', '1', '99', '1', '0']
pickle.dump(save_list, savefile)
savefile.close()




