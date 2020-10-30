import re
import settings

def check_command():
    user_exit = True
    entry = input('Please Enter Command').replace('"', '')
    user_exit = False
    return user_exit, entry.split()
