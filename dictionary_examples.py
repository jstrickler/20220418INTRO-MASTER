from pprint import pprint

d1 = dict()  # empty dict
d2 = {'a': 3, 'm': 19, 'd': 48, 'r': 11}
print(d2['a'], d2['r'])
d3 = {}  # empty dict

# dict(iterable-of-pairs)

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(len(airports))
airports['DFW'] = 'Dallas-Fort Worth'
if 'RDU' in airports:
    print("already exists")
else:
    airports['RDU'] = 'Durham'

airports['MIA'] = "Miami"

pprint(airports)
airports['ORD'] = 'Chicago'

print(airports['YOW'])
print()

# print(airports['DCA'])
print(airports.get('YOW', 'NOT FOUND'))
print(airports.get('DCA'))
print(airports.get('DCA', 'NOT FOUND'))

for key in airports:  #  airports.keys()
    print(key)
print('-' * 60)

for code, name in airports.items():
    print(code, name)
print('=' * 60)
print(airports.items())

#  DICT.keys()  DICT.values()  DICT.items()


















