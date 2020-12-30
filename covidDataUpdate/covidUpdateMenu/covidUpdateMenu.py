import dataFetch
import random
from datetime import datetime

currentTime = '{}-{}-{}'.format(datetime.now().strftime('%d'), datetime.now().strftime('%m'), datetime.now().strftime('%Y'))
invalidInputString = ['Please answer the question', "That's not a valid answer", 'Uhh.. Read the question again']

def firstMenu():
    print('''Type 1 to update or get info on the cases database
Type 2 to update or get info on the deaths database''')

    case = input()

    if case == str(1):
        secondMenu('cases')
    elif case == str(2):
        secondMenu('mortality')
    else:
        print('Please choose an option')
        firstMenu()

def secondMenu(info):
    print('''Type 1 to update database with today's data ({})
Type 2 to update database with all data up to today (01-01-2020 - {})
Type 3 to update database within a certain period
Type 'back' to go back to the first menu
Type 'exit' to end the program'''.format(currentTime,currentTime))

    case = input()

    if case == str(1):
        dataFetch.dbFetch(info, currentTime, currentTime)
    elif case == str(2):
        dataFetch.dbFetch(info, '01-01-2020', currentTime)
    elif case == str(3):
        initDate = input('Starting date (dd-mm-YYYY): ')
        lastDate = input('Up to (dd-mm-YYYY): ')
        dataFetch.dbFetch(info, initDate, lastDate)
    elif case == 'back':
        firstMenu()
    elif case == 'exit':
        print('goodbye then!')
        return()
    else:
        print('Please choose an option')
        secondMenu(info)

    print('Do you want to update anything else? ')
    repeatRequest()
    return()

def repeatRequest():
    repeat = input()
    if repeat == 'yes' or repeat == 'y':
        firstMenu()
    elif repeat == 'no' or repeat == 'n':
        print('Okay then, bye!')
        return()
    else:
        print(invalidInputString[random.randrange(len(invalidInputString))])
        repeatRequest()

firstMenu()
