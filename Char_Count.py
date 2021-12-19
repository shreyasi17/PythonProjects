import pprint

print('ENTER A STRING')
message = input()

count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character]+1

rjtext = pprint.pformat(count)

print(rjtext)
