import settings
import functions
import pardazesh
import sys
import os
from colorama import Fore


user_exit = False
state = "main_menu"
changes = []

u = open('back_slash.txt')
u = u.readline()

py_file_path = os.path.abspath(__file__)

py_file_path = functions.folder_without_file_name(py_file_path, u)

entry = pardazesh.Processing_sentence(input('Please Enter Command').replace('"', ''))
#print(entry)
#print(entry[:2])
state = 'insert'
#print(entry[:2])
while not user_exit:
    if state in settings.MENUS_VALID_STATES:
        if state == "main_menu":
            print(Fore.WHITE, functions.main_menu())
            try:
                state = settings.MENUS_VALID_STATES[int(input())]
                #print(state)
            except:
                print(Fore.RED, settings.ERROR[0])
                state = 'main_menu'
        elif state == "insert":

            tempo = functions.insert_menu(py_file_path, entry[0:2])
            if len(tempo) == 1:
                state = 'main_menu'
            else:
                #image, image_address, state, pos = tempo
                image = tempo[0]
                image_address = tempo[1]
                pos = tempo[2]
                #print(pos)
                #print(Fore.GREEN, settings.SUCCESS)
            if entry[2] == 'edit':
                state = 'edit'
            #state = 'main_menu'
        elif state == "export":
            try:
                #print(entry[0], entry[1], entry[-1])
                functions.export_menu(image, entry[0], entry[1], entry[-1])
            except:
                print(Fore.RED, settings.ERROR[2])
            state = 'main_menu'
        elif state == "edit":
            try:
                state = functions.edit_menu(image, entry[3:-1])
                if len(state) == 2:
                    image = state[0]
                    #changes.append(settings.CHANGES[state[1] - 1])
                    changes = state[1]
                #if state != 'main_menu':
                    #image = state
                state = 'main_menu'
                #print(Fore.GREEN, settings.SUCCESS)
            except:
                print(Fore.RED, settings.ERROR[2])
                state = 'main_menu'
            state = 'export'
        elif state == 'preview':
            try:
                image.show()
            except:
                print(Fore.RED, settings.ERROR[2])
            state = 'main_menu'
        elif state == 'show_changes':
            if len(changes) != 0:
                functions.show_changes(changes)
            else:
                print(Fore.RED, settings.ERROR[3])
            state = 'main_menu'
        else:
            sys.exit()
    else:
        functions.state_error()
    #print(changes)

