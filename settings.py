# State
MENUS_VALID_STATES = [
    "main_menu",
    "insert",
    "export",
    "edit",
    "preview",
    "show_changes",
    "exit"
]

# Menus
MAIN_MENU = """
Please Choose:
1. Insert new pic
2. Export New File
3. Edit
4. See Preview
5. Show Changes
6. Exit
"""
INSERT = """
Insert new pic: please Insert Pic Address
"""
EXPORT = """
Please Enter A Name:
"""
EDIT = """
Edit: please Choose:
1. Grayscale
2. Black and White
3. Negative
"""
ERROR = [
    "Error: Invalid Input, try agian...",
    "Error: there is no pic",
    "Error: Please Insert a image",
    "The photo has not been changed."
]

SUCCESS = """
[*]Done
"""

SEARCH = """
1. Easy Address
2. Enter the address manually
"""

# Changes
CHANGES = [
    'Grayscale',
    'Black and White',
    'Negative'
]

FILE_MODE = [
    '-nr',
    '-r'
]

HELP = """
Hello!
Welcome to the help page
When you come here, it means you have a question.
So solve your question using the guide below.
Or to participate in our project, visit our project on github: https://github.com/ashkanjalaliQ/pillow_project

@How to run the program?
>>> python main.py

@How to work?
>>> Please Enter Command
"[-nr/-r] + {image address}" edit {effect name} "{export name}"

Example:
"-r photo.png" edit grayscale negative blackandwhite "Salam_aziz"

@How many effects does our program support?
Our program supports 9 effects. This number will increase every day.

@Name effects:
    grayscale
    negative
    blackandwhite
    contour
    edgeenhance
    emboss
    findedges
    blur
    smooth
"""