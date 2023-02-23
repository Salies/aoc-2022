f = open('inputs/day6.txt', 'r')
lines = f.readlines()
f.close()

line = lines.pop(0).strip()

i = 0
# each 4 characters, check if they're all unique
while len(set(line[i:i+4])) != 4:
    i += 1
print("Part one:", i + 4)