import re
import settings

def check_command():
    user_exit = True
    entry = input('Please Enter Command').replace('"', '')
    user_exit = False
    return user_exit, entry.split()


def find_max(ls):
    _max_ = max(ls)
    for i in range(len(ls)):
        if ls[i] == _max_:
            return i



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
