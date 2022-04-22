from collections import Counter

words = ['spam', 'spam', 'poutine', 'spam', 'spam', 'spam',
         'spam', 'eggs', 'spam', 'spam', 'spam', 'eggs',
         'spam', 'poutine', 'back bacon',
         'spam', 'spam', 'spam', 'peameal bacon',
         'spam', 'spam', 'spam', 'spam', 'eggs',
         'back bacon', 'back bacon', 'Montreal smoked meat']

word_counter = Counter(words)

print(word_counter)

with open('DATA/words.txt') as words_in:
    letters = [word[0] for word in words_in]
    letter_counter = Counter(letters)
    print(letter_counter, '\n')
    print(letter_counter.most_common(5))

