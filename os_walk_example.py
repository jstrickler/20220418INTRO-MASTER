import os

GIT_FOLDER = '.git'

START_DIR = "."

for directory, subs, files in os.walk(START_DIR):
    for sub in subs:
        if sub.startswith(('.', '_')):
            subs.remove(sub)
    print(directory)
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(directory, file_name)
            file_size = os.path.getsize(file_path)
            print(f" {file_size:8d} {file_name}")

