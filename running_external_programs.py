from subprocess import run, PIPE, CalledProcessError
import shlex
from glob import glob

CMD = "netstat -an"
CMD_WORDS = shlex.split(CMD)

print("CMD: {}".format(CMD))
print("CMD_WORDS: {}".format(CMD_WORDS))

# run cmd, don't capture output
run(CMD_WORDS)

print('-' * 60)
print('-' * 60)

proc = run(CMD_WORDS, stdout=PIPE)
output = proc.stdout
output_lines = output.splitlines()
print("len(output_lines): {}".format(len(output_lines)))
print("output_lines[:4]: {}".format(output_lines[:4]))
print()

established_connections = [line for line in output_lines if b'LISTEN' in line]

for conn in established_connections:
    fields = conn.split()
    proto = fields[0]
    print(proto)





