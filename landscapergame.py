username = input('What is your name? ')
print(f'Your name is {username}')

start_response = input(f'Welcome {username}. You have started a landscaping business! Using your teeth, save up and conquer the landscaping world! Type (y) for yes to continue to play the game: ')

if start_response == 'y':
    print('Continue')
else:
    print('Exit the game')
    exit()

days = 0
dollars = 0

print('Using just your teeth, you can spend the day cutting lawns and make $1. You can do this as much as you want.')

when_using_teeth = True

while when_using_teeth:
    cut_response = input('Would you like to cut lawns today? Type (y) for yes to continue to play the game:')
    if cut_response == 'y':
        days += 1
        dollars += 1
        print(f'Continue, This is Day {days} and you have {dollars} dollars')
    else:
        print('Exit the game')
        exit()
    if dollars >= 5:
        scissor_response = input('You can buy a pair of rusty scissors for 5 dollars. Would you like to buy them? If yes, type (y), if no, type (n).')
        if scissor_response == 'y':
            dollars -= 5
            print(f'Continue, This is Day {days} and you have {dollars} dollars. You now have a pair of rusty scissors.')
            when_using_teeth = False

use_rusty_scissors = True

while use_rusty_scissors:
    cut_response = input('Would you like to cut lawns today? Type (y) for yes to continue to play the game:')
    if cut_response == 'y':
        days += 1
        dollars += 5
        print(f'Continue, This is Day {days} and you have {dollars} dollars')
    else:
        print('Exit the game')
        exit()
    if dollars >= 25:
        old_mower_response = input('You can buy an old-timey push lawnmower for 25 dollars. Would you like to buy them? If yes, type (y), if no, type (n).')
        if old_mower_response == 'y':
            dollars -= 25
            print(f'Continue, This is Day {days} and you have {dollars} dollars')
            use_rusty_scissors = False

old_mower_response = True

while old_mower_response:
    cut_response = input('Would you like to cut lawns today? Type (y) for yes to continue to play the game:')
    if cut_response == 'y':
        days += 1
        dollars += 50
        print(f'Continue, This is Day {days} and you have {dollars} dollars')
    else:
        print('Exit the game')
        exit()
    if dollars >= 250:
        bat_powered_response = input('You can buy a fancy battery-powered lawnmower for 250 dollars. Would you like to buy them? If yes, type (y), if no, type (n).')
        if bat_powered_response == 'y':
            dollars -= 250
            print(f'Continue, This is Day {days} and you have {dollars} dollars')
            old_mower_response = False

bat_powered_response = True

while bat_powered_response:
    cut_response = input('Would you like to cut lawns today? Type (y) for yes to continue to play the game: ')
    if cut_response == 'y':
        days += 1
        dollars += 100
        print(f'Continue, This is Day {days} and you have {dollars} dollars')
    else:
        print('Exit the game')
        exit()
    if dollars >= 500:
        starve_students = input('You can hire a team of starving students for 500 dollars. Would you like to buy them? If yes, type (y), if no, type (n).')
        if starve_students == 'y':
            dollars -= 500
            print(f'Continue, This is Day {days} and you have {dollars} dollars. You now have a team of starving students.')
            bat_powered_response = False

starve_students = True

while starve_students:
    cut_response = input('Would you like to cut lawns today? Type (y) for yes to continue to play the game:')
    if cut_response == 'y':
        days += 1
        dollars += 250
        print(f'Continue, This is Day {days} and you have {dollars} dollars')
    else:
        print('Exit the game')
        exit()
    if dollars >= 1000:
        print('You have won the game!')
        print(f'Continue, This is Day {days} and you have {dollars} dollars. You now have a team of starving students.')
        exit()
