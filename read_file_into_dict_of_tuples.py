from pprint import pprint

knight_data = {}

file_path = "DATA/knights.txt"

with open(file_path) as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = title, color, quest, comment

pprint(knight_data)
print('-' * 60)

print("knight_data['Galahad']: {}".format(knight_data['Galahad']))

print("knight_data['Galahad'][2]: {}".format(knight_data['Galahad'][2]))
print()

#    key  value
for name, data in knight_data.items():
    print(data[0], name)
print()

