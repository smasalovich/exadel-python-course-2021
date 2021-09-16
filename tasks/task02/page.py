import math
menu_options = {
    1: 'Calculate triangle area by base and height',
    2: 'Calculate triangle area by 2 sides and angle between them',
    3: 'Exit',


}

def print_menu():
    for key in menu_options.keys():
        key_point = str(key)+'.'
        print (key_point, menu_options[key])

while(True):
    print('menu:')
    print_menu()
    option = ''
    try:
        option = int(input('Enter menu item number: ')) 
    except:
        print('Wrong input. Please enter a number ...')

    if option == 1:
        try:
            parameters = (input('Enter base and height: '))
            parameters_list = parameters.split()
            if len(parameters_list) == 2:
                print (f'Area is:  {0.5*float(parameters_list[0])*float(parameters_list[1])} \n\n')
            else:
                print ('\n\n WRONG NUMBERS OF PARAMETERTS \n\n')
        except:
            print('\n\n Wrong input. \n\n ')
            continue
    elif option == 2:
        try:
            parameters = input('Enter 2 sides and angle(degrees) between them: ')
            parameters_list = parameters.split()
            if (len(parameters_list) == 3) and (0 < float(parameters_list[2]) < 180):
                area =  0.5*float(parameters_list[0])*float(parameters_list[1])*math.sin(math.radians(float(parameters_list[2])))
                print (f'Area is: {0.5*float(parameters_list[0])*float(parameters_list[1])*math.sin(math.radians(float(parameters_list[2])))}\n\n')
            else:
                print ('\n\nWRONG NUMBERS OF PARAMETERTS OR WRONG DEGREASE\n\n')
        except:
            print('\n\n Wrong input.\n\n ')
            continue
    elif option == 3:
        print ('Goodbye!')
        exit()
    else:
        print('Please enter a number between 1 and 3.')
