import pickle
from pathlib import Path

def main():
    my_file = Path("savefile.pkl")
    if my_file.is_file():
        temp = open('temp.pkl','wb')
        savefile = pickle.load(open('savefile.pkl','rb'))
        init_list = ['fn','ln','gen','age','inv','mag','wea',savefile[7], savefile[8], savefile[9], savefile[10],savefile[11],savefile[12],savefile[13],savefile[14]]
        pickle.dump(init_list, temp)
        temp.close()
        magic_list = open('magic_list.pkl','wb')
        magic_add = ['Fireball','Heal','Tornado']
        pickle.dump(magic_add, magic_list)
        magic_list.close()

    else:
        temp = open('temp.pkl', 'wb')
        init_list = ['fn', 'ln', 'gen', 'age', 'inv', 'mag', 'wea','1','0','1','0','0', '0', '0','20']
        pickle.dump(init_list, temp)
        temp.close()
        magic_list = open('magic_list.pkl','wb')
        magic_add = ['Fireball','Heal','Tornado']
        pickle.dump(magic_add, magic_list)
        magic_list.close()


