import pickle
import sys


def fn():
        global first_name
        first_name = input('First Name: ')
        while first_name == '':
            print('Please enter a first name.')
            first_name = input('First Name: ')
    
def ln():
        global last_name
        last_name = input('Last Name: ')
        while last_name == '':
            print('Please enter a last name.')
            last_name = input('Last Name: ')

def gender_func():
                        global gender
                        gender = input('Gender: (M or F): ')
                        gender_list = ['M','F','m','f']
                        while gender not in gender_list:
                            print('Please enter a valid gender.')
                            gender = input('Gender: (M or F): ')
                        else:
                                if gender == gender_list[2]:
                                        gender = 'M'
                                elif gender == gender_list[3]:
                                        gender = 'F'

def age_func():
                                try:
                                        global age
                                        age = input('Age: (19 to 40): ')
                                        num_age = int(age)
                                        while num_age < 19 or num_age > 40 or age == '':
                                                print('Please enter an age from 19 to 40.')
                                                age = input('Age: (19 to 40): ')
                                except ValueError:
                                        print('Please enter a number.')
                                        age_func()
                                        

##def m_bday():
##        
##                                            global month_bday
##                                            month_bday = input('Month of Birth: (01 to 12) ')
##                                            num_month_bday = int(month_bday)
##                                            long_months = ['01','03','05','07','08','10','12']
##                                            short_months = ['04','06','09','11']
##                                            febuary = '02'
##                                            while num_month_bday > 1 or num_month_bday < 12:
##                                                    if month_bday in long_months:
##                                                            global limit
##                                                            limit = '31'
##                                                    elif month_bday in short_months:
##                                                            limit = '30'
##                                                    elif month_bday == febuary:
##                                                            limit ='28'    
##                                            num_month_bday = int(month_bday)
##                                            while num_month_bday < 1 or num_month_bday > 12:
##                                                print('Please enter a valid month.')
##                                                month_bday = input('Month of Birth: (1 to 12) ')
##                                                num_month_bday = int(month_bday)
##
##def d_bday():
##                                                    global day_bday
##                                                    day_bday = input('Day of Birth: (1 to '+limit+') ')
##                                                    num_day_bday = int(day_bday)
##                                                    while  num_day_bday < 1 or num_day_bday > int(limit):
##                                                        print('Please enter a valid day of birth.')
##                                                        day_bday = input('Day of Birth: (1 to '+limit+') ')
##                                                        num_day_bday = int(day_bday)
##
def class_func():
                                                            global char_class
                                                            char_class_list = ['Fighter', 'Wizard','Rogue', 'Explorer', 'Scholar']
                                                            char_class = input('Class: (Fighter, Wizard, Rogue, Explorer, Scholar) ')
                                                            while char_class not in char_class_list:
                                                                print('Please enter a valid class.')
                                                                char_class = input('Class: (Fighter, Wizard, Rogue, Explorer, Scholar) ')
def confirm():
                                                                            print('')
                                                                            print('Your character: ')
                                                                            print('Name: '+first_name+' '+last_name+'')                                                             
                                                                            print('Gender: '+gender+'')
                                                                            print('Age: '+age+'')
                                                                            ##print('Birthday: '+month_bday+'/'+day_bday+'')                                                                            print('')


                                                                            confirm_character_creation = input('Is this character ok? (1.Yes or 2. No) ')
                                                                            if confirm_character_creation == '2':
                                                                                    wrong = input('What''s wrong? (1.First Name, 2.Last Name, 3.Gender, 4.Age, 5.Nothing) ')
                                                                                    if wrong == '1':
                                                                                        fn()
                                                                                        confirm()
                                                                                    elif wrong == '2':
                                                                                        ln()
                                                                                        confirm()
                                                                                    elif  wrong == '3':
                                                                                        gender_func()
                                                                                        confirm()
                                                                                    elif wrong == '4':
                                                                                        age_func()
                                                                                        confirm()
                                                                                    elif wrong == '5':
                                                                                        confirm()
                                                                                    while wrong not in ['1','2','3','4','5']:
                                                                                        print('Please enter a valid answer.')
                                                                

                                                                            if confirm_character_creation == '1':
                                                                                        character = [first_name, last_name, gender, age]
                                                                                        save = open('savefile.pkl','wb')
                                                                                        pickle.dump(character, save)
                                                                                        save.close()
                                                                                        




                    
                    




                        
            

    
