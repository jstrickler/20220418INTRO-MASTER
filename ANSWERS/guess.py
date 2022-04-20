#!/usr/bin/env python

max_value = 26
min_value = 0
tries = 1

while True:
    guess = (max_value + min_value) // 2
    answer = input(f"Is your number {guess}? ")

    if answer == "q":
        break
    elif answer == "h":
        max_value = guess
    elif answer == "l":
        min_value = guess
    elif answer == "y":
        print(f"I guessed it in {tries} tries!")
        break
    else:
        print("Please enter h, l, or y")

    if (answer == 'h') or (answer == 'l'):
        tries += 1
