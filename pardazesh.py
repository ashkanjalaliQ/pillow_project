import re
import settings

def Processing_sentence(sentence):
    return sentence.split()


def find_max(ls):
    _max_ = max(ls)
    for i in range(len(ls)):
        if ls[i] == _max_:
            return i

def check_command():
    user_exit = True
    error = False
    while user_exit:
        entry = input('Please Enter Command').replace('"', '')
        if '-r' in entry:
            if len(re.findall('-r [A-Z:a-z_]*.(png|jpg|jpeg|gif) edit (grayscale|negative|blackandwhite|contour|edgeenhance|emboss|findedges|blur|smooth)* [a-z]*', entry)) != 0 or len(re.findall('-r [A-Za-z1-9.]*.(png|jpg|jpeg|gif) tool image_to_text [a-z]*', entry)) != 0:
                user_exit = False
            if user_exit == True:
                error = True
        elif '-nr' in entry:
            if '/' in (entry.split()[1]).split('.')[0] or ('_' in (entry.split()[1]).split('.')[0] or '-' in (entry.split()[1]).split('.')[0] or '(' in (entry.split()[1]).split('.')[0] or ')' in (entry.split()[1]).split('.')[0]):
                if len(re.findall('-nr [^,;]+.(png|jpg|jpeg|gif) edit (grayscale|negative|blackandwhite|contour|edgeenhance|emboss|findedges|blur|smooth)* [a-z]*',entry)) != 0 or len(re.findall('-nr [^,;]+.(png|jpg|jpeg|gif) tool image_to_text (fas|eng) [a-z]*', entry)) != 0:
        
                    user_exit = False
                if user_exit == True:
                    error = True
        elif len(re.findall('-o camera edit (grayscale|negative|blackandwhite|contour|edgeenhance|emboss|findedges|blur|smooth)* [a-z]*', entry)) != 0:
            user_exit = False
            
        elif entry == '--help':
            print(settings.HELP)
        
        else:
            print(settings.ERROR[0])
        
        if error == True:
            print(settings.ERROR[0])
    return user_exit, Processing_sentence(entry)

def recommender(word, options):
    p = []
    word = word.strip()
    for option in options:
        t = 0
        for letter in option.strip():
            if letter in word:
                t += 1
        p.append(t / len(option))

    return options[find_max(p)]
