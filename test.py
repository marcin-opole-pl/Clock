import re


def check_func(user_hour, user_min, user_sec):
    global STATE
    hour = 12
    minute = 12
    second = 12
    match_h = re.fullmatch(r'(^[0]?[0-9]?|[1]?[0-2]?$)', user_hour)
    match_m = re.fullmatch(r'(^[0]?[0-9]?|[1-5]?[0-9]?$)', user_min)
    match_s = re.fullmatch(r'(^[0]?[0-9]?|[1-5]?[0-9]?$)', user_sec)
    # Check corectness of input format
    # User's input is blank '' '' ''
    if user_hour == '' or user_min == '' or user_sec == '':
        print('Wrong input format')
    # User's input is in corrrect format
    elif match_h and match_m and match_s:
        # Correct answer
        if int(user_hour) == hour and int(user_min) == minute and int(user_sec) == second:
            print('Correct answer')
        # Incorrect answer
        else:
            print('Wrong answer')
# User's input in incorrect format eg. 'dog'
    else:
        print('Wrong input format')

user_hour = input('Hour: ')
user_min = input('minute: ')
user_sec = input('second: ')

check_func(user_hour, user_min, user_sec)