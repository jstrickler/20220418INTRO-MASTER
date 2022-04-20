from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Andy")

print(d1)  # print(str(d1))

# NAUGHTY!!!
# print(d1._dealer)

# 1. getter method
print(d1.get_dealer())

# 2. getter property
print(d1.dealer)
print(type(d1.dealer))

# setter property
d1.dealer = "Nellie"
print(d1.dealer)

try:
    d1.dealer = 123.456
except TypeError as err:
    print(err)
else:
    print(d1.dealer)

d1.shuffle()

print(d1.cards)
print()

for _ in range(10):
    print(d1.draw())
print()

print(d1.get_suits())

print(CardDeck.get_suits())
print('-' * 60)

j = JokerDeck("Little Bear")
print(j)
j.shuffle()
print(j.cards)

print(len(d1), len(j))


print(d1, j)



