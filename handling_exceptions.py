
file_path = 'DATA/wombats.txt'

try:
    with open(file_path) as file_in:
        for raw_line in file_in:
            line = raw_line.rstrip()
            print(line)
except FileNotFoundError as err:
    print(err)

with open('DATA/breakfast.txt') as food_in:
    food = food_in.read().splitlines()
try:
    print(food[35])
except IndexError as err:
    print(err)

nums = [800, 0, 80, None, 1000, 32, "abc", 255, 14, "123", 400, 5, 5000]

for num in nums:
    try:
        result = 7500 / int(num)
    except ZeroDivisionError as err:
        print(err)
        # provide alternate value
        # log the error
        # shut down gracefully
        # skip this value
        # ???
    except (ValueError, TypeError) as err:
        print("HUH!", err)
    except Exception as err:
        print("UNEXPECTED!!", err)
    else:
        print(result)






print("ALL DONE")
