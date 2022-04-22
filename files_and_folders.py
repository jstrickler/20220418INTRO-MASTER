import os
from datetime import datetime

FOLDER = "DATA"
FILE_NAMES = os.listdir(FOLDER)

for file_name in sorted(FILE_NAMES):
    if file_name.endswith('.txt'):
        file_path = os.path.join(FOLDER, file_name)
        print("file_path: {}".format(file_path))

        # open file and read data
        # open file; read data; search/replace; write new file

        print("os.path.exists(file_path): {}".format(os.path.exists(file_path)))

        file_size = os.path.getsize(file_path)
        print("file_size: {}".format(file_size))

        base_name = os.path.basename(file_path)
        print("base_name: {}".format(base_name))

        dir_name = os.path.dirname(file_path)
        print("dir_name: {}".format(dir_name))

        abs_path = os.path.abspath(file_path)
        print("abs_path: {}".format(abs_path))

        raw_file_timestamp = os.path.getmtime(file_path)
        print("raw_file_timestamp: {}".format(raw_file_timestamp))

        file_timestamp = datetime.fromtimestamp(raw_file_timestamp)
        print("file_timestamp: {}".format(file_timestamp))

        stat_info = os.stat(file_path)
        raw_create_time = stat_info.st_birthtime
        print("raw_create_time: {}".format(raw_create_time))
        file_create_time = datetime.fromtimestamp(raw_create_time)
        print("file_create_time: {}".format(file_create_time))

        print("stat_info: {}".format(stat_info))
        print('*' * 60, '\n')

