import pickle


# Just text
def clear_data():
    print('...')
    print('All data cleared.')
    print('Assingning a standard demon.')
    print(' ')
    print('*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*')
    print('A Pixie level 2 was added to your demon list.')
    print('*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*')
    print(' ')


#  Just text
def prompt_start():
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print('Welcome to the demon summuning program.')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print(' ')
    print('Press the X key to register a demon, Y to see your demon compendium, B to exit or C to clear the demon list.')
    print('___________________________________________________________________________________________________________')
    print('If this is your first time using this program press C to receive a demon list.')
    print('___________________________________________________________________________________________________________')


#  Just text
def start_registering_prompt():
    print(' ')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print('Please insert a comma and a space between the name and the level of the demon.')
    print('Ex: Thor, 76.')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print(' ')
    print('Please provide the demon name and level.')


def demon_list_visualizer():
    with open('demon_list', 'rb') as dl:
        demon_list = pickle.load(dl)
        for index in range(len(demon_list)):
            print(index + 1, demon_list[index])


def transform_imput():
    start_registering_prompt()
    new_demon = input('>>>')
    if ',' in new_demon:
        comma = new_demon.find(',')
        demon = (new_demon[:comma], int(new_demon[comma + 1:].strip()))
        with open('demon_list', 'rb') as dl:
            demon_visualizer = pickle.load(dl)
            demon_visualizer.append(demon)
        with open('demon_list', 'wb') as dl:
            pickle.dump(demon_visualizer, dl, pickle.HIGHEST_PROTOCOL)
    else:
        raise NameError("Couldn't locate the comma or invalid syntax, please try again.")
    print(f'{new_demon[:comma]} was registered with success.')
    print(' ')


def clear_demon_list():
    creat_demon_list = [('Pixie', 2)]
    with open('demon_list', 'wb') as dl:
        pickle.dump(creat_demon_list, dl, pickle.HIGHEST_PROTOCOL)
        clear_data()


def program():
    prompt_start()
    key = input('>>>')
    clean_key = key.lower().strip()
    while clean_key != 'b':
        if clean_key == 'y':
            demon_list_visualizer()
        elif clean_key == 'x':
            transform_imput()
        elif clean_key == 'c':
            print('Clear all demon data? Y/N.')
            answer = input('>>>').lower().strip()
            if answer == 'y':
                clear_demon_list()
            elif answer == 'n':
                print('Returning to the main program.')
                print(' ')
                pass
            elif answer != 'y' or 'n':
                raise NameError('Invalid answer. Press F10 to restart the program.')
        else:
            raise NameError('Unregistered key, please insert a valid key. Press F10 to restart the program.')
        print('Press the X key to register a demon, Y to see the demon compendium or B to exit.')
        key = input('>>>')
        clean_key = key.lower().strip()
    print(' ')
    print('__Quitting__')


program()

