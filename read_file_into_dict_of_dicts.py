from pprint import pprint

knight_data = {}

file_path = "DATA/knights.txt"

with open(file_path) as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = {
            'title': title,
            'color': color,
            'quest': quest,
            'comment': comment,
        }

pprint(knight_data)
print('-' * 60)

print("knight_data['Galahad']: {}".format(knight_data['Galahad']))

print("knight_data['Galahad']['quest]: {}".format(knight_data['Galahad']['quest']))
print()

#    key  value
for name, data in knight_data.items():
    print(data['title'], name)
print()

