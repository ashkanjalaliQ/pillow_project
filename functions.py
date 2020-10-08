import settings
from effects import color_effect
from PIL import Image
from colorama import Fore
from pardazesh import recommender


def folder_without_file_name(address, split_by):
    address = address.split(split_by)[:-1]
    add_slash = ''
    for i in range(len(address)):
        add_slash += address[i] + '//'
    return add_slash[:-2]

def main_menu():
    return settings.MAIN_MENU

def insert_menu(py_file_path, image_address):
    if len(image_address) != 2:
        status = 'main_menu'
        return status
    pos = image_address[0]
    image_address = image_address[1]


    image = Image.open(image_address)

    image_address = folder_without_file_name(image_address, '//')
    if pos == '':
        if image_address == py_file_path:
            pos = '-r'
        else:
            pos = '-nr'
    try:
        return [image, image_address, pos]
    except:
        return 'back'

def export_menu(image, pos, image_address, file_name, response='.'):

    if file_name == 'back':
        status = 'main_menu'
        return status
    if pos == '-nr':
        image_address = folder_without_file_name(image_address, '//')

    if pos == '-nr':
        image_address += '//' + file_name
    else:
        image_address = file_name


    if image != '.':
        image_address += '.jpg'
        image.save(image_address)

    else:
        image_address += '.txt'
        '''file = open(image_address, 'w')
        file.write(response)
        file.close()'''

        with open(image_address, 'w') as text_file:
            text_file.write(response)


def edit_menu(image, options):

    switch = [
        'grayscale',
        'negative',
        'blackandwhite',
        'contour',
        'edgeenhance',
        'emboss',
        'findedges',
        'blur',
        'smooth'
    ]

    effects = [
        color_effect.gray_scale,
        color_effect.negative,
        color_effect.b_and_w,
        color_effect.contourfilter,
        color_effect.edgeenhance,
        color_effect.emboss,
        color_effect.findedges,
        color_effect.blur,
        color_effect.smooth
    ]
    changes = []

    for option in options:
        t = switch.index(recommender(option, switch))
        image = effects[t](image)
        effect_name = switch[t]
        changes.append(effect_name)
    return [image, changes]

def state_error():
    print(Fore.RED, settings.ERROR)
