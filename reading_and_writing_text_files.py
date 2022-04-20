import csv

file_path = "DATA/mary.txt"

mary_in = open(file_path, "r")
# read file here...
mary_in.close()
print("mary_in: {}".format(mary_in))
print()

# with EXPR as VARIABLE:
with open(file_path) as mary_in:
    pass
    # mary_in.close()

# read file line-by-line
with open(file_path) as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()  # remove \n
        print(line)
print('-' * 60)

# read whole file into a string
with open(file_path) as mary_in:
    whole_file = mary_in.read()  # read everything
    print("RAW:")
    print(repr(whole_file))
    print("NORMAL:")
    print(whole_file)  # print(str(whole_file))
print('-' * 60)

# read whole file into list WITHOUT newlines
with open(file_path) as mary_in:
    whole_file = mary_in.read()
    lines_without_nl = whole_file.splitlines()
    print(lines_without_nl)
print('-' * 60)

# read whole file into list WITH newlines
with open(file_path) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

target = 'Gates'

with open('DATA/computer_people.txt') as people_in:
    for raw_line in people_in:
        if 'Gates' in raw_line:
            print(raw_line.rstrip())
print('-' * 60)

with open('DATA/computer_people.txt') as people_in:
    # header = next(people_in)  # skip 1st line
    for raw_line in people_in:
        line = raw_line.rstrip()
        first_name, last_name, product, dob = line.split(';')
        if first_name == 'Larry':
            print(first_name, last_name)
print('-' * 60)

with open('DATA/computer_people.txt') as people_in:
    with open('larry.txt', 'w') as larry_out:
        with open('larry.csv', 'a') as csv_out:
            wtr = csv.writer(csv_out)
            for raw_line in people_in:
                line = raw_line.rstrip()
                fields = line.split(';')
                if fields[0] == 'Larry':
                    larry_out.write("\t".join(fields) + '\n')
                    wtr.writerow(fields)


# opening files
#  r  read
#  w  write
#  a  append
#  x  fail if exists else write

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

with open('numbers.txt', 'w') as numbers_out:
    for num in nums:
        numbers_out.write(str(num) + '\n')






