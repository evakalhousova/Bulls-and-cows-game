"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Eva Kalhousová
email: eva.kalhousova@gmail.com
discord: evakalhousova
"""

import random

def check_letters(guess):
    if not guess.isnumeric():
        print(f'The entered number must contain only digits. Enter a new number.')
        return False
    else:
        return True

def check_digits(guess):
    guess = [int(item) for item in guess]
    if len(guess) < 4:
        print(f'The entered number has less than 4 digits. Enter a new number.')
        return False
    elif len(guess) > 4:
        print(f'The entered number has more than 4 digits. Enter a new number.')
        return False
    elif len(set(guess)) != 4:
        print(f'The entered number contains duplicate values. Enter a new number.')
        return False
    elif guess[0] == 0:
        print(f'The entered number starts with 0. Enter a new number.')
        return False
    else:
        return True

def check_guess(guess):
    while True:
        if check_letters(guess):
            if check_digits(guess):
                break
        print('-' * 40)
        guess = input('>>> ')
    return guess

def count_correct_digits(guess):
    guess = [int(item) for item in guess]
    bulls = 0
    cows = 0
    for index, digit in enumerate(guess):           # Enumerate list to number iterations, the same number is the index as well
        if digit in number and digit == number[index]:
            bulls = bulls + 1
            continue
        elif digit in number and digit != number[index]:
            cows = cows + 1
            continue
        else:
            continue
    return bulls, cows

def show_hints(guess):
    bulls, cows = count_correct_digits(guess)
    if bulls == 1 and cows == 1:
        print(f'{bulls} bull, {cows} cow')
    elif bulls == 1:
        print(f'{bulls} bull, {cows} cows')
    elif cows == 1:
        print(f'{bulls} bulls, {cows} cow')
    else:
        print(f'{bulls} bulls, {cows} cows')

def show_result(number_of_guesses):
    if number_of_guesses == 1:
        print(f"Correct, you've guessed the right number in 1 guess!")
    else:
        print(f"Correct, you've guessed the right number in {number_of_guesses} guesses!")
    print('-' * 40)

def evaluate_number_of_guesses(number_of_guesses):
    if number_of_guesses < 5:
        print("That's amazing!")
    elif number_of_guesses < 10:
        print("That's average!")
    else:
        print("That's not so good!")

number = []

first_digit = random.randrange(1, 9)
number.append(first_digit)

while len(number) < 4:
    new_digit = random.randrange(0, 9)
    if new_digit not in number:
        number.append(new_digit)

print(f'Generated number: {number}')            # Just for Python instructor to see the generated number when playing.

print('Hi there!')
print('-' * 40)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print('-' * 40)
print('Enter a number:')
print('-' * 40)

guess = input('>>> ')
number_of_guesses = 1
guess_checked = [int(item) for item in check_guess(guess)]

while guess_checked != number:
    show_hints(guess_checked)
    print('-' * 40)
    guess = input('>>> ')
    guess_checked = check_guess(guess)
    guess_checked = [int(item) for item in check_guess(guess)]
    number_of_guesses = number_of_guesses + 1

show_result(number_of_guesses)
evaluate_number_of_guesses(number_of_guesses)
