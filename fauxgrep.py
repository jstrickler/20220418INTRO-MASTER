import fileinput
import re
from argparse import ArgumentParser

#         sys.argv[0]    [1]      [2]   [3]
#  python fauxgrep.py -i -n search-term file1 file2 ...

#  -i ignore case
#  -n print file name

description = """
Faux grep

Searches for regular expressions in text files, and prints out
matching lines.
"""

parser = ArgumentParser(description=description)

parser.add_argument('-i', dest="ignore_case", action="store_true", help="Ignore case")
parser.add_argument('-n', dest="show_file_name", action="store_true", help="Print file name")
parser.add_argument("regex", help="Regular expression to find")
parser.add_argument("files", nargs="+", help="Files to search")

args = parser.parse_args()  # parses sys.argv

print("args: {}".format(args))

regex = re.compile(args.regex, re.I if args.ignore_case else 0)

for raw_line in fileinput.input(args.files):
    if regex.search(raw_line):
        line = raw_line.rstrip()
        if args.show_file_name:
            print(fileinput.filename(), end=' ')
        print(line)


