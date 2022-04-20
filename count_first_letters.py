from pprint import pprint

letter_counts = {}

with open('DATA/words.txt') as words_in:
    for word in words_in:
        letter = word[0]
        if letter in letter_counts:
            letter_counts[letter] = letter_counts[letter] + 1
        else:
            letter_counts[letter] = 1

pprint(letter_counts)

