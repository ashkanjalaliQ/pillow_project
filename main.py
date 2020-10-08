import settings
import functions
import pardazesh
import sys
import pytesseract
import re
import os
from colorama import Fore

changes = []

u = open('back_slash.txt')
u = u.readline()

py_file_path = os.path.abspath(__file__)

py_file_path = functions.folder_without_file_name(py_file_path, u)


user_exit, entry = pardazesh.check_command()

state = 'insert'

while not user_exit:
    if state in settings.MENUS_VALID_STATES:
        if state == "main_menu":
            pass
        elif state == "insert":
            tempo = functions.insert_menu(py_file_path, entry[0:2])
            if len(tempo) == 1:
                state = 'main_menu'
            else:
                image = tempo[0]
                image_address = tempo[1]
                pos = tempo[2]
            if entry[2] == 'edit':
                state = 'edit'
            elif entry[2] == 'tool':
                state = 'tool'
        elif state == "export":
            if 'tool' in entry:
                try:
                    functions.export_menu('.', entry[0], entry[1], entry[-1], response)
                except:
                    print(Fore.RED, settings.ERROR[4])
            else:
                try:
                    functions.export_menu(image, entry[0], entry[1], entry[-1])
                except:
                    print(Fore.RED, settings.ERROR[2])
            user_exit = True
        elif state == "edit":
            try:
                state = functions.edit_menu(image, entry[3:-1])
                if len(state) == 2:
                    image = state[0]
                    changes = state[1]
                state = 'main_menu'
            except:
                print(Fore.RED, settings.ERROR[2])
                state = 'main_menu'
            state = 'export'

        elif state == "tool":
            pytesseract.pytesseract.tesseract_cmd = r'C:\Users\lenovo\AppData\Local\Tesseract-OCR\tesseract'

            response = pytesseract.image_to_string(entry[1], lang=entry[4]).strip()
            '''file = open(entry[-1] + '.txt', 'w')
            file.write(response)
            file.close()'''
            state = 'export'
        else:
            sys.exit()
    #else:
        #functions.state_error()

print(Fore.WHITE, 'Tamam')