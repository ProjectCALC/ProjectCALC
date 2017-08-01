import pickle
from pathlib import Path

def main():
    my_file = Path("savefile.pkl")
    if my_file.is_file():
        temp = open('temp.pkl','wb')
        savefile = pickle.load(open('savefile.pkl','rb'))
        init_list = ['fn','ln','gen','age','inv','mag','wea',savefile[7],savefile[8],savefile[9],savefile[10],'0','0','0']
        pickle.dump(init_list, temp)
        temp.close()
    else:
        temp = open('temp.pkl', 'wb')
        init_list = ['fn', 'ln', 'gen', 'age', 'inv', 'mag', 'wea','1','0','1','0','0', '0', '0']
        pickle.dump(init_list, temp)
        temp.close()



