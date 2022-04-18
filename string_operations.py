
actor = "Chris Hemsworth"
a1 = actor.upper()
print(a1)
print("actor.upper(): {}".format(actor.upper()))
print("actor: {}".format(actor))
print("actor.lower(): {}".format(actor.lower()))

s = "foo_bar"  #  FooBar
print("s.title().replace('_',''): {}".format(s.title().replace('_','')))
print(actor.replace('Chris', 'Liam'))

s1 = actor.startswith('Chris')
s2 = actor.startswith('Liam')
print(s1, s2)

print(
    actor.startswith('Chris'), actor.startswith('Liam')
)

#  func()  func(arg)   func(arg1, arg2, ...)

print("actor: {}".format(actor))
pos = actor.find('Hem')
print(pos)
#  012345678
# "abc"
pos = actor.find("wombat")
print(pos)

input = "1234"
print(input.isnumeric())
print(input.isdigit())
print(input.isalnum())
print(input.isalpha())

input = "    "
print(input.isspace())
print()

s = "      All my exes live in Texas      "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s = "$1000.04"
money = s.lstrip('$')
print("money: {}".format(money))

print("actor: {}".format(actor))
print("actor.replace('Chris', 'Liam'): {}".format(actor.replace('Chris', 'Liam')))

state = "Mississippi"
print(state.replace('i','X'))


data  = "John:Smith:Bend:Oregon"

fields = data.split(':')
print("fields: {}".format(fields))


data = "bim bam boom"
x = data.split()
print(x)
print(x[0], x[2])















