i = 0
while i < 5:
    print(i)
    i += 1
print()

while True:
    user_name = input("Enter user name (or q to quit): ")
    if user_name == 'q':
        break  # exit loop
    elif user_name == '':
        continue # go to top (while statement)
    user_state = input("Enter state abbr: ")
    print(f"{user_name} is from {user_state}")

