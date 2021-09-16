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
        parameters = (input('Enter base and height: '))
        parameters_list = parameters.split()
        map_parameters = map(int, parameters_list) 
        parameters_intager = list(map_parameters)    
        if len(parameters_intager) == 2:
            area =  0.5*parameters_intager[0]*parameters_intager[1]
            print ('Area is:', area)
            print()
            print()
        else:
            print()
            print()
            print ('WRONG NUMBERS OF PARAMETERTS')
            print()
            print()
    elif option == 2:
        parameters = input('Enter 2 sides and angle(degrees) between them: ')
        parameters_list = parameters.split()
        map_parameters = map(int, parameters_list) 
        parameters_intager = list(map_parameters)
        if len(parameters_intager) == 3:
            area =  0.5*parameters_intager[0]*parameters_intager[1]*math.sin(math.radians(parameters_intager[2]))
            print ('Area is:', area)
            print()
            print()
        else:
            print()
            print()
            print ('WRONG NUMBERS OF PARAMETERTS')
            print()
            print()
    elif option == 3:
        print ('Goodbye!')
        exit()
    else:
        print('Please enter a number between 1 and 3.')
