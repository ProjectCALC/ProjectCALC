import pickle

def main():
    temp = open('temp.pkl','wb')
    init_list = ['fn','ln','gen','age','inv','mag','wea','1','0','1','0','0','0','0']
    pickle.dump(init_list, temp)
    temp.close()


